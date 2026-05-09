# -----------------------------------
# ANOMALY DETECTION
# -----------------------------------

def detect_anomalies(df):

    anomalies = []

    # STANDARDIZE COLUMNS
    df.columns = [
        col.strip().lower()
        for col in df.columns
    ]

    # -----------------------------------
    # ROAS ANOMALY
    # -----------------------------------

    if "roas" in df.columns:

        avg_roas = df["roas"].mean()

        low_roas = df[
            df["roas"] < (avg_roas * 0.5)
        ]

        if len(low_roas) > 0:

            anomalies.append(
                f"{len(low_roas)} campaigns show critical ROAS decline."
            )

    # -----------------------------------
    # CTR ANOMALY
    # -----------------------------------

    if "ctr" in df.columns:

        avg_ctr = df["ctr"].mean()

        low_ctr = df[
            df["ctr"] < (avg_ctr * 0.5)
        ]

        if len(low_ctr) > 0:

            anomalies.append(
                f"{len(low_ctr)} campaigns show abnormal CTR decline."
            )

    # -----------------------------------
    # CONVERSION ANOMALY
    # -----------------------------------

    if "conversions" in df.columns:

        zero_conversion = df[
            df["conversions"] == 0
        ]

        if len(zero_conversion) > 0:

            anomalies.append(
                f"{len(zero_conversion)} campaigns have zero conversions."
            )

    return "\n".join(anomalies)