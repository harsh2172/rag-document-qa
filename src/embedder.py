from dotenv import load_dotenv
from google import genai
from loader import load_pdf 
from chunker import chunk_pages

load_dotenv()
client = genai.Client()

def embed_texts(texts, model="gemini-embedding-001"):
    result = client.models.embed_content(model=model, contents=texts)
    return [e.values for e in result.embeddings]

if __name__ == "__main__":
    pages = load_pdf("data/jio_rhp.pdf", start=0, end=30)
    chunks = chunk_pages(pages)
    vectors = embed_texts([c["text"] for c in chunks[:5]])
    print(f"Vectors: {len(vectors)}, numbers per vector: {len(vectors[0])}")
    print(vectors[0][:5])

