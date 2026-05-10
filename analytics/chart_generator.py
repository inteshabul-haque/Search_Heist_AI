import plotly.express as px


def generate_chart(df):

    numeric_cols = df.select_dtypes(
        include="number"
    ).columns.tolist()

    if len(numeric_cols) < 2:

        return None

    x_col = numeric_cols[0]

    y_col = numeric_cols[1]

    fig = px.scatter(
        df,
        x=x_col,
        y=y_col,
        title=f"{x_col} vs {y_col}"
    )

    return fig