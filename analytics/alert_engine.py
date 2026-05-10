from analytics.column_detector import detect_columns


def detect_alerts(df):

    alerts = []

    detected = detect_columns(df)

    # ========================================================
    # ROAS ALERT
    # ========================================================

    if "roas" in detected:

        roas_col = detected["roas"]

        avg_roas = df[roas_col].mean()

        if avg_roas < 2:

            alerts.append(
                "🚨 Critical Alert: ROAS below target benchmark."
            )

    # ========================================================
    # CTR ALERT
    # ========================================================

    if "ctr" in detected:

        ctr_col = detected["ctr"]

        avg_ctr = df[ctr_col].mean()

        if avg_ctr < 1:

            alerts.append(
                "⚠ CTR performance is weak."
            )

    # ========================================================
    # CONVERSION ALERT
    # ========================================================

    if "conversions" in detected:

        conv_col = detected["conversions"]

        avg_conv = df[conv_col].mean()

        low_conv = df[
            df[conv_col] < avg_conv
        ]

        if len(low_conv) > 0:

            alerts.append(
                f"⚠ {len(low_conv)} campaigns below average conversions."
            )

    return alerts