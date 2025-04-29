# 📚 CTSE Lecture Notes Chatbot

> SE4010 – Current Trends in Software Engineering (Semester 1, 2025)  
> Assignment 2 – AI/ML: LLM Development Toolkit

---

## ✨ Project Overview

This project implements a **Retrieval-Augmented Generation (RAG)** based chatbot using **LangChain**, **Hugging Face models**, and **Chroma vector store**.  
The chatbot answers questions based on the **CTSE lecture notes**.

---

## 🚀 Features
- Load and process lecture notes (PDF)
- Split documents into searchable chunks
- Generate semantic embeddings using Hugging Face models
- Store and retrieve documents efficiently with ChromaDB
- Use a lightweight LLM (`flan-t5-base`) to generate answers
- Simple chatbot function for easy interaction

---

## 🛠️ Tech Stack
- **Python**
- **LangChain** – for chaining LLMs and retrievers
- **Hugging Face Transformers** – for embeddings and LLMs
- **Chroma** – vector database for document retrieval
- **Jupyter Notebook** – for implementation and testing

---

## 📦 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ctse-chatbot.git
cd ctse-chatbot
```

2. Install dependencies:
```bash
pip install langchain langchain-huggingface chromadb transformers torch
```

3. Ensure you have a Hugging Face API key if needed:
```bash
export HUGGINGFACEHUB_API_TOKEN=your_token_here
```

---

## 🧩 How It Works

1. **Load** CTSE lecture notes from a PDF file.
2. **Split** the notes into small, manageable chunks.
3. **Generate embeddings** using `sentence-transformers/all-mpnet-base-v2`.
4. **Store embeddings** into a Chroma vector database.
5. **Retrieve relevant chunks** when a question is asked.
6. **Generate final answers** using `google/flan-t5-base` language model.

---

## 🧪 Running the Notebook

1. Open the provided `ctse_chatbot.ipynb` notebook.
2. Follow the sequential cells:
   - Install libraries
   - Load documents
   - Split and embed documents
   - Set up retriever
   - Initialize LLM
   - Build and test the chatbot

3. Replace `CTSE_Lecture_Notes.pdf` with your actual file if needed.

---

## 🤖 Example Chat

```bash
🟡 Question: What is Agile methodology?
🟢 Answer: Agile methodology is a software development approach based on iterative development, where requirements and solutions evolve through collaboration between cross-functional teams.
```

---

## 📚 References
- [LangChain RAG Tutorial](https://python.langchain.com/docs/tutorials/rag/)
- [Hugging Face Model Hub](https://huggingface.co/models)
- [Chroma Documentation](https://docs.trychroma.com/)

---

## ⚡ Author

- Name: *didula bhanuka*
- University: *SLIIT*
- Course: *SE4010 – Current Trends in Software Engineering*
