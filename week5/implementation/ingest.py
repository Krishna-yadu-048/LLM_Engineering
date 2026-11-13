import glob
import os
from pathlib import Path

from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

MODEL = "gpt-5-mini"
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

db_name = str(Path(__file__).parent.parent / "vetor_db")
KNOWLEDGE_BASE = str(Path(__file__).parent.parent / "knowledge-base")

load_dotenv(override = True)
openai = os.getenv("OPENAI_API_KEY")

#------------------------------------------------------------------------------------------------ Writing function for fetching the documents

def fetch_docs():
    folders = glob.glob(str(Path(KNOWLEDGE_BASE)/ "*"))
    documents = []
    for folder in folders:
        doc_type = os.path.basename(folder)
        loader = DirectoryLoader(
                folder, 
                glob = "**/*.md",
                loader_cls = TextLoader,
                show_progress= True,
                loader_kwargs = {"encoding":"utf-8"}
        )
        folder_docs = loader.load()
        for doc in folder_docs:
            doc.metadata["doc_type"] = doc_type
            documents.append(doc)

    return documents

#------------------------------------------------------------------------------------------------ # Function for chunking the given documents

def chunking(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
    chunks = text_splitter.split_documents(documents)

    return chunks

#------------------------------------------------------------------------------------------------ # Function for creating Vector Store and Embedding the chunked documents

def vector_store_creation(chunks):
    if os.path.exists(db_name):
        Chroma(persist_directory=db_name, embedding_function=embeddings).delete_collection()

    vector_store = Chroma.from_documents(
                    documents = chunks,
                    embedding = embeddings,
                    persist_directory=db_name
    )

    collection = vector_store._collection
    count = collection.count()

    sample_embeddings = collection.get(limit =1, include = ["embeddings"])["embeddings"][0]
    dimensions = len(sample_embeddings)

    print(f"Vector Store has {count} vectors and each vector has {dimensions} dimensions.")

    return vector_store

#------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    documents = fetch_docs()
    chunks = chunking(documents)
    vector_store_creation(chunks)
    print("Ingestion Complete!!")