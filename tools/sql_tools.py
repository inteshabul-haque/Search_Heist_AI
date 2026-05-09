# -----------------------------------
# SQL QUERY GENERATOR
# -----------------------------------

def generate_sql_query(user_question):

    user_question = user_question.lower()

    # -----------------------------------
    # ROAS QUERY
    # -----------------------------------

    if "roas" in user_question:

        return """

        SELECT
            Campaign,
            AVG(ROAS) AS avg_roas
        FROM campaigns
        GROUP BY Campaign
        ORDER BY avg_roas DESC;

        """

    # -----------------------------------
    # SPEND QUERY
    # -----------------------------------

    elif "spend" in user_question:

        return """

        SELECT
            Campaign,
            SUM(Spend) AS total_spend
        FROM campaigns
        GROUP BY Campaign
        ORDER BY total_spend DESC;

        """

    # -----------------------------------
    # CTR QUERY
    # -----------------------------------

    elif "ctr" in user_question:

        return """

        SELECT
            Campaign,
            AVG(CTR) AS avg_ctr
        FROM campaigns
        GROUP BY Campaign
        ORDER BY avg_ctr DESC;

        """

    # -----------------------------------
    # DEFAULT QUERY
    # -----------------------------------

    return "No SQL query available."