import os
import pickle
import faiss
from sentence_transformers import SentenceTransformer
import numpy as np

STORAGE_DIR = "storage"
EMBED_MODEL = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def load_index():
    index = faiss.read_index(os.path.join(STORAGE_DIR, "faiss.index"))
    with open(os.path.join(STORAGE_DIR, "docs.pkl"), "rb") as f:
        docs = pickle.load(f)
    return index, docs

def ask_question(question, top_k=3):
    index, docs = load_index()
    q_vec = EMBED_MODEL.encode([question], convert_to_numpy=True)
    D, I = index.search(q_vec, top_k)
    results = []
    for idx in I[0]:
        doc = docs[idx]
        results.append(f"{doc['text']} (File: {doc['filename']}, Page: {doc['page']})")
    return "\n\n".join(results)
