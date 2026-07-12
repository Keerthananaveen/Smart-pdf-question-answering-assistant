from modules.rag_pipeline import PDFQuestionAnsweringAssistant
assistant = PDFQuestionAnsweringAssistant()
print("=" * 60)
print("Smart PDF Question Answering Assistant")
print("=" * 60)
while True:
    question = input("\nAsk a question (type 'exit' to quit): ")
    if question.lower() == "exit":
        break
    answer = assistant.ask(question)
    print("\nAnswer:\n")
    print(answer)