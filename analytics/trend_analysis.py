# -----------------------------------
# TREND ANALYSIS
# -----------------------------------

def analyze_trends(df):

    insights = []

    # STANDARDIZE COLUMNS
    df.columns = [
        col.strip().lower()
        for col in df.columns
    ]

    # ROAS TREND
    if "roas" in df.columns:

        first_roas = df["roas"].iloc[0]
        last_roas = df["roas"].iloc[-1]

        if last_roas > first_roas:

            insights.append(
                "ROAS trend is improving over time."
            )

        else:

            insights.append(
                "ROAS trend is declining over time."
            )

    # CTR TREND
    if "ctr" in df.columns:

        first_ctr = df["ctr"].iloc[0]
        last_ctr = df["ctr"].iloc[-1]

        if last_ctr > first_ctr:

            insights.append(
                "CTR trend is improving."
            )

        else:

            insights.append(
                "CTR trend is declining."
            )

    return "\n".join(insights)