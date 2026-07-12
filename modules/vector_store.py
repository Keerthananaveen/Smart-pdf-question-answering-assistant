from langchain_community.vectorstores import FAISS
from modules.embeddings import get_embeddings
DB_PATH = "database/faiss_index"
def create_vector_store(chunks):
    embeddings = get_embeddings()

    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    vector_store.save_local(DB_PATH)

    print("Vector Store Created Successfully!")

    return vector_store
def load_vector_store():
    embeddings = get_embeddings()

    vector_store = FAISS.load_local(
        DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vector_store