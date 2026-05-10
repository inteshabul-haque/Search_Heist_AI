def generate_auto_insights(df):

    insights = []

    columns = [c.lower() for c in df.columns]

    # =========================================
    # ROAS ALERT
    # =========================================

    if "roas" in columns:

        avg_roas = df["ROAS"].mean()

        if avg_roas < 2:

            insights.append(
                "ROAS performance is below target benchmark."
            )

    # =========================================
    # HIGH SPEND ALERT
    # =========================================

    if "spend" in columns:

        spend = df["Spend"].sum()

        insights.append(
            f"Total marketing spend detected: ${spend:,.0f}"
        )

    return insights