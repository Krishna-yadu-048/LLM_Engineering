# LLM Engineering: Course Notes & Code

My notes, code, and experiments from **Ed Donner's [AI Engineering Core Track: LLM Engineering](https://www.udemy.com/)** course on Udemy.

The course covers building real-world applications with large language models: frontier and open-source model APIs, building interfaces, retrieval-augmented generation (RAG), fine-tuning, and agentic workflows. This repo is my learning log as I work through it week by week.

> **Credit:** The course and its original materials are by [Ed Donner](https://github.com/ed-donner). The official course repo is at [ed-donner/llm_engineering](https://github.com/ed-donner/llm_engineering). This repo contains my own notes, modifications, and experiments.

---

## 📂 Contents

| Week | Topic | Highlights |
|------|-------|------------|
| [Week 1](./week1) | Frontier models & the LLM landscape | Calling the OpenAI API, running local models with Ollama, prompt basics (system vs. user prompts), a website summarizer, structured outputs |
| [Week 2](./week2) | Frontier APIs & building UIs | Working with multiple providers (OpenAI, Anthropic, Google), streaming responses, building chat UIs with Gradio, tool calling, multimodal assistants |
| Week 3+ | *In progress* | Open-source models (Hugging Face), RAG, fine-tuning, agents |

---

## 🛠️ Tech Stack

- **Python** (managed with [uv](https://github.com/astral-sh/uv))
- **LLM APIs:** OpenAI, Anthropic, Google Gemini
- **Local models:** Ollama
- **UI:** Gradio
- **Notebooks:** Jupyter

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/Krishna-yadu-048/<repo-name>.git
cd <repo-name>
```

### 2. Install dependencies

This project uses `uv`:

```bash
uv sync
```

### 3. Add your API keys

Create a `.env` file in the project root (it is excluded by `.gitignore`):

```env
OPENAI_API_KEY=your-key-here
ANTHROPIC_API_KEY=your-key-here
GOOGLE_API_KEY=your-key-here
```

You only need keys for the providers you plan to use. Week 1 can be run entirely with Ollama if you'd rather not use a paid API.

### 4. Run the notebooks

```bash
uv run jupyter lab
```

---

## 📝 Key Takeaways

*A running list of the concepts that stuck with me.*

**Week 1**
- The difference between system and user prompts, and how much the system prompt shapes output
- Open-source models via Ollama are a free, private alternative to frontier APIs for experimenting
- <!-- add your own -->

**Week 2**
- Most providers follow an OpenAI-compatible chat format, which makes switching between them easy
- Gradio makes it fast to put a UI on top of an LLM for demos
- Tool calling lets the model decide when to call your own Python functions
- <!-- add your own -->

---

## 📌 Status

🟢 Actively working through the course. Notes are updated as I complete each week.

---

## 📄 License & Attribution

Course content and original exercises © Ed Donner. My own notes and code in this repo are shared for learning purposes.