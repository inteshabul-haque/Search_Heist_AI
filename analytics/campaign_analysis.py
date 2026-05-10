def analyze_campaigns(df):

    insights = []

    columns = [c.lower() for c in df.columns]

    # =========================================
    # HIGH SPEND LOW ROAS
    # =========================================

    if "spend" in columns and "roas" in columns:

        bad_campaigns = df[
            (df["Spend"] > df["Spend"].mean())
            &
            (df["ROAS"] < df["ROAS"].mean())
        ]

        if len(bad_campaigns) > 0:

            insights.append(
                f"{len(bad_campaigns)} campaigns detected with high spend and low ROAS."
            )

    return insights