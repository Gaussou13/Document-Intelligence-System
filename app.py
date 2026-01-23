import streamlit as st
import os
from ingest import build_index, load_pdfs, save_index
from query import ask_question

# --- Setup directories ---
UPLOAD_DIR = "data/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# --- Page config ---
st.set_page_config(
    page_title="Document Intelligence",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Global CSS (Tight Top Alignment) ---
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400&family=Playfair+Display:wght@400&display=swap');

    /* ---------- Reset spacing ---------- */
    html, body {
        margin: 0;
        padding: 0;
        height: 100%;
        overflow: hidden;
    }

    .stApp {
        background-color: #0b0b0b;
        color: #f2f2ee;
        font-family: 'Inter', sans-serif;
        height: 100vh;
        overflow: hidden;
    }

    /* Remove Streamlit padding */
    .block-container {
        padding-top: 12px !important;
        padding-bottom: 0px !important;
    }

    #MainMenu, footer, header {
        visibility: hidden;
    }

    /* ---------- Sidebar ---------- */
    section[data-testid="stSidebar"] {
        background-color: #0d0d0d;
        border-right: 1px solid rgba(255,255,255,0.05);
    }

    section[data-testid="stSidebar"] * {
        color: rgba(255,255,255,0.55);
        font-size: 13px;
    }

    /* ---------- Hero ---------- */
    .hero {
        padding-left: 120px;
        padding-top: 20px; /* 🔑 key fix */
        max-width: 900px;
    }

    .hero h1 {
        font-family: 'Playfair Display', serif;
        font-size: 104px;
        font-weight: 400;
        line-height: 1.05;
        margin: 0;
    }

    .hero .sub {
        margin-top: 20px;
        font-family: 'Playfair Display', serif;
        font-style: italic;
        font-size: 36px;
        line-height: 1.2;
        color: rgba(242,242,238,0.45);
    }

    /* ---------- Input ---------- */
    .input-wrap {
        margin-top: 32px;
        max-width: 520px;
    }

    .stTextInput > div > div > input {
        background: transparent;
        border: none;
        border-bottom: 1px solid rgba(255,255,255,0.3);
        border-radius: 0;
        padding: 12px 4px;
        font-size: 14px;
        color: #f2f2ee;
    }

    /* ---------- Button ---------- */
    .stButton > button {
        margin-top: 16px;
        background: transparent;
        border: 1px solid rgba(255,255,255,0.3);
        color: #f2f2ee;
        padding: 10px 30px;
        border-radius: 40px;
        font-size: 12px;
        letter-spacing: 1px;
    }

    /* ---------- Results ---------- */
    .card {
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.06);
        border-radius: 14px;
        padding: 18px 20px;
        margin-top: 14px;
        font-size: 13px;
        line-height: 1.6;
        color: rgba(242,242,238,0.85);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Sidebar ---
st.sidebar.title("Document Intelligence")
st.sidebar.markdown(
    "Upload PDFs or notes, ask questions, and get answers with page numbers and file references."
)

uploaded_files = st.sidebar.file_uploader(
    "Upload PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

top_k = st.sidebar.slider("Top results", 1, 10, 3)

# --- Handle uploads ---
if uploaded_files:
    for file in uploaded_files:
        path = os.path.join(UPLOAD_DIR, file.name)
        with open(path, "wb") as f:
            f.write(file.read())

    docs = load_pdfs()
    index = build_index(docs)
    save_index(index, docs)
    st.sidebar.success(f"Indexed {len(docs)} pages successfully!")

# --- Hero ---
st.markdown(
    """
    <div class="hero">
        <h1>Document<br>Intelligence</h1>
        <div class="sub">
            Ask questions about your PDFs<br>
            and get precise answers
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# --- Query ---
st.markdown('<div class="input-wrap">', unsafe_allow_html=True)

question = st.text_input("Type your question here")

if st.button("Get Answer") and question:
    with st.spinner("Fetching answers..."):
        response = ask_question(question, top_k=top_k)
        snippets = response.split("\n\n")

        for snip in snippets:
            st.markdown(
                f"<div class='card'>{snip}</div>",
                unsafe_allow_html=True
            )

st.markdown('</div>', unsafe_allow_html=True)
