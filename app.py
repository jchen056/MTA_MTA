import dash
from dash import html

app = dash.Dash(__name__)
app.layout = html.Div([
    html.Div(children='Hello World')
])

if __name__ == '__main__':
    app.server.run(debug=True)
