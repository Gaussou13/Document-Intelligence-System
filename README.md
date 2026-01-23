📄 Document Intelligence

Minimal PDF Question Answering System

Document Intelligence is a clean, local-first PDF question answering system that allows users to upload documents, index their contents, and ask natural language questions to retrieve accurate, source-backed answers.

Built using LlamaIndex, HuggingFace open-source models, and Streamlit, the project emphasizes clarity, simplicity, and performance, paired with a minimal black-and-white editorial UI.

🔍 Core Topics Covered

Document Intelligence

Retrieval-Augmented Generation (RAG)

PDF Parsing & Text Extraction

Vector Embeddings & Semantic Search

LLM-powered Question Answering

Minimal UI/UX Design for AI Applications

Local-first AI Systems (No Paid APIs)

✨ Key Features

📂 Upload multiple PDF documents

🧠 Semantic indexing using vector embeddings

🔎 Ask natural language questions across documents

📄 Page-level context retrieval

⚡ Fast local inference (no external API dependency)

🎨 Minimal black & white editorial UI

🛡️ Fully offline-capable after setup

🧱 Architecture Overview
User
 ↓
Streamlit UI
 ↓
Query Engine (LlamaIndex)
 ↓
Vector Store (Local)
 ↓
PDF Content + Metadata

🛠️ Tech Stack
Frontend

Streamlit

Custom CSS (Minimal Black & White UI)

Backend

Python 3.10+

LlamaIndex

HuggingFace Transformers

Sentence Transformers (Embeddings)

Storage

Local Vector Store (LlamaIndex SimpleVectorStore)

Persistent Index Storage

Document Processing

PyPDF / PDF Reader utilities

📁 Project Structure
document-intelligence/
│
├── app.py                # Streamlit UI
├── ingest.py             # PDF loading & indexing
├── query.py              # Query engine logic
├── data/
│   ├── uploads/          # Uploaded PDFs
│   └── storage/          # Persisted index
├── requirements.txt
└── README.md

📖 How It Works

Upload one or more PDF documents

The system extracts and chunks text

Embeddings are generated and stored locally

A semantic index is built and persisted

User questions are matched against relevant chunks

The LLM generates an answer using retrieved context

🧠 Example Questions

“Explain data mining concepts discussed in page 1.”

“What are the advantages of clustering algorithms?”

“Summarize the introduction section.”

🎨 UI Philosophy

Black & white only

No visual noise

Typography-focused layout

Content-first interaction

Editorial / studio-inspired aesthetic

The interface is designed to disappear — letting documents speak.

🔐 Privacy & Cost

❌ No OpenAI / paid APIs

✅ Runs fully on local machine

✅ Documents never leave your system

📌 Use Cases

Study notes & textbooks

Research papers

Exam preparation

Technical documentation

Personal knowledge bases
