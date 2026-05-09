# =========================================================
# FILE: app/streamlit_app.py
# =========================================================

import os
import re
import sys
import streamlit as st
import pandas as pd

# =========================================================
# ROOT PATH
# =========================================================

ROOT_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

sys.path.append(ROOT_DIR)

# =========================================================
# IMPORT GEMINI
# =========================================================

from utils.gemini_helper import ask_gemini

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Search Heist AI",
    page_icon="🎭",
    layout="wide"
)

# =========================================================
# LOAD CSS
# =========================================================

css_path = os.path.join(
    ROOT_DIR,
    "assets",
    "custom.css"
)

with open(css_path) as f:

    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

# =========================================================
# SESSION STATE
# =========================================================

if "messages" not in st.session_state:

    st.session_state.messages = [

        {
            "role": "assistant",
            "content": """
🎭 Welcome to Search Heist AI.

I can help you:

• Analyze ROAS decline

• Detect inefficient spend

• Identify weak-performing campaigns

• Generate executive summaries

• Detect anomalies automatically

• Recommend optimization opportunities

• Create SQL queries

• Visualize campaign intelligence

Upload your dataset and ask anything.
"""
        }

    ]

if "df" not in st.session_state:
    st.session_state.df = None

# =========================================================
# CLEAN TEXT FUNCTION
# =========================================================

def clean_ai_response(text):

    text = str(text)

    # REMOVE HTML TAGS COMPLETELY
    text = re.sub(r"<.*?>", "", text)

    # REMOVE BAD STRINGS
    bad_items = [
        "</div>",
        "<div>",
        "```",
        "html",
        "css",
        "javascript"
    ]

    for item in bad_items:

        text = text.replace(item, "")

    # REMOVE EXTRA SPACES
    text = re.sub(r"\n\s*\n", "\n", text)

    return text.strip()

# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    logo_path = os.path.join(
        ROOT_DIR,
        "assets",
        "logo.png"
    )

    st.image(
        logo_path,
        width=80
    )

    st.markdown("## Mission Control")

    st.divider()

    st.markdown(
        "### Upload Intelligence Dataset"
    )

    uploaded_file = st.file_uploader(
        "Upload CSV or Excel File",
        type=["csv", "xlsx"]
    )

    # =====================================================
    # LOAD DATASET
    # =====================================================

    if uploaded_file is not None:

        try:

            # CSV
            if uploaded_file.name.endswith(".csv"):

                df = pd.read_csv(uploaded_file)

            # XLSX
            else:

                df = pd.read_excel(uploaded_file)

            st.session_state.df = df

            st.markdown(
                """
                <div class="upload-success-box">
                    Dataset Uploaded Successfully
                </div>
                """,
                unsafe_allow_html=True
            )

        except Exception as e:

            st.error(str(e))

# =========================================================
# HEADER
# =========================================================

col1, col2 = st.columns([1, 10])

with col1:

    st.image(
        logo_path,
        width=70
    )

with col2:

    st.markdown(
        """
        <h1 class="main-title">
            SEARCH HEIST AI
        </h1>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <p class="subtitle">
            AI-Powered Marketing Intelligence Command Center
        </p>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# CHAT HISTORY
# =========================================================

for msg in st.session_state.messages:

    # =====================================================
    # USER MESSAGE
    # =====================================================

    if msg["role"] == "user":

        st.markdown(
            f"""
            <div class="user-message">
                <div class="user-bubble">
                    🎭 {msg["content"]}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # =====================================================
    # AI MESSAGE
    # =====================================================

    else:

        clean_content = clean_ai_response(
            msg["content"]
        )

        st.markdown(
            f"""
            <div class="ai-message">
                <div class="ai-bubble">
                    <div class="ai-content">
                        {clean_content}
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# =========================================================
# CHAT INPUT
# =========================================================

prompt = st.chat_input(
    "Ask The Professor about campaign intelligence..."
)

# =========================================================
# USER QUESTION
# =========================================================

if prompt:

    # SAVE USER MESSAGE
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # =====================================================
    # AI RESPONSE
    # =====================================================

    with st.spinner(
        "🎭 The Professor is thinking..."
    ):

        try:

            ai_response = ask_gemini(
                prompt,
                st.session_state.df
            )

            ai_response = clean_ai_response(
                ai_response
            )

        except Exception as e:

            ai_response = f"""
🎭 The Professor encountered an issue.

{str(e)}
"""

    # SAVE AI MESSAGE
    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_response
    })

    st.rerun()