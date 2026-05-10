def analyze_trends(df):

    trends = []

    if "revenue" in df.columns:

        revenue = df["revenue"].sum()

        if revenue > 0:

            trends.append(
                "Revenue trend appears positive."
            )

    if "add_to_cart" in df.columns:

        atc = df["add_to_cart"].sum()

        if atc > 0:

            trends.append(
                "Cart engagement is healthy."
            )

    return trends