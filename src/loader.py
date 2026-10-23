from pypdf import PdfReader


def load_pdf(path, start=0, end=None):
    reader = PdfReader(path)
    pages = reader.pages[start:end]
    text = ""
    for page in pages:
        text += (page.extract_text() or "") + "\n"
    return text


if __name__ == "__main__":
    text = load_pdf("data/jio_rhp.pdf", start=0, end=30)
    print(f"Characters extracted: {len(text)}")
    print(text[:500])
    
