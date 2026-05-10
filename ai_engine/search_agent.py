def analyze_search_data(df):

    insights = []

    columns = [c.lower() for c in df.columns]

    # =========================================
    # ZERO RESULT QUERIES
    # =========================================

    if "results" in columns:

        zero_results = df[df["Results"] == 0]

        insights.append(
            f"Detected {len(zero_results)} zero-result search queries."
        )

    # =========================================
    # LOW CTR QUERIES
    # =========================================

    if "ctr" in columns:

        low_ctr = df[df["CTR"] < df["CTR"].mean()]

        insights.append(
            f"{len(low_ctr)} queries detected with below-average CTR."
        )

    return insights