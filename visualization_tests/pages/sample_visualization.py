import pandas as pd
import plotly.express as px
from dash import html, dcc, Input, Output, callback, register_page

from keplergl import KeplerGl


register_page(
    __name__,
    top_nav=True,
    path='/sample_vis'
)

# Initial Plot
initial_fig = px.line(title='Select a file to display data')

# Assuming you have public AWS S3 links
aws_s3_links = [
    'https://s3.amazonaws.com/yourbucket/geospatial.csv',
    # Add other AWS S3 links here as needed
]

# Update the dropdown to use AWS S3 links
layout = html.Div([
    html.H1('Plotting Value A'),
    dcc.Dropdown(
        id='file-dropdown',
        options=[{'label': link.split('/')[-1], 'value': link} for link in aws_s3_links],
        value=aws_s3_links[0]  # Default value or None
    ),
    dcc.Graph(id='plot', figure=initial_fig),
    html.Iframe(
        id="keplergl_map",
        src="/assets/keplergl_map.html",
        width="100%",
        height="500px"
    )
])

