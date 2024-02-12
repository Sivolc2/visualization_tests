import polars as pl
from dash import dash_table
from typing import Any

def convert_df_to_dash(data: pl.DataFrame) -> dash_table.DataTable:
    """
    Converts a Polars DataFrame into a format suitable for display in a Dash DataTable.
    """
    # Convert Polars DataFrame to a list of dictionaries, which is the format Dash DataTable expects.
    data_dict = data.to_dicts()
    return dash_table.DataTable(data=data_dict)

def format_datetime(data: pl.DataFrame, column_name: str) -> pl.DataFrame:
    """
    Formats a datetime column in a Polars DataFrame for better visualization.
    """
    # Placeholder for actual datetime formatting logic.
    # For the purpose of this example, we'll assume the datetime is already formatted.
    return data

def reverse_text(n_clicks, text):
    if n_clicks and text:
        return text[::-1]
    return ''
