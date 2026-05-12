import pandas as pd
import numpy as np

# ============================================================
# TREND ANALYSIS
# ============================================================

def analyze_trends(df):

    insights = []

    numeric_cols = df.select_dtypes(
        include="number"
    ).columns.tolist()

    # ========================================================
    # AUTO DETECT IMPORTANT COLUMNS
    # ========================================================

    revenue_col = None
    purchase_col = None
    traffic_col = None
    cart_col = None
    category_col = None

    for col in df.columns:

        lower_col = col.lower()

        # ----------------------------------------------------

        if any(x in lower_col for x in [
            "revenue",
            "sales",
            "gmv",
            "income"
        ]):

            revenue_col = col

        # ----------------------------------------------------

        elif any(x in lower_col for x in [
            "purchase",
            "orders",
            "transactions"
        ]):

            purchase_col = col

        # ----------------------------------------------------

        elif any(x in lower_col for x in [
            "visit",
            "traffic",
            "session",
            "users"
        ]):

            traffic_col = col

        # ----------------------------------------------------

        elif any(x in lower_col for x in [
            "cart",
            "basket"
        ]):

            cart_col = col

        # ----------------------------------------------------

        elif any(x in lower_col for x in [
            "category",
            "product",
            "segment",
            "brand"
        ]):

            category_col = col

    # ========================================================
    # REVENUE TREND
    # ========================================================

    try:

        if revenue_col:

            revenue_growth = round(

                df[revenue_col]

                .pct_change()

                .mean() * 100,
                2
            )

            revenue_volatility = round(

                df[revenue_col]

                .std(),
                2
            )

            if revenue_growth > 0:

                insights.append(
                    f"""
📈 Revenue performance is showing positive momentum,
with an average growth trend of
{revenue_growth}% across records.
However, revenue volatility of
{revenue_volatility}
suggests fluctuations that may require monitoring.
"""
                )

            else:

                insights.append(
                    f"""
📉 Revenue trend indicates declining momentum,
with average movement of
{revenue_growth}%.
This may signal weakening campaign performance
or reduced customer demand.
"""
                )

    except:
        pass

    # ========================================================
    # PURCHASE TREND
    # ========================================================

    try:

        if purchase_col:

            purchase_growth = round(

                df[purchase_col]

                .pct_change()

                .mean() * 100,
                2
            )

            total_purchase = int(
                df[purchase_col].sum()
            )

            insights.append(
                f"""
🛒 Customer purchasing activity generated
{total_purchase}
transactions overall.
Trend analysis shows average purchase movement of
{purchase_growth}%,
highlighting evolving customer buying behavior.
"""
            )

    except:
        pass

    # ========================================================
    # TRAFFIC VS CONVERSION
    # ========================================================

    try:

        if traffic_col and purchase_col:

            total_traffic = df[
                traffic_col
            ].sum()

            total_purchase = df[
                purchase_col
            ].sum()

            if total_traffic > 0:

                conversion_rate = round(
                    (
                        total_purchase
                        / total_traffic
                    ) * 100,
                    2
                )

                insights.append(
                    f"""
🚦 Customer conversion efficiency currently stands at
{conversion_rate}%.
Traffic levels remain strong,
but conversion optimization opportunities
may exist within the customer journey.
"""
                )

    except:
        pass

    # ========================================================
    # CART ENGAGEMENT
    # ========================================================

    try:

        if cart_col and traffic_col:

            cart_rate = round(
                (
                    df[cart_col].sum()
                    /
                    df[traffic_col].sum()
                ) * 100,
                2
            )

            if cart_rate > 20:

                insights.append(
                    f"""
🧺 Cart engagement remains healthy,
with approximately
{cart_rate}% of visitors reaching the cart stage.
This indicates strong product interest and engagement.
"""
                )

            else:

                insights.append(
                    f"""
⚠️ Cart engagement is relatively low at
{cart_rate}%,
suggesting potential friction in product discovery
or purchase intent.
"""
                )

    except:
        pass

    # ========================================================
    # CATEGORY / SEGMENT ANALYSIS
    # ========================================================

    try:

        if category_col and revenue_col:

            category_summary = (

                df.groupby(category_col)[revenue_col]

                .sum()

                .sort_values(
                    ascending=False
                )
            )

            top_category = (
                category_summary.index[0]
            )

            weakest_category = (
                category_summary.index[-1]
            )

            insights.append(
                f"""
🏆 The strongest-performing segment is
{top_category},
while
{weakest_category}
shows comparatively weaker performance.
This indicates shifting consumer preferences
across product categories or audience segments.
"""
            )

    except:
        pass

    # ========================================================
    # OUTLIER DETECTION
    # ========================================================

    try:

        outlier_cols = []

        for col in numeric_cols:

            q1 = df[col].quantile(0.25)

            q3 = df[col].quantile(0.75)

            iqr = q3 - q1

            lower = q1 - 1.5 * iqr

            upper = q3 + 1.5 * iqr

            outliers = df[
                (df[col] < lower)
                |
                (df[col] > upper)
            ]

            if len(outliers) > 0:

                outlier_cols.append(
                    f"{col}"
                )

        if len(outlier_cols) > 0:

            insights.append(
                f"""
🚨 Significant anomalies were detected in:
{', '.join(outlier_cols)}.
These spikes or declines may indicate campaign surges,
tracking inconsistencies,
or emerging business opportunities.
"""
            )

    except:
        pass

    # ========================================================
    # LIMIT INSIGHTS
    # ========================================================

    insights = insights[:5]

    # ========================================================
    # FALLBACK
    # ========================================================

    if len(insights) == 0:

        insights.append(
            """
📊 No major trend patterns were detected
in the current dataset.
"""
        )

    return insights