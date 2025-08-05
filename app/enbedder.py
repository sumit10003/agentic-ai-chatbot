import os
from dotenv import load_dotenv
from typing import List
from openai import OpenAI
import tiktoken

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

# Simple text splitter
def split_text(text: str, chunk_size: int = 300, overlap: int = 50) -> List[str]:
    tokens = text.split()
    chunks = []
    for i in range(0, len(tokens), chunk_size - overlap):
        chunk = " ".join(tokens[i:i + chunk_size])
        chunks.append(chunk)
    return chunks

# Embed text chunks
def embed_text_chunks(chunks: List[str]) -> List[List[float]]:
    embeddings = []
    for chunk in chunks:
        response = client.embeddings.create(
            input=chunk,
            model="text-embedding-3-small"  # You can also try text-embedding-ada-002
        )
        embeddings.append(response.data[0].embedding)
    return embeddings
