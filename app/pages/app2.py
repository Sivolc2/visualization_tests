from dash import html, dcc, callback, Input, Output, State, register_page

register_page(
    __name__,
    top_nav=True,
    path='/app2'
)
# Define the layout for this page
layout = html.Div([
    html.H1('App 2 Page'),
    html.Div("This is a simple example for App 2."),
    html.Div([
        html.Label("Input Text: "),
        html.Div(id='app2-output'),
        html.Br(),
        dcc.Input(id='app2-input', type='text', value=''),  # Set value to '' to make it controlled from the start
        html.Button('Submit', id='app2-submit'),
    ])
])

# Define any callbacks specific to this page
@callback(
    Output('app2-output', 'children'),
    Input('app2-submit', 'n_clicks'),
    State('app2-input', 'value'),
    prevent_initial_call=True
)
def update_output(n_clicks, input_value):
    if n_clicks:
        return f'You entered: {input_value}'
    return 'Enter something and click submit.'