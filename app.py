from dash import Dash, dcc, html, Input, Output
import os
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 1, 2])])
fig.update_layout(legend=dict(title_text = "Churn Dashboard", yanchor='top',y=1.1, xanchor="right",x=0.99,title=dict(x=0.5))




app.layout = html.Div([
    html.H2('Hello World'),
    dcc.Dropdown(['LA','NYV','MTL'],'LA', id= 'dropdown'),
    html.Div(id='display-value'),
    dcc.Graph(figure=fig)
])

@app.callback(Output('display-value', 'children'),
                [Input('dropdown', 'value')])
def display_value(value):
    return f'You have selected {value}'

if __name__ == '__main__':
    app.run_server(debug=True)
