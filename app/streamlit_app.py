# ============================================================
# FILE: app/streamlit_app.py
# ============================================================

import sys
import os

import sys
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent

if str(ROOT_DIR) not in sys.path:

    sys.path.insert(0, str(ROOT_DIR))
    
import pandas as pd
import streamlit as st

from analytics.dashboard_renderer import render_dashboard
from ai_engine.gemini_client import ask_gemini

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Search Heist AI",
    page_icon="🎬",
    layout="wide"
)

# ============================================================
# CSS
# ============================================================

st.markdown(
    """
    <style>

    html,
    body,
    .stApp {

        background: #000000 !important;
        color: white !important;
    }

    header {

        visibility: hidden !important;
    }

    [data-testid="stHeader"] {

        display: none !important;
    }

    [data-testid="stToolbar"] {

        display: none !important;
    }

    .block-container {

        padding-top: 0rem !important;

        padding-left: 2rem !important;

        padding-right: 2rem !important;

        padding-bottom: 2rem !important;

        margin-top: -60px !important;

        max-width: 100% !important;
    }

    /* =====================================================
    FEATURE CARDS
    ===================================================== */

    .feature-card {

        background:
            linear-gradient(
                135deg,
                rgba(18,18,18,0.96),
                rgba(8,8,8,0.98)
            );

        padding: 22px;

        border-radius: 18px;

        text-align: center;

        color: white;

        border: 1px solid #222222;

        margin-bottom: 18px;

        font-weight: bold;

        font-size: 18px;
    }

    /* =====================================================
    FILE UPLOADER
    ===================================================== */

    [data-testid="stFileUploader"] {

        background: #111111 !important;

        border: 1px solid #222222 !important;

        border-radius: 18px !important;

        padding: 16px !important;
    }

    [data-testid="stFileUploader"] section {

        background: #111111 !important;
    }

    [data-testid="stFileUploader"] button {

        background: #1f1f1f !important;

        color: white !important;

        border: 1px solid #333333 !important;

        border-radius: 10px !important;
    }

    [data-testid="stFileUploader"] small {

        color: #bbbbbb !important;
    }

    /* =====================================================
    CHAT INPUT
    ===================================================== */

    [data-testid="stChatInput"] {

        background: #111111 !important;

        border: 2px solid #222222 !important;

        border-radius: 20px !important;

        padding: 10px !important;

        margin-top: 25px !important;
    }

    [data-testid="stChatInput"] textarea {

        background: white !important;

        color: black !important;

        -webkit-text-fill-color: black !important;

        font-weight: 600 !important;
    }

    /* =====================================================
    CHAT MESSAGE
    ===================================================== */

    div[data-testid="stChatMessage"] {

        background: #111111 !important;

        border: 1px solid #222222 !important;

        border-radius: 18px !important;

        padding: 16px !important;

        margin-bottom: 15px !important;
    }

    div[data-testid="stChatMessage"] * {

        color: white !important;
    }

    /* =====================================================
    METRICS
    ===================================================== */

    [data-testid="metric-container"] {

        background: #111111 !important;

        border: 1px solid #222222 !important;

        border-radius: 18px !important;

        padding: 18px !important;
    }

    [data-testid="metric-container"] * {

        color: white !important;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ============================================================
# HERO SECTION
# ============================================================

hero_html = "<div style='background:linear-gradient(135deg,#7a0000,#2b0000);padding:45px;border-radius:24px;margin-bottom:30px;box-shadow:0 0 30px rgba(229,9,20,0.25);'><div style='color:#ff2a2a;font-size:72px;font-weight:900;'>SEARCH HEIST AI</div><div style='color:white;font-size:24px;margin-top:18px;'>AI-Powered Marketing Intelligence & Search Analytics</div></div>"

st.markdown(
    hero_html,
    unsafe_allow_html=True
)

# ============================================================
# FEATURES
# ============================================================

c1, c2, c3 = st.columns(3)

with c1:

    st.markdown(
        "<div class='feature-card'>📉 ROAS Decline Detection</div>",
        unsafe_allow_html=True
    )

with c2:

    st.markdown(
        "<div class='feature-card'>💰 Spend Optimization</div>",
        unsafe_allow_html=True
    )

with c3:

    st.markdown(
        "<div class='feature-card'>🚨 Anomaly Detection</div>",
        unsafe_allow_html=True
    )

c4, c5, c6 = st.columns(3)

with c4:

    st.markdown(
        "<div class='feature-card'>📊 Executive Summaries</div>",
        unsafe_allow_html=True
    )

with c5:

    st.markdown(
        "<div class='feature-card'>🔍 Search Merchandising</div>",
        unsafe_allow_html=True
    )

with c6:

    st.markdown(
        "<div class='feature-card'>🧠 AI Recommendations</div>",
        unsafe_allow_html=True
    )

# ============================================================
# UPLOAD SECTION
# ============================================================

upload_html = "<div style='background:#111111;padding:22px;border-radius:20px;border:1px solid #222222;margin-top:20px;margin-bottom:20px;'><h3 style='color:white;margin-top:0;'>📂 Upload Dataset</h3><p style='color:#aaaaaa;'>Upload CSV or Excel file and let AI agents analyze performance.</p></div>"

st.markdown(
    upload_html,
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "",
    type=["csv", "xlsx"],
    label_visibility="collapsed"
)

# ============================================================
# LOAD DATA
# ============================================================

df = None

if uploaded_file is not None:

    try:

        if uploaded_file.name.endswith(".csv"):

            df = pd.read_csv(uploaded_file)

        else:

            df = pd.read_excel(uploaded_file)

        st.success(
            "Dataset Loaded Successfully"
        )

        # ====================================================
        # AI DASHBOARD
        # ====================================================

        render_dashboard(df)

    except Exception as e:

        st.error(str(e))

# ============================================================
# CHAT HISTORY
# ============================================================

if "messages" not in st.session_state:

    st.session_state.messages = []

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])

# ============================================================
# CHAT INPUT
# ============================================================

prompt = st.chat_input(
    "Ask The Professor about campaign intelligence..."
)

# ============================================================
# AI CHAT RESPONSE
# ============================================================

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):

        st.markdown(prompt)

    if df is not None:

        dataset_context = f"""

        Dataset Columns:
        {list(df.columns)}

        Sample Data:
        {df.head(10).to_string()}

        """

        final_prompt = f"""

        You are Search Heist AI,
        an expert marketing analytics assistant.

        Analyze the uploaded dataset and answer the question.

        USER QUESTION:
        {prompt}

        DATASET:
        {dataset_context}

        Give:
        - direct answer
        - reasoning
        - business insights
        - recommendations
        """

        try:

            response = ask_gemini(
                final_prompt
            )

        except Exception as e:

            response = f"Gemini Error: {str(e)}"

    else:

        response = "Please upload dataset first."

    with st.chat_message("assistant"):

        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )