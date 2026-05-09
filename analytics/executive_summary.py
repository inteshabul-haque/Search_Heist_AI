# -----------------------------------
# EXECUTIVE SUMMARY
# -----------------------------------

def generate_executive_summary(df):

    summary = []

    # STANDARDIZE COLUMNS
    df.columns = [
        col.strip().lower()
        for col in df.columns
    ]

    # ROAS
    if "roas" in df.columns:

        avg_roas = round(
            df["roas"].mean(),
            2
        )

        summary.append(
            f"Average ROAS is {avg_roas}."
        )

    # SPEND
    if "spend" in df.columns:

        total_spend = round(
            df["spend"].sum(),
            2
        )

        summary.append(
            f"Total marketing spend is {total_spend}."
        )

    # REVENUE
    if "revenue" in df.columns:

        total_revenue = round(
            df["revenue"].sum(),
            2
        )

        summary.append(
            f"Total revenue generated is {total_revenue}."
        )

    # CONVERSIONS
    if "conversions" in df.columns:

        total_conversions = int(
            df["conversions"].sum()
        )

        summary.append(
            f"Total conversions are {total_conversions}."
        )

    return "\n".join(summary)