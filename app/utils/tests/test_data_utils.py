import pytest
import polars as pl
from visualization_project.utils.data_utils import convert_df_to_dash

def test_convert_df_to_dash_empty_dataframe():
    """
    Test converting an empty Polars DataFrame to a Dash DataTable.
    """
    # Create an empty Polars DataFrame
    df = pl.DataFrame()
    
    # Convert the DataFrame to Dash DataTable
    dash_table = convert_df_to_dash(df)
    
    # Check if the conversion results in an empty data attribute
    assert dash_table.data == [], "The data attribute should be an empty list for an empty DataFrame."

def test_convert_df_to_dash_non_empty_dataframe():
    """
    Test converting a non-empty Polars DataFrame to a Dash DataTable.
    """
    # Create a non-empty Polars DataFrame
    df = pl.DataFrame({
        "column1": [1, 2, 3],
        "column2": ["a", "b", "c"]
    })
    
    # Convert the DataFrame to Dash DataTable
    dash_table = convert_df_to_dash(df)
    
    # Expected data format for Dash DataTable
    expected_data = [
        {"column1": 1, "column2": "a"},
        {"column1": 2, "column2": "b"},
        {"column1": 3, "column2": "c"}
    ]
    
    # Check if the conversion results in the correct data attribute
    assert dash_table.data == expected_data, "The data attribute should match the expected list of dictionaries."