import os
import tempfile
from langchain_community.document_loaders import PyPDFLoader
def load_pdf(file_path=None, file_bytes=None):
    """
    Load a PDF file and return LangChain Document objects.

    Either file_path or file_bytes must be provided.
    """
    if file_path:
        loader = PyPDFLoader(file_path)
        return loader.load()

    if file_bytes is not None:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(file_bytes)
            temp_path = tmp_file.name

        try:
            loader = PyPDFLoader(temp_path)
            return loader.load()
        finally:
            try:
                os.remove(temp_path)
            except OSError:
                pass

    raise ValueError("Either file_path or file_bytes must be provided.")