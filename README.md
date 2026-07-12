# Smart PDF Question Answering Assistant

A Retrieval-Augmented Generation (RAG) application built with Python, LangChain, FAISS, HuggingFace Embeddings, and Google Gemini.

The application reads a PDF document, creates vector embeddings, stores them in a FAISS vector database, and answers user questions using the contents of the document.

---

## Features

- Load PDF documents
- Split text into chunks
- Generate embeddings using HuggingFace
- Store embeddings in FAISS
- Retrieve relevant context
- Answer questions using Google Gemini
- Command-line interface

---

## Tech Stack

- Python
- LangChain
- Google Gemini API
- HuggingFace Embeddings
- FAISS
- PyPDF
- dotenv

---

## Project Structure

```
smart-pdf-assistant/
│
├── app.py
├── requirements.txt
├── .env
│
├── data/
│   └── book.pdf
│
├── faiss_index/
│
└── modules/
    ├── llm.py
    ├── embeddings.py
    ├── loader.py
    ├── vector_store.py
    ├── rag_pipeline.py
    ├── prompts.py
    └── helper.py
```

---

## Installation

Clone the repository.

```bash
git clone <repository-url>
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate the environment.

Windows

```bash
venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file.

```
GOOGLE_API_KEY=your_google_api_key
```

---

## Build the Vector Database

Run the indexing script.

```bash
python create_vector_db.py
```

---

## Run the Application

```bash
python app.py
```

Example:

```
Ask a question:

What is Python?

Answer:

Python is a general-purpose programming language with simple syntax...
```

---

## Workflow

```
PDF
   ↓
Load Document
   ↓
Split into Chunks
   ↓
Generate Embeddings
   ↓
Store in FAISS
   ↓
Retrieve Relevant Chunks
   ↓
Gemini
   ↓
Answer
```

---

## Future Improvements

- Upload any PDF from the UI
- Streamlit interface
- Chat history
- Multiple PDF support
- Source citations
- Conversation memory

---
