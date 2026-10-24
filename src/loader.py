from pypdf import PdfReader


def load_pdf(path, start=0, end=None):
    reader = PdfReader(path)
    pages = []
    for i, page in enumerate(reader.pages[start:end], start=start + 1):
        text = page.extract_text() or ""
        if text.strip():
            pages.append({"page": i, "text": text})
    return pages


if __name__ == "__main__":
    pages = load_pdf("data/jio_rhp.pdf", start=0, end=30)
    print(f"Pages loaded: {len(pages)}")
    print(pages[5]["page"], pages[5]["text"][:300])