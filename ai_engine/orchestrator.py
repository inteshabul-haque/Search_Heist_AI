from ai_engine.router import route_query

from ai_engine.search_agent import analyze_search_data

from ai_engine.sql_agent import generate_sql

from analytics.kpi_engine import analyze_kpis

from analytics.campaign_analysis import analyze_campaigns

from analytics.executive_summary import generate_executive_summary

from analytics.auto_insights import generate_auto_insights


def run_analysis(df, user_query):

    # ========================================================
    # ROUTER
    # ========================================================

    route = route_query(user_query)

    # ========================================================
    # SQL AGENT
    # ========================================================

    if route == "sql":

        return generate_sql(user_query)

    # ========================================================
    # SEARCH ANALYSIS
    # ========================================================

    search_results = analyze_search_data(df)

    # ========================================================
    # KPI ANALYSIS
    # ========================================================

    kpi_results = analyze_kpis(df)

    # ========================================================
    # CAMPAIGN ANALYSIS
    # ========================================================

    campaign_results = analyze_campaigns(df)

    # ========================================================
    # AUTO INSIGHTS
    # ========================================================

    auto_insights = generate_auto_insights(df)

    # ========================================================
    # EXECUTIVE SUMMARY
    # ========================================================

    summary = generate_executive_summary(
        df=df,
        user_query=user_query,
        kpi_results=kpi_results,
        campaign_results=campaign_results
    )

    # ========================================================
    # FINAL RESPONSE
    # ========================================================

    final_response = f"""

# SEARCH HEIST AI REPORT

---

## AUTO INSIGHTS

{auto_insights}

---

## KPI ANALYSIS

{kpi_results}

---

## CAMPAIGN ANALYSIS

{campaign_results}

---

## SEARCH ANALYSIS

{search_results}

---

## EXECUTIVE SUMMARY

{summary}

"""

    return final_response