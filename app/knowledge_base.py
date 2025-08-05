import requests
from bs4 import BeautifulSoup
from embedder import split_text, embed_text_chunks

# Get all text from a single web page
def get_text_from_url(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Remove script and style tags
    for script in soup(["script", "style", "noscript"]):
        script.decompose()

    text = soup.get_text(separator=" ")
    return text.strip()

# Build knowledge base from a list of URLs
def build_knowledge_base(urls):
    knowledge_chunks = []
    embeddings = []

    for url in urls:
        print(f"[+] Processing {url}")
        raw_text = get_text_from_url(url)
        chunks = split_text(raw_text)
        chunk_embeddings = embed_text_chunks(chunks)

        knowledge_chunks.extend(chunks)
        embeddings.extend(chunk_embeddings)

    return knowledge_chunks, embeddings