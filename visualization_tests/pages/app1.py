from dash import html, callback, Input, Output, State, register_page, dcc


register_page(
    __name__,
    top_nav=True,
    path='/app1'
)

layout = html.Div([
    html.Div(dcc.Input(id='input-on-submit', type='text', value='')),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Div(id='container-button-basic',
             children='Enter a value and press submit')
])


@callback(
    Output('container-button-basic', 'children'),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value'),
    prevent_initial_call=True
)
def update_output(n_clicks, value):
    return 'The input value was "{}" and the button has been clicked {} times'.format(
        value,
        n_clicks
    )