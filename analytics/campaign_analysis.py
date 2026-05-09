# -----------------------------------
# CAMPAIGN PERFORMANCE ANALYSIS
# -----------------------------------

def analyze_campaign_performance(df):

    insights = []

    # -----------------------------------
    # STANDARDIZE COLUMN NAMES
    # -----------------------------------

    df.columns = [
        col.strip().lower()
        for col in df.columns
    ]

    # -----------------------------------
    # ROAS ANALYSIS
    # -----------------------------------

    if "roas" in df.columns:

        avg_roas = df["roas"].mean()

        low_roas = df[
            df["roas"] < avg_roas
        ]

        insights.append(
            f"Average ROAS is {round(avg_roas, 2)}."
        )

        insights.append(
            f"{len(low_roas)} campaigns are below average ROAS."
        )

    # -----------------------------------
    # SPEND ANALYSIS
    # -----------------------------------

    if "spend" in df.columns:

        high_spend = df[
            df["spend"] > df["spend"].mean()
        ]

        insights.append(
            f"{len(high_spend)} campaigns have above-average spend."
        )

    # -----------------------------------
    # CTR ANALYSIS
    # -----------------------------------

    if "ctr" in df.columns:

        low_ctr = df[
            df["ctr"] < df["ctr"].mean()
        ]

        insights.append(
            f"{len(low_ctr)} campaigns have below-average CTR."
        )

    # -----------------------------------
    # CONVERSION ANALYSIS
    # -----------------------------------

    if "conversion_rate" in df.columns:

        low_conversion = df[
            df["conversion_rate"]
            < df["conversion_rate"].mean()
        ]

        insights.append(
            f"{len(low_conversion)} campaigns have weak conversion rates."
        )

    # -----------------------------------
    # DEAD CAMPAIGNS
    # -----------------------------------

    if "conversions" in df.columns:

        dead_campaigns = df[
            df["conversions"] == 0
        ]

        insights.append(
            f"{len(dead_campaigns)} campaigns have zero conversions."
        )

    return "\n".join(insights)