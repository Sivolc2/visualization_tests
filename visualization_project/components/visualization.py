import plotly.graph_objects as go
import polars as pl
from typing import Dict

def create_bar_chart(data: pl.DataFrame, x_col: str, y_col: str, title: str) -> go.Figure:
    """
    Generates a bar chart with specified x and y columns from a Polars DataFrame.
    """
    fig = go.Figure(data=[go.Bar(x=data[x_col].to_list(), y=data[y_col].to_list())])
    fig.update_layout(title=title)
    return fig

def create_line_chart(data: pl.DataFrame, x_col: str, y_col: str, title: str) -> go.Figure:
    """
    Generates a line chart with specified x and y columns from a Polars DataFrame.
    """
    fig = go.Figure(data=[go.Scatter(x=data[x_col].to_list(), y=data[y_col].to_list(), mode='lines')])
    fig.update_layout(title=title)
    return fig

def format_chart(figure: go.Figure, layout_options: Dict[str, Any]) -> go.Figure:
    """
    Applies formatting options to a given Plotly figure.
    """
    figure.update_layout(**layout_options)
    return figure