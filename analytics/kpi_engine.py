# -----------------------------------
# KPI CALCULATIONS
# -----------------------------------

def calculate_kpis(df):

    kpis = {}

    # STANDARDIZE COLUMNS
    df.columns = [
        col.strip().lower()
        for col in df.columns
    ]

    # TOTAL SPEND
    if "spend" in df.columns:

        kpis["Total Spend"] = round(
            df["spend"].sum(),
            2
        )

    # TOTAL REVENUE
    if "revenue" in df.columns:

        kpis["Total Revenue"] = round(
            df["revenue"].sum(),
            2
        )

    # AVERAGE ROAS
    if "roas" in df.columns:

        kpis["Average ROAS"] = round(
            df["roas"].mean(),
            2
        )

    # AVERAGE CTR
    if "ctr" in df.columns:

        kpis["Average CTR"] = round(
            df["ctr"].mean(),
            2
        )

    # TOTAL CONVERSIONS
    if "conversions" in df.columns:

        kpis["Total Conversions"] = int(
            df["conversions"].sum()
        )

    # AVERAGE CPC
    if "cpc" in df.columns:

        kpis["Average CPC"] = round(
            df["cpc"].mean(),
            2
        )

    return kpis