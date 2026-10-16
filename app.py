
import os
import streamlit as st
from groq import Groq
from pypdf import PdfReader

# ---------------- PAGE SETTINGS ----------------

st.set_page_config(
    page_title="My AI Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 My AI Assistant")
st.caption("Powered by Groq AI")

# ---------------- API KEY ----------------

try:
    api_key = st.secrets.get("GROQ_API_KEY")
except Exception:
    api_key = None

api_key = api_key or os.getenv("GROQ_API_KEY")

if not api_key:
    st.error(
        "Groq API key not found. "
        "Please set GROQ_API_KEY in your environment."
    )
    st.stop()

client = Groq(api_key=api_key)

# ---------------- SESSION MEMORY ----------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = ""

# ---------------- SIDEBAR ----------------

with st.sidebar:
    st.header("⚙️ Settings")

    if st.button("🗑️ Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.subheader("📄 Upload PDF")

    uploaded_file = st.file_uploader(
        "Choose a PDF file",
        type=["pdf"]
    )

    if uploaded_file is not None:
        try:
            reader = PdfReader(uploaded_file)

            text = "\n".join(
                page.extract_text() or ""
                for page in reader.pages
            )

            st.session_state.pdf_text = text

            st.success("PDF uploaded successfully!")
            st.caption(f"Extracted {len(text)} characters")

        except Exception as error:
            st.error(f"Could not read PDF: {error}")

    if st.button("Remove PDF"):
        st.session_state.pdf_text = ""
        st.rerun()

# ---------------- DISPLAY CHAT HISTORY ----------------

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------- USER INPUT ----------------

user_input = st.chat_input(
    "Ask me anything or ask about your PDF..."
)

if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # ---------------- SYSTEM INSTRUCTIONS ----------------

    pdf_text = st.session_state.pdf_text

    if pdf_text:
        context = (
            "You are a helpful AI assistant. Answer questions "
            "about the uploaded PDF using its content when relevant. "
            "If the answer is not in the document, say so clearly.\n\n"
            "DOCUMENT CONTENT:\n" + pdf_text[:30000]
        )
    else:
        context = (
            "You are a helpful AI assistant. "
            "Answer clearly and accurately."
        )

    # Groq accepts user and assistant roles
    history = [
        {"role": "system", "content": context}
    ]

    for message in st.session_state.messages[-12:]:
        history.append({
            "role": (
                "assistant"
                if message["role"] == "assistant"
                else "user"
            ),
            "content": message["content"]
        })

    # ---------------- GROQ RESPONSE ----------------

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="openai/gpt-oss-20b",
                    messages=history,
                    temperature=0.7,
                    max_tokens=1024
                )

                answer = (
                    response.choices[0].message.content
                    or "Sorry, I couldn't generate a response."
                )

                st.markdown(answer)

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer
                })

            except Exception as error:
                st.error("Could not generate a response.")
                st.caption(str(error))

