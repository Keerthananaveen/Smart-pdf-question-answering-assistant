from langchain_core.prompts import ChatPromptTemplate
prompt = ChatPromptTemplate.from_template(
"""
You are an intelligent PDF Question Answering Assistant.

Answer ONLY using the provided context.

If the answer is not found in the context, say:

"I couldn't find the answer in the uploaded PDF."
Context:
{context}

Question:
{input}

Answer:
"""
)