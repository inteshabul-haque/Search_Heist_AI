def detect_anomalies(df):

    anomalies = []

    if "checkout" in df.columns:

        checkout = df["checkout"].sum()

        if checkout == 0:

            anomalies.append(
                "Checkout performance is critically low."
            )

    if "purchase" in df.columns:

        purchases = df["purchase"].sum()

        if purchases < 2:

            anomalies.append(
                "Purchase count is unusually low."
            )

    return anomalies