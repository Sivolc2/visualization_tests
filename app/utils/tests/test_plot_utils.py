import pytest
from unittest.mock import patch, MagicMock
import polars as pl
import plotly.graph_objects as go
from visualization_project.utils.plot_utils import create_bar_chart, create_line_chart, format_chart

# Sample data for testing
sample_data = pl.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6], "lat": [1, 2, 3], "lon": [4, 5, 6]})

@pytest.fixture
def mock_figure():
    with patch('plotly.graph_objects.Figure') as mock:
        yield mock

def test_create_bar_chart(mock_figure):
    """
    Test the creation of a bar chart.
    """
    fig = create_bar_chart(sample_data, "x", "y", "Test Bar Chart")
    assert fig is not None
    mock_figure.assert_called_once()

def test_create_line_chart(mock_figure):
    """
    Test the creation of a line chart.
    """
    fig = create_line_chart(sample_data, "x", "y", "Test Line Chart")
    assert fig is not None
    mock_figure.assert_called_once()

@patch('plotly.graph_objects.Figure.update_layout')
def test_format_chart(mock_update_layout):
    """
    Test formatting options applied to a figure.
    """
    fig = go.Figure()
    formatted_fig = format_chart(fig, {"title": "Formatted Chart"})
    assert formatted_fig is not None
    mock_update_layout.assert_called_once_with(title="Formatted Chart")
