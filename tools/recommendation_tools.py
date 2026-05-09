# -----------------------------------
# OPTIMIZATION RECOMMENDATIONS
# -----------------------------------

def generate_recommendations(df):

    recommendations = []

    # STANDARDIZE COLUMNS
    df.columns = [
        col.strip().lower()
        for col in df.columns
    ]

    # -----------------------------------
    # ROAS OPTIMIZATION
    # -----------------------------------

    if "roas" in df.columns:

        avg_roas = df["roas"].mean()

        low_roas = df[
            df["roas"] < avg_roas
        ]

        if len(low_roas) > 0:

            recommendations.append(
                "- Reduce spend on low ROAS campaigns."
            )

            recommendations.append(
                "- Reallocate budget toward higher-performing campaigns."
            )

    # -----------------------------------
    # CTR OPTIMIZATION
    # -----------------------------------

    if "ctr" in df.columns:

        low_ctr = df[
            df["ctr"] < df["ctr"].mean()
        ]

        if len(low_ctr) > 0:

            recommendations.append(
                "- Improve ad creatives for campaigns with weak CTR."
            )

            recommendations.append(
                "- Test new headlines and creatives."
            )

    # -----------------------------------
    # CONVERSION OPTIMIZATION
    # -----------------------------------

    if "conversion_rate" in df.columns:

        low_conversion = df[
            df["conversion_rate"]
            < df["conversion_rate"].mean()
        ]

        if len(low_conversion) > 0:

            recommendations.append(
                "- Optimize landing pages for weak-converting campaigns."
            )

            recommendations.append(
                "- Review funnel drop-off points."
            )

    # -----------------------------------
    # DEAD CAMPAIGNS
    # -----------------------------------

    if "conversions" in df.columns:

        dead_campaigns = df[
            df["conversions"] == 0
        ]

        if len(dead_campaigns) > 0:

            recommendations.append(
                "- Pause campaigns generating zero conversions."
            )

            recommendations.append(
                "- Review targeting and audience relevance."
            )

    # -----------------------------------
    # SPEND ANALYSIS
    # -----------------------------------

    if "spend" in df.columns:

        high_spend = df[
            df["spend"] > df["spend"].mean()
        ]

        if len(high_spend) > 0:

            recommendations.append(
                "- Audit high-spend campaigns for efficiency."
            )

    return "\n".join(recommendations)