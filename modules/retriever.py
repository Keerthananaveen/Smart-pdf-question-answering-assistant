from modules.vector_store import load_vector_store
def get_retriever():
    """
    Load the FAISS database and return a retriever.
    """

    vector_store = load_vector_store()

    retriever = vector_store.as_retriever(
        search_kwargs={"k": 3}
    )

    return retriever