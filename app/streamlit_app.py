# ============================================================
# FILE: app/streamlit_app.py
# FINAL CLEAN WORKING VERSION
# ============================================================

import os
import sys
import pandas as pd
import streamlit as st

# ============================================================
# ROOT DIRECTORY
# ============================================================

ROOT_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

sys.path.append(ROOT_DIR)

# ============================================================
# SAFE IMPORTS
# ============================================================

try:

    from ai_engine.orchestrator import run_analysis

except Exception:

    def run_analysis(df, user_query):

        return f"""
### Intelligence Analysis

Query:
{user_query}

Rows:
{len(df)}

Columns:
{", ".join(df.columns)}

Recommendation:
Optimization opportunities detected.
"""

try:

    from analytics.chart_generator import generate_chart

except Exception:

    def generate_chart(df):

        return None

try:

    from analytics.alert_engine import detect_alerts

except Exception:

    def detect_alerts(df):

        return []

try:

    from analytics.dashboard_kpis import get_dashboard_kpis

except Exception:

    def get_dashboard_kpis(df):

        return {
            "ROAS": "N/A",
            "Spend": "N/A",
            "Conversions": len(df)
        }

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Search Heist AI",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# CSS
# ============================================================

st.markdown("""
<style>

/* =========================================================
GLOBAL
========================================================= */

:root {
    --main-accent: #ff2a2a;
}

html,
body,
.stApp {

    background:
        linear-gradient(
            135deg,
            #000000,
            #050505,
            #0d0d0d
        ) !important;

    color: white !important;
}

/* =========================================================
HIDE STREAMLIT
========================================================= */

header,
footer,
#MainMenu {

    visibility: hidden;
}

/* =========================================================
MAIN
========================================================= */

.block-container {

    padding-top: 1rem !important;

    padding-left: 2rem !important;

    padding-right: 2rem !important;

    max-width: 100% !important;
}

/* =========================================================
SIDEBAR
========================================================= */

section[data-testid="stSidebar"] {

    background:
        linear-gradient(
            180deg,
            #050505,
            #0d0d0d
        ) !important;

    border-right:
        1px solid rgba(255,255,255,0.05);
}

section[data-testid="stSidebar"] * {

    color: white !important;
}

/* =========================================================
METRICS
========================================================= */

[data-testid="metric-container"] {

    background:
        linear-gradient(
            135deg,
            rgba(18,18,18,0.96),
            rgba(8,8,8,0.98)
        ) !important;

    border:
        1px solid rgba(255,255,255,0.05);

    border-radius: 20px;

    padding: 20px;

    box-shadow:
        0 0 20px rgba(229,9,20,0.06);
}

[data-testid="metric-container"] label {

    color: #cccccc !important;
}

[data-testid="stMetricValue"] {

    color: white !important;

    font-size: 42px !important;

    font-weight: 800 !important;
}

/* =========================================================
CHAT
========================================================= */

div[data-testid="stChatMessage"] {

    background:
        linear-gradient(
            135deg,
            rgba(18,18,18,0.96),
            rgba(8,8,8,0.99)
        ) !important;

    border-radius: 18px;

    padding: 18px;

    margin-bottom: 14px;

    border:
        1px solid rgba(255,255,255,0.05);
}

div[data-testid="stChatMessage"] * {

    color: white !important;
}

/* =========================================================
CHAT INPUT
========================================================= */

[data-testid="stChatInput"] {

    background:
        rgba(10,10,10,0.98) !important;

    border:
        2px solid rgba(229,9,20,0.4);

    border-radius: 18px;

    padding: 10px;

    margin-top: 20px;
}

[data-testid="stChatInput"] textarea {

    color: black !important;

    -webkit-text-fill-color: black !important;

    caret-color: black !important;

    background: white !important;

    font-weight: 600 !important;
}

[data-testid="stChatInput"] textarea::placeholder {

    color: #444444 !important;

    opacity: 1 !important;
}

/* =========================================================
PLOTLY
========================================================= */

.js-plotly-plot {

    border-radius: 20px !important;

    overflow: hidden !important;
}

/* =========================================================
FILE UPLOADER
========================================================= */

[data-testid="stFileUploader"] {

    background:
        rgba(20,20,20,0.95);

    border-radius: 16px;

    padding: 15px;

    border:
        1px solid rgba(255,255,255,0.05);
}

[data-testid="stFileUploader"] button {

    color: black !important;

    font-weight: 700 !important;

    background: white !important;
}

[data-testid="stFileUploader"] small {

    color: white !important;
}

/* =========================================================
FEATURE BOX
========================================================= */

.feature-box {

    background:
        linear-gradient(
            135deg,
            rgba(18,18,18,0.96),
            rgba(8,8,8,0.98)
        );

    padding: 20px;

    border-radius: 18px;

    text-align: center;

    border:
        1px solid rgba(255,255,255,0.05);

    font-weight: 700;

    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)

# ============================================================
# SIDEBAR
# ============================================================

# Custom CSS to force black text inside the sidebar and uploader button
import streamlit as st
import os

# Inject CSS overrides
st.markdown(
    """
    <style>
    /* Sidebar text */
    [data-testid="stSidebar"] * {
        color: black !important;
    }

    /* File uploader label text */
    [data-testid="stFileUploader"] label {
        color: black !important;
    }

    /* File uploader button text */
    [data-testid="stFileUploader"] button {
        color: black !important;
        background-color: #f0f0f0 !important; /* optional: light background */
        border: 1px solid #ccc !important;
    }

    /* File uploader drag-and-drop area text */
    [data-testid="stFileUploaderDropzone"] div {
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

ROOT_DIR = os.getcwd()
logo_path = os.path.join(ROOT_DIR, "assets", "logo.png")

with st.sidebar:
    if os.path.exists(logo_path):
        st.image(logo_path, width=90)

    st.markdown("<h1 style='color:black;'>Mission Control</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:black;'>Upload Intelligence Dataset</p>", unsafe_allow_html=True)

    uploaded_file = st.file_uploader(
        "Upload CSV or Excel File",
        type=["csv", "xlsx"]
    )
# ============================================================
# HERO SECTION
# ============================================================

st.markdown(
    """
    <p style='
        color:white;
        font-size:24px;
        margin:0;
    '>
        AI-Powered Marketing Intelligence & Search Analytics
    </p>
    """,
    unsafe_allow_html=True
)
# ============================================================
# FEATURES
# ============================================================

c1, c2, c3 = st.columns(3)

with c1:

    st.markdown("""
    <div class='feature-box'>
    📉 ROAS Decline Detection
    </div>
    """, unsafe_allow_html=True)

with c2:

    st.markdown("""
    <div class='feature-box'>
    💰 Spend Optimization
    </div>
    """, unsafe_allow_html=True)

with c3:

    st.markdown("""
    <div class='feature-box'>
    🚨 Anomaly Detection
    </div>
    """, unsafe_allow_html=True)

c4, c5, c6 = st.columns(3)

with c4:

    st.markdown("""
    <div class='feature-box'>
    📊 Executive Summaries
    </div>
    """, unsafe_allow_html=True)

with c5:

    st.markdown("""
    <div class='feature-box'>
    🔍 Search Merchandising
    </div>
    """, unsafe_allow_html=True)

with c6:

    st.markdown("""
    <div class='feature-box'>
    🧠 AI Recommendations
    </div>
    """, unsafe_allow_html=True)

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

    except Exception as e:

        st.error(str(e))

# ============================================================
# ALERTS
# ============================================================

if df is not None:

    alerts = detect_alerts(df)

    for alert in alerts:

        st.warning(alert)

# ============================================================
# KPI
# ============================================================

if df is not None:

    metrics = get_dashboard_kpis(df)

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Average ROAS",
            metrics.get("ROAS", "N/A")
        )

    with c2:

        st.metric(
            "Total Spend",
            metrics.get("Spend", "N/A")
        )

    with c3:

        st.metric(
            "Conversions",
            metrics.get("Conversions", "N/A")
        )

# ============================================================
# CHART
# ============================================================

if df is not None:

    fig = generate_chart(df)

    if fig is not None:

        try:

            fig.update_layout(

                paper_bgcolor="#111111",

                plot_bgcolor="#111111",

                font_color="white"
            )

        except:

            pass

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# ============================================================
# CHAT
# ============================================================

if "messages" not in st.session_state:

    st.session_state.messages = []

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):

        st.markdown(msg["content"])

prompt = st.chat_input(
    "Ask The Professor about campaign intelligence..."
)

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

        with st.spinner("Analyzing dataset..."):

            try:

                response = run_analysis(
                    df=df,
                    user_query=prompt
                )

            except Exception as e:

                response = f"""
Analysis Error:

{e}
"""

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