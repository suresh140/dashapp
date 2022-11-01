from dash import Dash, dcc, html, Input, Output
import os
import plotly.graph_objects as go
import plotly.express as px


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 1, 2])])


app.layout = html.Div([
    html.H2('Hello World'),
    dcc.Graph(figure=fig)
])

@app.callback(Output('display-value', 'children'),
                [Input('dropdown', 'value')])
def display_value(value):
    return f'You have selected {value}'

if __name__ == '__main__':
    app.run_server(debug=True)
