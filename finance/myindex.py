from dash import html, dcc
import dash
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

from app import *
from components import sidebar, extratos, dashboards




# =========  Layout  =========== #
content = html.Div(id="page-content")


app.layout = dbc.Container(children=[
    dbc.Row([
        dbc.Col([
            dcc.Location(id="url"),
            sidebar.layout
        ], md=2, style={"background-color": "", 'height': "1080px", 'padding': '0px'}),
        dbc.Col([
            content
        ], md=10, style={"background-color": "", 'height': "1080px", 'padding': '0px'})
    ])
    
], fluid=True,)

@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/" or pathname == "/dashboard":
        return dashboards.layout
    if pathname == "/extratos":
        return extratos.layout


if __name__ == '__main__':
    app.run_server(port=8051, debug=True)