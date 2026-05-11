def calculate_kpis(df):

    revenue = 0
    purchases = 0
    conversion_rate = 0
    aov = 0

    revenue_col = None
    purchase_col = None
    visitor_col = None

    # Detect columns automatically

    for col in df.columns:

        c = col.lower()

        if "revenue" in c:
            revenue_col = col

        if "purchase" in c or "order" in c:
            purchase_col = col

        if "visit" in c or "traffic" in c:
            visitor_col = col

    # Revenue

    if revenue_col:
        revenue = round(df[revenue_col].sum(), 2)

    # Purchases

    if purchase_col:
        purchases = int(df[purchase_col].sum())

    # Conversion Rate

    if visitor_col and purchase_col:

        visits = df[visitor_col].sum()

        if visits > 0:

            conversion_rate = round(
                (purchases / visits) * 100,
                2
            )

    # AOV

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