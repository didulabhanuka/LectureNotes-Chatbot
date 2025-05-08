import streamlit as st
from chatbot import ask  # Chat function with conversational memory

# Page setup
st.set_page_config(page_title="CTSE Chatbot", layout="wide")
st.title("📘 CTSE Lecture Notes Chatbot (LLaMA + LangChain)")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Chat input form
with st.form("chat_form", clear_on_submit=True):
    user_query = st.text_input("Ask a question about CTSE or Software Engineering:")
    submit = st.form_submit_button("Ask")

# Process query
answer = None  # Initialize answer variable to avoid reference before assignment
if submit and user_query:
    try:
        with st.spinner("🤖 Thinking..."):
            answer = ask(user_query)
        st.session_state.chat_history.append(("You", user_query))
        st.session_state.chat_history.append(("Bot", answer))
    except Exception as e:
        error_msg = f"⚠️ Error: {str(e)}"
        st.session_state.chat_history.append(("Bot", error_msg))
        answer = error_msg

# Styling
st.markdown("""
    <style>
    .chat-container {
        max-height: 500px;
        overflow-y: auto;
        padding: 10px;
        background-color: #fafafa;
        border: 1px solid #ddd;
        border-radius: 10px;
    }
    .chat-user {
        background-color: #DCF8C6;
        text-align: right;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    .chat-bot {
        background-color: #F1F0F0;
        padding: 10px;
        border-radius: 10px;
        margin-bottom: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Chat display
if st.session_state.chat_history:
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    st.markdown("### Chat History")

    for role, msg in st.session_state.chat_history:
        if role == "You":
            st.markdown(f"<div class='chat-user'><strong>🧑 You:</strong><br>{msg}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='chat-bot'><strong>🤖 Bot:</strong><br>{msg}</div>", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

