import pandas as pd

# ============================================================
# FUNNEL ANALYSIS
# ============================================================

def analyze_funnel(df):

    funnel_steps = [

        "visited",

        "product_view",

        "add_to_cart",

        "checkout",

        "purchase"
    ]

    existing_steps = [

        step for step in funnel_steps

        if step in df.columns
    ]

    if len(existing_steps) == 0:

        return None

    values = []

    for step in existing_steps:

        values.append(
            df[step].sum()
        )

    funnel_df = pd.DataFrame({

        "stage": existing_steps,

        "users": values
    })

    return funnel_df