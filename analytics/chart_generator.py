import streamlit as st
import plotly.express as px
import pandas as pd

# =========================================================
# CHART GENERATOR
# =========================================================

def generate_charts(df):

    # =====================================================
    # NUMERIC COLUMNS
    # =====================================================

    numeric_cols = df.select_dtypes(
        include="number"
    ).columns.tolist()

    if len(numeric_cols) == 0:

        st.warning(
            "No numeric columns found."
        )

        return

    # =====================================================
    # CHART DATAFRAME
    # =====================================================

    chart_df = df[numeric_cols].copy()

    # =====================================================
    # TREND LINE CHART
    # =====================================================

    fig_line = px.line(

        chart_df,

        template="plotly_dark"
    )

    fig_line.update_layout(

        paper_bgcolor="#050505",

        plot_bgcolor="#050505",

        font=dict(
            color="white",
            size=12
        ),

        height=360,

        margin=dict(
            l=10,
            r=10,
            t=20,
            b=10
        ),

        legend=dict(

            orientation="h",

            yanchor="bottom",

            y=1.02,

            xanchor="right",

            x=1,

            font=dict(
                size=10,
                color="white"
            )
        ),

        hovermode="x unified"
    )

    fig_line.update_traces(

        line=dict(
            width=3
        )
    )

    st.plotly_chart(

        fig_line,

        use_container_width=True
    )

    # =====================================================
    # PERFORMANCE COMPARISON
    # =====================================================

    st.markdown(
        """
        <h3 style='
            color:#ff004f;
            margin-top:20px;
            margin-bottom:12px;
            font-size:24px;
            font-weight:800;
        '>
        📊 Performance Comparison
        </h3>
        """,
        unsafe_allow_html=True
    )

    # =====================================================
    # METRIC SELECTOR
    # =====================================================

    st.caption(
        "Select metrics to compare"
    )

    selected_metrics = st.multiselect(

        label="Choose Metrics",

        options=numeric_cols,

        default=[],

        placeholder="Select metrics..."
    )

    # =====================================================
    # EMPTY SELECTION
    # =====================================================

    if len(selected_metrics) == 0:

        st.info(
            "Please select metrics to display comparison chart."
        )

        return

    # =====================================================
    # SUMMARY DATAFRAME
    # =====================================================

    summary_df = pd.DataFrame({

        "Metric": selected_metrics,

        "Value": [

            df[col].sum()

            for col in selected_metrics
        ]
    })

    # =====================================================
    # BAR CHART
    # =====================================================

    fig_bar = px.bar(

        summary_df,

        x="Metric",

        y="Value",

        template="plotly_dark",

        text_auto=True
    )

    fig_bar.update_layout(

        paper_bgcolor="#050505",

        plot_bgcolor="#050505",

        font=dict(
            color="white",
            size=12
        ),

        height=360,

        margin=dict(
            l=10,
            r=10,
            t=20,
            b=10
        ),

        xaxis=dict(
            title="",
            tickangle=-15
        ),

        yaxis=dict(
            title=""
        )
    )

    fig_bar.update_traces(

        marker=dict(

            line=dict(
                width=1,
                color="#ff004f"
            )
        ),

        textposition="outside"
    )

    st.plotly_chart(

        fig_bar,

        use_container_width=True
    )