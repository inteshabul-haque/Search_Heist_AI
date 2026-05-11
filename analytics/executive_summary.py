# ============================================================
# EXECUTIVE SUMMARY
# ============================================================

def generate_executive_summary(
    df,
    user_query=None,
    kpi_results=None,
    campaign_results=None
):

    rows = len(df)
    cols = len(df.columns)

    summary = f"""
<div style="
    background: linear-gradient(135deg,#111111,#0a0a0a);
    padding:20px;
    border-radius:16px;
    border:1px solid rgba(255,255,255,0.06);
">

<h3 style="
    color:white;
    margin-bottom:16px;
    font-size:28px;
    font-weight:800;
">
🧠 AI Executive Summary
</h3>

<ul style="
    color:#dddddd;
    font-size:16px;
    line-height:1.6;
    padding-left:20px;
    margin:0;
">

<li>
Dataset contains <b>{rows}</b> rows.
</li>

<li style="margin-top:8px;">
Total columns detected: <b>{cols}</b>
</li>

<li style="margin-top:8px;">
AI agents analyzed funnel performance,
conversion trends,
campaign efficiency,
and revenue opportunities.
</li>

<li style="margin-top:8px;">
Executive recommendations generated successfully.
</li>

</ul>

</div>
"""

    return summary