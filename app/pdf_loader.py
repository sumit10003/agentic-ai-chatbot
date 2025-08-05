from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List
from langchain.schema import Document

from embedder import get_embedder  # Assuming you have this in embedder.py

def load_pdf_documents(pdf_paths: List[str]) -> List[Document]:
    """Load and split PDF documents into chunks."""
    all_docs = []
    for path in pdf_paths:
        loader = PyPDFLoader(path)
        docs = loader.load()
        all_docs.extend(docs)
    return all_docs

def split_documents(documents: List[Document], chunk_size: int = 1000, chunk_overlap: int = 200) -> List[Document]:
    """Split documents into smaller chunks for embedding."""
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.split_documents(documents)

def embed_pdf_documents(pdf_paths: List[str]):
    """Load, split, and embed PDF documents."""
    documents = load_pdf_documents(pdf_paths)
    split_docs = split_documents(documents)
    embedder = get_embedder()
    embeddings = embedder.embed_documents([doc.page_content for doc in split_docs])
    return embeddings, split_docs