import streamlit as st
from modules.rag_pipeline import PDFQuestionAnsweringAssistant

st.set_page_config(
    page_title="Smart PDF Question Answering Assistant",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Smart PDF Question Answering Assistant")

st.write("Ask questions about your PDF document.")

@st.cache_resource
def load_assistant():
    return PDFQuestionAnsweringAssistant()

assistant = load_assistant()

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
question = st.chat_input("Ask something about the PDF...")

if question:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            answer = assistant.ask(question)

            st.markdown(answer)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )