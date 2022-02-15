import altair as alt
from vega_datasets import data
alt.data_transformers.enable('data_server')
alt.renderers.enable('mimetype')
from dash import Dash, dcc, html, Input, Output
import pandas as pd
import numpy as np

data = pd.read_csv("vgsales.csv")

def plot_altair(genre):
    chart = alt.Chart(data[data['Genre']==genre], title=f"Mean Global Sales {genre}").mark_line(color='red').encode(
    x='Year',
    y=alt.Y('mean(Global_Sales)',title="Mean Global Sales"))
    return chart.to_html()

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server

app.layout = html.Div([
    html.H1(children='Visualization of Video Game sales', style={'font-size': "260%", 'color':'#660000'}),
    html.Br(),
    html.Br(),
    html.Br(),


        html.Iframe(
            id='line',
            style={'border-width': '0', 'width': '200%', 'height': '400px'},
            srcDoc=plot_altair(genre='Sports')),
            html.Div(children='''
            Please select Genre of Video Game
            ''', style={'color':'#660000'}),
            dcc.Dropdown(
            id='genre', value='Sports',
            options=[{'label': i, 'value': i} for i in data['Genre'].unique()],
            style={'height': '30px', 'width': '200px'})])

@app.callback(
    Output('line', 'srcDoc'),
    Input('genre', 'value'))

def update_output(genre):
    return plot_altair(genre)

if __name__ == '__main__':
    app.run_server(debug=True)