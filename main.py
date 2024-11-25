import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from click import style
from dash.dependencies import Input, Output
import plotly.graph_objects as go
from PIL import Image

app = dash.Dash(__name__)
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
logo = Image.open('assets/images/i.png')

app.layout = html.Div(children=[
    html.Div(
        children=[
            html.H1(children='Мониторинг министерства', className= 'header-emoji'),
            html.P(children='Демография', className='header-description')
        ], className='header'),
    
    html.Div([
        html.Img(src=logo, className='logo')
    ]),
    html.Div([
        html.H2('Выберите Регион:',className= 'H2_position'),
        dcc.Dropdown(
            id='demo_drop',
            options=[
                {'label': 'Москва', 'value': '1'},
                {'label': 'Санкт-Петербург', 'value': '2'},
                {'label': 'Краснодарский Край', 'value': '3'}
            ],
            value='cut', className="dropdown"
        ),
        dcc.Graph(id='graf', className='graf_position')
    ]),
    html.Div([
       html.H2('Тут будет выводиться текст', className='H2_txt_position', id= 'Text') 
    ]),
    html.Div([
        html.H2('Выберите Показатель:', className='H2_2_position'),
        dcc.Dropdown(
            id= 'demo_drop_2',
            options=[
                {'label': 'Эмиграция', 'value': '1'},
                {'label': 'Браки', 'value': '2'},
                {'label': 'Разводы', 'value': '3'},
                {'label': 'Рождаемость', 'value': '4'},
                {'label': 'Смертность', 'value': '5'}
            ],
            value='cut', className="dropdown2"), dcc.Graph(id= 'graf_2', className= 'graf2_position')]),
    html.Div([
        html.H2('Решения', className= 'answer')
    ])
])
@app.callback(
    Output(component_id='graf', component_property='figure'),
    [Input(component_id='demo_drop', component_property='value')]
)
def update_output(value):
    if value == '3':
        labels = ['Эмиграция', 'Браки', 'Разводы', 'Рождаемость', 'Смертность','Зарплата','Стоимость жилья']
        values = [2500, 1200, 670, 1001, 302, 400, 650]
    elif value == '2':
        labels = ['Эмиграция', 'Браки', 'Разводы', 'Рождаемость', 'Смертность']
        values = [4000, 2100, 589, 1889, 301]

    elif value == '1':
        labels = ['Эмиграция', 'Браки', 'Разводы', 'Рождаемость', 'Смертность']
        values = [5000, 2500, 429, 1890, 213]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.4 )])
    fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=10,
                      marker=dict(line=dict(color='#000000', width=1)))
    return fig

@app.callback(
    Output(component_id='graf_2', component_property='figure'),
    [Input(component_id='demo_drop_2', component_property='value')]
)

def update_output_hist(value):
    if value == '1':
        x = ["Эмиграция 2000год", "Эмиграция 2010 год", 'Эмиграция 2020 год']
        y = ['120', '214', '300']
    elif value == '2':
        x = ['Браки 2000', 'Браки 2010', 'Браки 2020']
        y = ['257', '180','220']
    elif value == '3':
        x = ['Разводы 2000', 'Разводы 2010', 'Разводы 2020']
        y = ['100', '133', '210']
    elif value == '4':
        x = ['Рождаемость 2000', 'Рождаемость 2010', 'Рождаемость 2020']
        y = ['257', '240', '120']
    elif value == '5':
        x = ['Смертность 2000', 'Смертность 2010', 'Смертность 2020']
        y = ['220', '140', '92']

    fig_2 = px.histogram(x=x, y=y, category_orders=dict(day=x))
    return fig_2

if __name__ == '__main__':
   app.run_server(debug=True) # Run the Dash apph app

'''@app.callback(
    Output('slider-output-container', 'children'),
    Input('my-slider', 'value')
)
def update_output(value):
    return 'Вы выбпали "{}"'.format(value)'''
