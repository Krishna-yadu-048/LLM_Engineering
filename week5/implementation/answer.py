from pathlib import Path

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.messages import HumanMessage, SystemMessage, convert_to_messages
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI

MODEL = "gpt-5-mini"
embeddings = HuggingFaceEmbeddings(model_name = "all-miniLM-L6-v2")
retrival_k = 5

db_name = str(Path(__file__).parent.parent / "vetor_db")


SYSTEM_PROMPT = """
You are a knowledgeable, friendly assistant representing the company Insurellm.
You are chatting with a user about Insurellm.
If relevant, use the given context to answer any question.
If you don't know the answer, say so.
Context:
{context}
"""

vector_store = Chroma(persist_directory=db_name, embedding_function=embeddings)
retriver = vector_store.as_retriever()
llm = ChatOpenAI(temperature=0, model_name = MODEL)

#--------------------------------------------------------------------------------------------

def fetch_context(question: str) -> list[Document]:
    return retriver.invoke(question, k = retrival_k)

#--------------------------------------------------------------------------------------------

def combined_question(question: str, history: list[dict] = []) -> str:  # noqa: B006

    """This function sends all the user question combined to the LLM model to give it a better context regarding the conversation!!!"""

    past = '\n'.join(m["content"] for m in history if m['role'] == "user")
    return past + "\n" + question

#--------------------------------------------------------------------------------------------

def answer_question(question: str, history: list[dict] = []) -> tuple[str, list[Document]]:
    """
    Answer the given question with RAG; return the answer and the context documents.
    """
    combined = combined_question(question, history)
    docs = fetch_context(combined)
    context = "\n\n".join(doc.page_content for doc in docs)
    system_prompt = SYSTEM_PROMPT.format(context=context)
    messages = [SystemMessage(content=system_prompt)]
    messages.extend(convert_to_messages(history))
    messages.append(HumanMessage(content=question))
    response = llm.invoke(messages)
    return response.content, docs