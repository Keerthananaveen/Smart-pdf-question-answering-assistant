from modules.vector_store import load_vector_store
from modules.llm import get_llm
from modules.prompts import prompt
class PDFQuestionAnsweringAssistant:

    def __init__(self):
        self.vector_store = load_vector_store()
        self.retriever = self.vector_store.as_retriever(
            search_kwargs={"k": 3}
        )
        self.llm = get_llm()

    def ask(self, question):

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
        content=response.content
        if isinstance(content, str):
            return content
        if isinstance(content, list):
            answer=""
            for item in content:
                if isinstance(item, dict):
                    if item.get("type") == "text":
                         answer += item.get("text", "")
            return answer.strip()
        return str(content)