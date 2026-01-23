import os
import pickle
from pypdf import PdfReader
from sentence_transformers import SentenceTransformer
import faiss

UPLOAD_DIR = "data/uploads"
STORAGE_DIR = "storage"
os.makedirs(STORAGE_DIR, exist_ok=True)

EMBED_MODEL = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def load_pdfs():
    docs = []
    for filename in os.listdir(UPLOAD_DIR):
        if filename.endswith(".pdf"):
            path = os.path.join(UPLOAD_DIR, filename)
            pdf = PdfReader(path)
            for i, page in enumerate(pdf.pages):
                text = page.extract_text()
                if text:
                    docs.append({
                        "text": text,
                        "page": i+1,
                        "filename": filename
                    })
    return docs

def build_index(docs):
    embeddings = EMBED_MODEL.encode([d["text"] for d in docs], convert_to_numpy=True)
    dim = embeddings.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(embeddings)
    return index

def save_index(index, docs):
    faiss.write_index(index, os.path.join(STORAGE_DIR, "faiss.index"))
    with open(os.path.join(STORAGE_DIR, "docs.pkl"), "wb") as f:
        pickle.dump(docs, f)

if __name__ == "__main__":
    docs = load_pdfs()
    index = build_index(docs)
    save_index(index, docs)
    print("FAISS index and documents saved successfully.")
