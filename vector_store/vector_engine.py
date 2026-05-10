from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_community.vectorstores import FAISS

from langchain_google_genai import GoogleGenerativeAIEmbeddings

# ============================================================
# SPLITTER
# ============================================================

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

# ============================================================
# VECTOR STORE
# ============================================================

def create_vector_store(text):

    chunks = splitter.split_text(text)

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001"
    )

    vector_db = FAISS.from_texts(
        chunks,
        embedding=embeddings
    )

    return vector_db