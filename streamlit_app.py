import streamlit as st
from modules.rag_pipeline import PDFQuestionAnsweringAssistant

st.set_page_config(
    page_title="Smart PDF Question Answering Assistant",
    page_icon="📄",
    layout="wide"
)

st.title("📄 Smart PDF Question Answering Assistant")
st.write("Upload a PDF and ask questions about its content.")

@st.cache_resource
def load_default_assistant():
    try:
        return PDFQuestionAnsweringAssistant.from_local_index()
    except Exception:
        return None

@st.cache_resource
def build_assistant_from_pdf(file_bytes):
    return PDFQuestionAnsweringAssistant.from_pdf(file_bytes=file_bytes, save_local=False)

uploaded_file = st.sidebar.file_uploader("Upload a PDF file", type=["pdf"])
assistant = None

if uploaded_file is not None:
    st.sidebar.write(f"Selected file: {uploaded_file.name}")
    with st.spinner("Indexing uploaded PDF..."):
        assistant = build_assistant_from_pdf(uploaded_file.read())
        st.sidebar.success("PDF uploaded and indexed.")
else:
    assistant = load_default_assistant()
    if assistant is not None:
        st.sidebar.success("Loaded the local indexed PDF database.")
    else:
        st.sidebar.info("No local vector index found. Upload a PDF to begin.")

if assistant is None:
    st.warning("Please upload a PDF file to use the assistant.")
else:
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    question = st.chat_input("Ask something about the PDF...")

    if question:
        st.session_state.messages.append({"role": "user", "content": question})

        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                answer = assistant.ask(question)
                st.markdown(answer)

        st.session_state.messages.append({"role": "assistant", "content": answer})