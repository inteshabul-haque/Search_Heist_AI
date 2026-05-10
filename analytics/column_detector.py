def detect_columns(df):

    detected = {}

    columns = df.columns.tolist()

    lower_map = {
        c.lower(): c for c in columns
    }

    # ========================================================
    # ROAS
    # ========================================================

    for p in [
        "roas",
        "return on ad spend"
    ]:

        if p in lower_map:

            detected["roas"] = lower_map[p]

    # ========================================================
    # SPEND
    # ========================================================

    for p in [
        "spend",
        "cost",
        "ad spend"
    ]:

        if p in lower_map:

            detected["spend"] = lower_map[p]

    # ========================================================
    # CTR
    # ========================================================

    for p in [
        "ctr",
        "click through rate"
    ]:

        if p in lower_map:

            detected["ctr"] = lower_map[p]

    # ========================================================
    # CONVERSIONS
    # ========================================================

    for p in [
        "conversions",
        "orders",
        "sales"
    ]:

        if p in lower_map:

            detected["conversions"] = lower_map[p]

    return detected