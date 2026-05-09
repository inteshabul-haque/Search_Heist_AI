# -----------------------------------
# AUTONOMOUS AI INSIGHTS
# -----------------------------------

def generate_auto_insights(df):

    insights = []

    # STANDARDIZE COLUMNS
    df.columns = [
        col.strip().lower()
        for col in df.columns
    ]

    # -----------------------------------
    # ROAS INSIGHTS
    # -----------------------------------

    if "roas" in df.columns:

        avg_roas = df["roas"].mean()

        low_roas = df[
            df["roas"] < avg_roas
        ]

        if len(low_roas) > 0:

            insights.append(
                f"⚠️ {len(low_roas)} campaigns are below average ROAS."
            )

    # -----------------------------------
    # CTR INSIGHTS
    # -----------------------------------

    if "ctr" in df.columns:

        avg_ctr = df["ctr"].mean()

        low_ctr = df[
            df["ctr"] < avg_ctr
        ]

        if len(low_ctr) > 0:

            insights.append(
                f"📉 {len(low_ctr)} campaigns have weak CTR performance."
            )

    # -----------------------------------
    # CONVERSION INSIGHTS
    # -----------------------------------

    if "conversions" in df.columns:

        zero_conversion = df[
            df["conversions"] == 0
        ]

        if len(zero_conversion) > 0:

            insights.append(
                f"🚨 {len(zero_conversion)} campaigns have zero conversions."
            )

    # -----------------------------------
    # SPEND INSIGHTS
    # -----------------------------------

    if "spend" in df.columns:

        high_spend = df[
            df["spend"] > df["spend"].mean()
        ]

        if len(high_spend) > 0:

            insights.append(
                f"💰 {len(high_spend)} campaigns show above-average spend."
            )

    return insights