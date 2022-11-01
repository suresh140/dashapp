
Suresh Vashdev Sharma <suresharma@eand.com>
12:44 PM (0 minutes ago)
to me

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import dash
from dash import dcc
from dash import html
from dash import Input
from dash import Output
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
from flask import Flask


server = Flask(__name__)
app = dash.Dash(
    __name__,
    server=server,
    url_base_pathname='/dash/'
)

fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 1, 2])])
app.layout = html.Div([dcc.Graph(figure=fig)])



@server.route("/dash")
def my_dash_app():
    return app.index()

if __name__ == "__main__":
    app.run(debug=True)
