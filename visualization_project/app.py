import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from apps.app1 import layout as app1_layout
from apps.app2 import layout as app2_layout
from callbacks import register_callbacks

app = dash.Dash(__name__)

# Define a simple layout with a dropdown to switch between apps
app.layout = html.Div([
    dcc.Dropdown(
        id='app-selector',
        options=[
            {'label': 'App 1', 'value': 'app1'},
            {'label': 'App 2', 'value': 'app2'}
        ],
        value='app1'  # Default value
    ),
    html.Div(id='app-content')
])

@app.callback(
    Output('app-content', 'children'),
    [Input('app-selector', 'value')]
)
def display_app(selected_app):
    if selected_app == 'app1':
        return app1_layout
    elif selected_app == 'app2':
        return app2_layout
    else:
        return "Please select an app"

register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)
