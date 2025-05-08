Here's an improved and corrected version of your GitHub README, based on your notebook content and the overall project structure. The changes improve clarity, grammar, and consistency, while highlighting the technical components accurately:

---

# 📚 CTSE Lecture Notes Chatbot

> SE4010 – Current Trends in Software Engineering (Semester 1, 2025)
> Assignment 2 – AI/ML: LLM Development Toolkit

---

## ✨ Project Overview

This project implements two intelligent chatbot systems based on **LangChain**, **ChromaDB**, and **Hugging Face models**, enabling students to query **CTSE lecture notes** through natural language.

---

## 🚀 Features

| Version                                 | Capabilities                                                         |
| :-------------------------------------- | :------------------------------------------------------------------- |
| **Simple RetrievalQA**                  | One-shot question answering with high speed and accuracy             |
| **Conversational Retrieval (Advanced)** | Multi-turn memory chatbot with chat history and contextual awareness |

---

## 🛠️ Tech Stack

* **Python**
* **LangChain** – LLM framework for retrieval and chaining
* **ChromaDB** – vector database for document indexing and retrieval
* **FastEmbed** – for embedding generation
* **Hugging Face Transformers** – for embedding models and LLMs
* **Ollama** – for running LLaMA models locally
* **Jupyter Notebook** – primary development environment

---

## 📦 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/didulabhanuka/LectureNotes-Chatbot.git
cd LectureNotes-Chatbot
```

2. **Install required packages:**

```bash
pip install langchain langchain-huggingface langchain-community fastembed chromadb transformers torch
```

3. **Set up environment variables::**

* Create a `.env` file in the project root directory and add your Hugging Face token:

```
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_key_here
```

---

## 📂 Notebooks Overview

| Notebook                                              | Description                                                                          |
| :---------------------------------------------------- | :----------------------------------------------------------------------------------- |
| `lecsnote-chatbot-SimpleRetrievalQA.ipynb`            | ✅ **Primary notebook** – Fast, one-shot question answering via `RetrievalQA`         |
| `lecsnote-chatbot-ConversationalRetrievalChain.ipynb` | 💬 **Advanced version** – Maintains chat history with `ConversationalRetrievalChain` |

---

## ⚙️ How It Works

1. **Load** CTSE lecture notes from PDF using `PyPDFLoader`.
2. **Split** content into chunks using `RecursiveCharacterTextSplitter`.
3. **Embed** the chunks using `FastEmbedEmbeddings`.
4. **Store and retrieve** using `Chroma` vector store.
5. **Query** the documents using a retriever with a similarity score threshold.
6. **Answer** using LLaMA models (e.g., TinyLLaMA) via **Ollama**, integrated into LangChain.

---

## 🧠 Model Details

* **Embedding Model**: `FastEmbed` (built-in via LangChain)
* **Language Model**: `tinyllama` (run locally via Ollama)
* **Prompting**: Custom prompt templates for conversational QA
* **Memory (Advanced)**: `ConversationBufferMemory` for chat history

---

## ✅ Deliverables

* 📓 Jupyter Notebook (Simple RetrievalQA recommended)
* 📄 PDF Report
* 📹 Demo Video (2–3 minutes)

---

## 📚 References

* [LangChain RAG Tutorial](https://python.langchain.com/docs/tutorials/rag/)
* [Hugging Face Model Hub](https://huggingface.co/models)
* [ChromaDB Documentation](https://docs.trychroma.com/)
* [Ollama: Open Source LLMs](https://ollama.com/)

---
