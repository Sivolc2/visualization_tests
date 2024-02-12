import dash
from dash import html

dash.register_page(
    __name__, 
    name='Home', 
    top_nav=True, 
    path='/'
)

def layout():
    layout = html.Div([
        html.H1(
            [
                "Home Page: The Shire"
            ]
        )
    ])
    return layout

