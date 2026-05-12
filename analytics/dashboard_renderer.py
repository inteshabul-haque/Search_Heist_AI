import streamlit as st
import plotly.express as px

from analytics.executive_summary import generate_executive_summary
from analytics.kpi_engine import calculate_kpis
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
        """
        <h3 style='
            color:#ff004f;
            margin-top:15px;
            margin-bottom:15px;
            font-size:24px;
            font-weight:800;
        '>
        🧠 Executive Summary
        </h3>
        """,
        unsafe_allow_html=True
    )

    summary = generate_executive_summary(df)

    st.markdown(
        summary,
        unsafe_allow_html=True
    )

    # ========================================================
    # FUNNEL ANALYSIS
    # ========================================================

    funnel_df = analyze_funnel(df)

    if funnel_df is not None:

        st.markdown(
            """
            <h3 style='
                color:#ff004f;
                margin-top:20px;
                margin-bottom:15px;
                font-size:24px;
                font-weight:800;
            '>
            📉 Funnel Analysis
            </h3>
            """,
            unsafe_allow_html=True
        )

        fig_funnel = px.funnel(

            funnel_df,

            x="users",

            y="stage",

            template="plotly_dark"
        )

        fig_funnel.update_layout(

            paper_bgcolor="#050505",

            plot_bgcolor="#050505",

            font=dict(
                color="white",
                size=13
            ),

            height=380,

            margin=dict(
                l=10,
                r=10,
                t=20,
                b=10
            )
        )

        fig_funnel.update_traces(

            textfont_size=14
        )

        st.plotly_chart(

            fig_funnel,

            use_container_width=True
        )

    # ========================================================
    # CHARTS
    # ========================================================

    st.markdown(
        """
        <h3 style='
            color:#ff004f;
            margin-top:20px;
            margin-bottom:15px;
            font-size:24px;
            font-weight:800;
        '>
        📈 Trend Analysis
        </h3>
        """,
        unsafe_allow_html=True
    )

    generate_charts(df)

    # ========================================================
    # ANOMALIES
    # ========================================================

    st.markdown(
        """
        <h3 style='
            color:#ff004f;
            margin-top:20px;
            margin-bottom:15px;
            font-size:24px;
            font-weight:800;
        '>
        🚨 AI Detected Issues
        </h3>
        """,
        unsafe_allow_html=True
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
        """
        <h3 style='
            color:#ff004f;
            margin-top:20px;
            margin-bottom:15px;
            font-size:24px;
            font-weight:800;
        '>
        🔥 Trend Insights
        </h3>
        """,
        unsafe_allow_html=True
    )

    trends = analyze_trends(df)

    for trend in trends:

        st.info(trend)

    # ========================================================
    # DATA PREVIEW
    # ========================================================

    st.markdown(
        """
        <h3 style='
            color:#ff004f;
            margin-top:20px;
            margin-bottom:15px;
            font-size:24px;
            font-weight:800;
        '>
        📋 Dataset Preview
        </h3>
        """,
        unsafe_allow_html=True
    )

    st.dataframe(
        df.head(20),
        use_container_width=True
    )