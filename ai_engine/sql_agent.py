def generate_sql(user_query):

    return f"""

SELECT *
FROM campaigns
WHERE spend > 1000
ORDER BY roas ASC;

Generated based on:
{user_query}

"""