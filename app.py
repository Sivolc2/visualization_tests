import dash
import dash_core_components as dcc
import dash_html_components as html
from callbacks import register_callbacks

app = dash.Dash(__name__)

app.layout = html.Div([
    # Placeholder for actual layout components.
    # For the purpose of this example, we'll create a dummy input and output.
    dcc.Input(id='dummy-input', type='text', value=''),
    html.Div(id='dummy-output')
])

register_callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)