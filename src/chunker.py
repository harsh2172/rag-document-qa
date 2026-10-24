from loader import load_pdf


def chunk_pages(pages, chunk_size=1000, overlap=200):
    chunks = []
    for p in pages:
        text = p["text"]
        start = 0
        while start < len(text):
            piece = text[start:start + chunk_size]
            chunks.append({"page": p["page"], "text": piece})
            start += chunk_size - overlap
    return chunks


if __name__ == "__main__":
    pages = load_pdf("data/jio_rhp.pdf", start=0, end=30)
    chunks = chunk_pages(pages)
    print(f"Total chunks: {len(chunks)}")
    print(chunks[10])