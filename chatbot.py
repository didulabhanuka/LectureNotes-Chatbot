from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import FastEmbedEmbeddings
from langchain.vectorstores import Chroma
from langchain_community.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
hf_token = os.getenv("HUGGINGFACEHUB_API_TOKEN")
if hf_token is None:
    raise ValueError("HUGGINGFACEHUB_API_TOKEN is not set in environment variables")
os.environ["HUGGINGFACEHUB_API_TOKEN"] = hf_token

# File paths
PDF_PATH = "ctse_lecture_notes.pdf"
PERSIST_DIR = "./chroma_langchain_db"

# Step 1: Load & process PDF
def load_and_process_pdf():
    loader = PyPDFLoader(PDF_PATH)
    pages = loader.load_and_split()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=2048,
        chunk_overlap=200,
        length_function=len,
        add_start_index=True,
    )
    return splitter.split_documents(pages)

# Step 2: Create or load vector store
def get_vector_store(docs):
    embeddings = FastEmbedEmbeddings()
    if os.path.exists(PERSIST_DIR):
        return Chroma(persist_directory=PERSIST_DIR, embedding_function=embeddings)
    else:
        store = Chroma.from_documents(docs, embedding=embeddings, persist_directory=PERSIST_DIR)
        store.persist()
        return store

# Step 3: Set up retriever
def setup_retriever(vector_store):
    return vector_store.as_retriever(
        search_type="similarity_score_threshold",
        search_kwargs={"k": 3, "score_threshold": 0.5}
    )

# Step 4: Set up conversational QA chain
def setup_conversational_chain(retriever):
    llm = ChatOllama(model="tinyllama")
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful AI assistant. Use the provided context to answer the user's question. If you don't know the answer based on the context, say 'I don't know.'"),
        ("human", "Context:\n{context}\n\nQuestion: {question}")
    ])
    return ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        combine_docs_chain_kwargs={"prompt": prompt}
    )

# One-time initialization
_docs = load_and_process_pdf()
_vector_store = get_vector_store(_docs)
_retriever = setup_retriever(_vector_store)
_qa_chain = setup_conversational_chain(_retriever)

# Step 5: Ask function
def ask(query: str):
    # Check if any documents meet the similarity threshold
    relevant_docs = _retriever.invoke(query)
    if not relevant_docs:
        return "I don't know. The answer is not in the lecture notes."

    # Continue with the QA chain
    result = _qa_chain.invoke({"question": query})
    return result["answer"]
