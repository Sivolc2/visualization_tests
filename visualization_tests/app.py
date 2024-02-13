from dash import Dash, html, dcc, Input, Output, page_registry, page_container
import dash_bootstrap_components as dbc
from visualization_tests.components.navbar import create_navbar
import os
from flask import Flask, send_from_directory
from keplergl import KeplerGl

NAVBAR = create_navbar()
# To use Font Awesome Icons
FA621 = "https://use.fontawesome.com/releases/v6.2.1/css/all.css"
APP_TITLE = "My Dash App"

kepler_map = KeplerGl(height=800)
## kepler_map.add_data(data=df, name='geodata')

## config= {} # can save map setup
kepler_map.save_to_html(file_name='assets/keplergl_map.html')

app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[
        dbc.themes.LUX,  # Dash Themes CSS
        FA621,  # Font Awesome Icons CSS
    ],
    title=APP_TITLE,
    use_pages=True,  # New in Dash 2.7 - Allows us to register pages
)

app.layout = dcc.Loading(  # <- Wrap App with Loading Component
    id='loading_page_content',
    children=[
        html.Div(
            [
                NAVBAR,
                page_container
            ]
        )
    ],
    color='primary',  # <- Color of the loading spinner
)

server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)
