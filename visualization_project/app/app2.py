import dash_html_components as html
import dash_core_components as dcc

# Define your layout here
layout = html.Div([
    html.H3('App 2: Reverse Text'),
    dcc.Input(id='input-2', type='text', value='', placeholder='Enter text to reverse'),
    html.Button('Reverse', id='reverse-btn'),
    html.Div(id='output-2', style={'marginTop': 20})
])

# Callbacks for app2 should be defined in the main app.py or a separate callbacks file
# to interact with this layout, such as reversing the input text when the button is clicked.