from analytics.column_detector import detect_columns


def get_dashboard_kpis(df):

    detected = detect_columns(df)

    metrics = {}

    # ========================================================
    # ROAS
    # ========================================================

    if "roas" in detected:

        roas_col = detected["roas"]

        metrics["ROAS"] = round(
            df[roas_col].mean(),
            2
        )

    # ========================================================
    # SPEND
    # ========================================================

    if "spend" in detected:

        spend_col = detected["spend"]

        metrics["Spend"] = round(
            df[spend_col].sum(),
            0
        )

    # ========================================================
    # CONVERSIONS
    # ========================================================

    if "conversions" in detected:

        conv_col = detected["conversions"]

        metrics["Conversions"] = round(
            df[conv_col].sum(),
            0
        )

    return metrics