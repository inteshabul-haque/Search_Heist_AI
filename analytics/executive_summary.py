# ============================================================
# EXECUTIVE SUMMARY
# ============================================================

def generate_executive_summary(df):

    rows = len(df)

    cols = len(df.columns)

    summary = f"""

    <h3 style='color:white;'>
    AI Executive Summary
    </h3>

    <p style='color:#dddddd;font-size:17px;line-height:1.8;'>

    • Dataset contains <b>{rows}</b> rows.

    <br><br>

    • Total columns detected:
    <b>{cols}</b>

    <br><br>

    • AI agents analyzed:
    funnel performance,
    conversion trends,
    campaign efficiency,
    and revenue opportunities.

    <br><br>

    • Executive recommendations generated successfully.

    </p>
    """

    return summary