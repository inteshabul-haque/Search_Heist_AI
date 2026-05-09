import plotly.express as px

# -----------------------------------
# ROAS TREND CHART
# -----------------------------------

def create_roas_chart(df):

    # STANDARDIZE COLUMNS
    df.columns = [
        col.strip().lower()
        for col in df.columns
    ]

    if "date" in df.columns and "roas" in df.columns:

        fig = px.line(
            df,
            x="date",
            y="roas",
            title="ROAS Trend"
        )

        return fig

    return None


# -----------------------------------
# SPEND TREND CHART
# -----------------------------------

def create_spend_chart(df):

    # STANDARDIZE COLUMNS
    df.columns = [
        col.strip().lower()
        for col in df.columns
    ]

    if "campaign" in df.columns and "spend" in df.columns:

        fig = px.bar(
            df,
            x="campaign",
            y="spend",
            title="Campaign Spend Analysis"
        )

        return fig

    return None


# -----------------------------------
# CTR TREND CHART
# -----------------------------------

def create_ctr_chart(df):

    # STANDARDIZE COLUMNS
    df.columns = [
        col.strip().lower()
        for col in df.columns
    ]

    if "campaign" in df.columns and "ctr" in df.columns:

        fig = px.bar(
            df,
            x="campaign",
            y="ctr",
            title="CTR Performance"
        )

        return fig

    return None