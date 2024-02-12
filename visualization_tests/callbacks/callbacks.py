## For callbacks used across multiple apps
import dash
from dash.dependencies import Input, Output, State
from utils.data_utils import reverse_text
from visualization_project.plots.visualization import specific_chart

import polars as pl
import plotly.express as px

def register_callbacks(app: dash.Dash) -> None:
    """
    Registers all callback functions necessary for the dashboard to interact with user inputs and updates the visualizations accordingly.
    """
    # Placeholder for callback functions.
    # For the purpose of this example, we'll create a dummy callback that does nothing.
    @app.callback(
        Output('dummy-output', 'children'),
        [Input('dummy-input', 'value')]
    )
    def update_output(value):
            return f"You have entered {value}"

    # Adding a new callback for reversing text in app2
    @app.callback(
        Output('output-2', 'children'),
        [Input('reverse-btn', 'n_clicks')],
        [State('input-2', 'value')]
    )
    def reversal(n_clicks, value):
        reverse_text(n_clicks, value)

def register_callbacks_visualization(app: dash.Dash) -> None:
    @app.callback(
        Output('plot', 'figure'),
        Input('file-dropdown', 'value')
    )
    def callback_update_figure(selected_file):
        return specific_chart(selected_file)
