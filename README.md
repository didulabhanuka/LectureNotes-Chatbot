# 📚 CTSE Lecture Notes Chatbot

> SE4010 – Current Trends in Software Engineering (Semester 1, 2025)  
> Assignment 2 – AI/ML: LLM Development Toolkit

---

## ✨ Project Overview

This project implements two versions of a chatbot using **LangChain**, **Hugging Face models**, and **ChromaDB**, capable of answering questions based on **CTSE lecture notes**.

---

## 🚀 Features
| Version | Features |
|:---|:---|
| **Simple RetrievalQA (Final)** | One-shot question answering, direct, fast, accurate |
| **Conversational Retrieval (Advanced)** | Chat memory, multi-turn conversations, context retention |

---

## 🛠️ Tech Stack
- **Python**
- **LangChain** – for LLM chaining
- **Hugging Face Transformers** – for embeddings and LLMs
- **Chroma** – vector database for efficient retrieval
- **Jupyter Notebook** – implementation environment

---

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/didulabhanuka/LectureNotes-Chatbot.git
cd ctse-chatbot
````

2. Install dependencies:
```bash
pip install langchain langchain-huggingface chromadb transformers torch
```

3. Authenticate with Hugging Face (if necessary):
```bash
export HUGGINGFACEHUB_API_TOKEN=your_token_here
```

---

## 📂 Available Notebooks

| Notebook Name | Description |
|:---|:---|
| `lecsnote-chatbot-SimpleRetrievalQA.ipynb` | **[Primary for assignment]** Fast and accurate one-shot question answering using RetrievalQA |
| `lecsnote-chatbot-ConversationalRetrievalChain.ipynb` | **[Advanced]** Multi-turn memory chatbot using ConversationalRetrievalChain |

---

## 🧩 How It Works

1. **Load** CTSE lecture notes from a PDF.
2. **Split** the notes into manageable text chunks.
3. **Generate embeddings** using `sentence-transformers/all-mpnet-base-v2`.
4. **Store embeddings** inside ChromaDB.
5. **Retrieve relevant context** for any question.
6. **Answer** using `flan-t5-large` Hugging Face model.

---

## 📜 Deliverables
- **Jupyter Notebook** (Simple RetrievalQA version recommended)
- **PDF Report**
- **Video Demonstration** (2–3 min demo)

---

## 📚 References
- [LangChain RAG Tutorial](https://python.langchain.com/docs/tutorials/rag/)
- [Hugging Face Model Hub](https://huggingface.co/models)
- [ChromaDB Documentation](https://docs.trychroma.com/)
