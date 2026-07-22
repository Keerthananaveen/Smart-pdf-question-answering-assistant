from modules.vector_store import create_vector_store, load_vector_store
from modules.llm import get_llm
from modules.prompts import prompt

class PDFQuestionAnsweringAssistant:

    def __init__(self, vector_store):
        self.vector_store = vector_store
        self.retriever = self.vector_store.as_retriever(
            search_kwargs={"k": 3}
        )
        self.llm = get_llm()

    @classmethod
    def from_local_index(cls):
        vector_store = load_vector_store()
        return cls(vector_store)

    @classmethod
    def from_pdf(cls, file_path=None, file_bytes=None, save_local=False):
        from modules.pdf_loader import load_pdf
        from modules.text_splitter import split_documents

        documents = load_pdf(file_path=file_path, file_bytes=file_bytes)
        chunks = split_documents(documents)
        vector_store = create_vector_store(chunks, save_local=save_local)
        return cls(vector_store)

    def ask(self, question):
        if hasattr(self.retriever, "get_relevant_documents"):
            docs = self.retriever.get_relevant_documents(question)
        else:
            docs = self.retriever.invoke(question)

        context = "\n\n".join(
            doc.page_content for doc in docs
        )

        messages = prompt.invoke(
            {
                "context": context,
                "input": question
            }
        )

        response = self.llm.invoke(messages)
        content = response.content
        if isinstance(content, str):
            return content
        if isinstance(content, list):
            answer = ""
            for item in content:
                if isinstance(item, dict):
                    if item.get("type") == "text":
                        answer += item.get("text", "")
            return answer.strip()
        return str(content)