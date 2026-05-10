from analytics.column_detector import detect_columns


def analyze_kpis(df):

    insights = []

    detected = detect_columns(df)

    # =========================================
    # ROAS
    # =========================================

    if "roas" in detected:

        roas_col = detected["roas"]

        avg_roas = df[roas_col].mean()

        insights.append(
            f"Average ROAS: {avg_roas:.2f}"
        )

        low_roas = df[
            df[roas_col] < avg_roas
        ]

        insights.append(
            f"{len(low_roas)} campaigns below average ROAS."
        )

    # =========================================
    # SPEND
    # =========================================

    if "spend" in detected:

        spend_col = detected["spend"]

        total_spend = df[spend_col].sum()

        insights.append(
            f"Total Spend: ${total_spend:,.0f}"
        )

    # =========================================
    # CTR
    # =========================================

    if "ctr" in detected:

        ctr_col = detected["ctr"]

        avg_ctr = df[ctr_col].mean()

        insights.append(
            f"Average CTR: {avg_ctr:.2f}%"
        )

    # =========================================
    # CONVERSIONS
    # =========================================

    if "conversions" in detected:

        conv_col = detected["conversions"]

        total_conv = df[conv_col].sum()

        insights.append(
            f"Total Conversions: {total_conv:,.0f}"
        )

    return insights