import streamlit as st

from analytics.executive_summary import generate_executive_summary
from .kpi_engine import calculate_kpis
from analytics.funnel_analysis import analyze_funnel
from analytics.chart_generator import generate_charts
from analytics.anomaly_detection import detect_anomalies
from analytics.trend_analysis import analyze_trends

# ============================================================
# DASHBOARD RENDERER
# ============================================================

def render_dashboard(df):

    # ========================================================
    # KPIs
    # ========================================================

    kpis = calculate_kpis(df)

    st.markdown("## 📊 Executive KPIs")

    c1, c2, c3, c4 = st.columns(4)

    with c1:

        st.metric(
            "Revenue",
            f"${kpis['revenue']}"
        )

    with c2:

        st.metric(
            "Purchases",
            kpis["purchases"]
        )

    with c3:

        st.metric(
            "Conversion Rate",
            f"{kpis['conversion_rate']}%"
        )

    with c4:

        st.metric(
            "AOV",
            f"${kpis['aov']}"
        )

    # ========================================================
    # EXEC SUMMARY
    # ========================================================

    st.markdown(
        "## 🧠 Executive Summary"
    )

    summary = generate_executive_summary(df)

    st.markdown(
        f"""
        <div style='
            background:#111111;
            padding:25px;
            border-radius:18px;
            border:1px solid #222222;
        '>

        {summary}

        </div>
        """,
        unsafe_allow_html=True
    )

    # ========================================================
    # FUNNEL
    # ========================================================

    funnel_df = analyze_funnel(df)

    if funnel_df is not None:

        st.markdown(
            "## 📉 Funnel Analysis"
        )

        st.bar_chart(
            funnel_df.set_index("stage")
        )

    # ========================================================
    # CHARTS
    # ========================================================

    st.markdown(
        "## 📈 Trend Analysis"
    )

    generate_charts(df)

    # ========================================================
    # ANOMALIES
    # ========================================================

    st.markdown(
        "## 🚨 AI Detected Issues"
    )

    anomalies = detect_anomalies(df)

    if len(anomalies) > 0:

        for item in anomalies:

            st.warning(item)

    else:

        st.success(
            "No major anomalies detected."
        )

    # ========================================================
    # TRENDS
    # ========================================================

    st.markdown(
        "## 🔥 Trend Insights"
    )

    trends = analyze_trends(df)

    for trend in trends:

        st.info(trend)

    # ========================================================
    # DATA PREVIEW
    # ========================================================

    st.markdown(
        "## 📋 Dataset Preview"
    )

    st.dataframe(
        df.head(20),
        use_container_width=True
    )