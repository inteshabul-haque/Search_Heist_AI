# ============================================================
# KPI ENGINE
# ============================================================

def calculate_kpis(df):

    revenue = 0
    purchases = 0
    conversion_rate = 0
    aov = 0

    # ========================================================
    # REVENUE
    # ========================================================

    if "revenue" in df.columns:

        revenue = round(
            df["revenue"].sum(),
            2
        )

    # ========================================================
    # PURCHASES
    # ========================================================

    if "purchase" in df.columns:

        purchases = int(
            df["purchase"].sum()
        )

    # ========================================================
    # CONVERSION RATE
    # ========================================================

    if "visited" in df.columns and "purchase" in df.columns:

        visits = df["visited"].sum()

        if visits > 0:

            conversion_rate = round(
                (purchases / visits) * 100,
                2
            )

    # ========================================================
    # AOV
    # ========================================================

    if purchases > 0:

        aov = round(
            revenue / purchases,
            2
        )

    return {

        "revenue": revenue,

        "purchases": purchases,

        "conversion_rate": conversion_rate,

        "aov": aov
    }