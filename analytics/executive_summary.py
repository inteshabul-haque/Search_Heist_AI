import pandas as pd
import numpy as np

# ============================================================
# EXECUTIVE SUMMARY
# ============================================================

def generate_executive_summary(
    df,
    user_query=None,
    kpi_results=None,
    campaign_results=None
):

    # ========================================================
    # BASIC INFO
    # ========================================================

    rows = len(df)

    cols = len(df.columns)

    numeric_cols = df.select_dtypes(
        include="number"
    ).columns.tolist()

    # ========================================================
    # AUTO DETECT IMPORTANT COLUMNS
    # ========================================================

    column_map = {}

    for col in df.columns:

        lower_col = col.lower()

        # ----------------------------------------------------

        if any(x in lower_col for x in [
            "revenue",
            "sales",
            "gmv",
            "income"
        ]):

            column_map["revenue"] = col

        # ----------------------------------------------------

        elif any(x in lower_col for x in [
            "purchase",
            "orders",
            "transactions"
        ]):

            column_map["purchase"] = col

        # ----------------------------------------------------

        elif any(x in lower_col for x in [
            "visit",
            "traffic",
            "session",
            "users"
        ]):

            column_map["traffic"] = col

        # ----------------------------------------------------

        elif any(x in lower_col for x in [
            "category",
            "product",
            "segment",
            "brand"
        ]):

            column_map["category"] = col

        # ----------------------------------------------------

        elif any(x in lower_col for x in [
            "gender",
            "age",
            "city",
            "country",
            "region"
        ]):

            column_map["demographic"] = col

        # ----------------------------------------------------

        elif "date" in lower_col:

            column_map["date"] = col

    # ========================================================
    # INSIGHTS CONTAINER
    # ========================================================

    insights = []

    # ========================================================
    # DATASET OVERVIEW
    # ========================================================

    insights.append(
        f"""
<li style="margin-top:10px;">
<b>Dataset Overview:</b>
The dataset contains
<b>{rows}</b> rows and
<b>{cols}</b> columns,
including
<b>{len(numeric_cols)}</b>
numeric business metrics analyzed by AI agents.
</li>
"""
    )

    # ========================================================
    # REVENUE ANALYSIS
    # ========================================================

    if "revenue" in column_map:

        revenue_col = column_map["revenue"]

        total_revenue = round(
            df[revenue_col].sum(),
            2
        )

        avg_revenue = round(
            df[revenue_col].mean(),
            2
        )

        max_revenue = round(
            df[revenue_col].max(),
            2
        )

        min_revenue = round(
            df[revenue_col].min(),
            2
        )

        revenue_growth = round(
            df[revenue_col]
            .pct_change()
            .mean() * 100,
            2
        )

        insights.append(
            f"""
<li style="margin-top:10px;">
<b>Revenue Performance:</b>
Total revenue generated was
<b>${total_revenue}</b>,
with an average value of
<b>${avg_revenue}</b>.
Peak revenue reached
<b>${max_revenue}</b>,
while the minimum observed value was
<b>${min_revenue}</b>.
Average revenue movement across records was
<b>{revenue_growth}%</b>.
</li>
"""
        )

    # ========================================================
    # PURCHASE / TRANSACTION ANALYSIS
    # ========================================================

    if "purchase" in column_map:

        purchase_col = column_map["purchase"]

        total_purchase = int(
            df[purchase_col].sum()
        )

        avg_purchase = round(
            df[purchase_col].mean(),
            2
        )

        purchase_growth = round(
            df[purchase_col]
            .pct_change()
            .mean() * 100,
            2
        )

        insights.append(
            f"""
<li style="margin-top:10px;">
<b>Purchasing Trends:</b>
Customers completed
<b>{total_purchase}</b>
transactions overall,
with an average of
<b>{avg_purchase}</b>
per record.
Trend analysis indicates an average movement of
<b>{purchase_growth}%</b>,
highlighting changes in customer buying behavior.
</li>
"""
        )

    # ========================================================
    # TRAFFIC VS PURCHASE CONVERSION
    # ========================================================

    if (
        "traffic" in column_map
        and
        "purchase" in column_map
    ):

        traffic_col = column_map["traffic"]

        purchase_col = column_map["purchase"]

        total_traffic = df[
            traffic_col
        ].sum()

        total_purchase = df[
            purchase_col
        ].sum()

        if total_traffic > 0:

            conversion_rate = round(
                (total_purchase / total_traffic) * 100,
                2
            )

            insights.append(
                f"""
<li style="margin-top:10px;">
<b>Customer Conversion:</b>
The dataset reflects an overall conversion rate of
<b>{conversion_rate}%</b>.
This suggests opportunities to optimize
customer journeys and reduce funnel drop-offs.
</li>
"""
            )

    # ========================================================
    # CATEGORY / PRODUCT ANALYSIS
    # ========================================================

    if (
        "category" in column_map
        and
        "revenue" in column_map
    ):

        category_col = column_map["category"]

        revenue_col = column_map["revenue"]

        category_performance = (

            df.groupby(category_col)[revenue_col]

            .sum()

            .sort_values(
                ascending=False
            )
        )

        top_category = (
            category_performance.index[0]
        )

        top_value = round(
            category_performance.iloc[0],
            2
        )

        weakest_category = (
            category_performance.index[-1]
        )

        weakest_value = round(
            category_performance.iloc[-1],
            2
        )

        insights.append(
            f"""
<li style="margin-top:10px;">
<b>Product / Segment Performance:</b>
The strongest-performing segment was
<b>{top_category}</b>,
generating approximately
<b>${top_value}</b>
in revenue.
The weakest-performing segment was
<b>{weakest_category}</b>
with approximately
<b>${weakest_value}</b>.
This highlights areas for expansion and optimization.
</li>
"""
        )

    # ========================================================
    # DEMOGRAPHIC ANALYSIS
    # ========================================================

    if "demographic" in column_map:

        demographic_col = column_map[
            "demographic"
        ]

        top_group = (

            df[demographic_col]

            .value_counts()

            .idxmax()
        )

        top_share = round(

            df[demographic_col]

            .value_counts(
                normalize=True
            )

            .max() * 100,
            2
        )

        insights.append(
            f"""
<li style="margin-top:10px;">
<b>Customer Demographics:</b>
The largest audience group identified was
<b>{top_group}</b>,
representing
<b>{top_share}%</b>
of the dataset.
This segment appears to be the primary driver of engagement and performance.
</li>
"""
        )

    # ========================================================
    # OUTLIER DETECTION
    # ========================================================

    outlier_cols = []

    try:

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
                    f"{col} ({len(outliers)})"
                )

    except:
        pass

    if len(outlier_cols) > 0:

        insights.append(
            f"""
<li style="margin-top:10px;">
<b>Outlier Detection:</b>
Potential anomalies were detected in
<b>{', '.join(outlier_cols)}</b>.
These unusually high or low values may indicate campaign spikes,
tracking inconsistencies,
or emerging business opportunities.
</li>
"""
        )

    # ========================================================
    # DATA QUALITY
    # ========================================================

    missing_values = int(
        df.isnull().sum().sum()
    )

    duplicate_rows = int(
        df.duplicated().sum()
    )

    insights.append(
        f"""
<li style="margin-top:10px;">
<b>Data Quality:</b>
The dataset contains
<b>{missing_values}</b>
missing values and
<b>{duplicate_rows}</b>
duplicate rows.
Improving data consistency may strengthen reporting reliability and decision-making accuracy.
</li>
"""
    )

    # ========================================================
    # LIMIT INSIGHTS
    # ========================================================

    insights = insights[:5]

    # ========================================================
    # FINAL SUMMARY HTML
    # ========================================================

    summary = f"""

<div style="
    background: linear-gradient(135deg,#111111,#0a0a0a);
    padding:24px;
    border-radius:18px;
    border:1px solid rgba(255,255,255,0.06);
">

<h3 style="
    color:white;
    margin-bottom:18px;
    font-size:28px;
    font-weight:800;
">
🧠 Executive Summary
</h3>

<ul style="
    color:#dddddd;
    font-size:16px;
    line-height:1.8;
    padding-left:20px;
    margin:0;
">

{''.join(insights)}

</ul>

</div>

"""

    return summary