import streamlit as st

def generate_charts(df):

    numeric_cols = df.select_dtypes(
        include="number"
    ).columns

    if len(numeric_cols) == 0:

        return

    # ========================================================
    # LINE CHART
    # ========================================================

    st.markdown(
        "### 📈 Trend Chart"
    )

    st.line_chart(
        df[numeric_cols]
    )

    # ========================================================
    # BAR CHART
    # ========================================================

    st.markdown(
        "### 📊 Comparison Chart"
    )

    st.bar_chart(
        df[numeric_cols].sum()
    )