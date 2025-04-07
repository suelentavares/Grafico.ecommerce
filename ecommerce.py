import pandas as pd
from dash import Dash,dcc,html
import plotly.express as px

# ler arquivo csv
df = pd.read_csv('C:\Users\SUELEN TAVARES\PycharmProjects\CursoPycharm\ecommerce_estatistica.csv')

# criar aplicação dash
app = Dash(__nome__)


# criar um grafico em plotly
fig = px.line(df, x='data', y='vendas', title='vendas ao lngo do tempo')

# criar uma aplicação
app.layout = html.Div(children=[
    html.H1(children='dashboard de E-ecommerce'),
    dcc.Graph(
        id= 'grafico -vendas',
        figure=fig
    )
])

# executar a aplicação
if __nome__ == '__main__':
    app.run_server(debug=True)
