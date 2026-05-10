def route_query(user_query):

    query = user_query.lower()

    # =========================================
    # SEARCH MERCHANDISING
    # =========================================

    if any(word in query for word in [
        "search",
        "query",
        "zero result",
        "merchandising",
        "ranking"
    ]):

        return "search"

    # =========================================
    # SQL
    # =========================================

    if any(word in query for word in [
        "sql",
        "query",
        "table",
        "join",
        "select"
    ]):

        return "sql"

    # =========================================
    # EXECUTIVE SUMMARY
    # =========================================

    if any(word in query for word in [
        "summary",
        "leadership",
        "executive",
        "overview"
    ]):

        return "summary"

    # =========================================
    # DEFAULT
    # =========================================

    return "campaign"