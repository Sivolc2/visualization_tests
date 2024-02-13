import plotly.graph_objects as go
import polars as pl
from typing import Dict

import plotly.express as px


from visualization_tests.utils.plot_utils import create_bar_chart

def specific_chart(selected_file):
    '''
    Specific chart for lat/lon plot on dynamic dataset
    '''
    if selected_file is None:
        return px.bar(title='Select a file to display data')
    # Convert pandas DataFrame to Polars DataFrame
    pl_df = pl.read_csv(selected_file)
    fig = create_bar_chart(pl_df, x_col='lat', y_col='lon', title=f'Value A from {selected_file}')
    return fig
