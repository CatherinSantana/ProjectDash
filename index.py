import dash
import dash_core_components as dcc 
import dash_html_components as html
import plotly.express as px
import pandas as pd 
from dash.dependencies import Input,Output

df = pd.read_csv('Covid19PacientesAgrupados.csv')
#print(df)
#print(df.dia_semana.nunique())

app = dash.Dash(__name__)

app.layout = html.Div([
    
    html.Div([
        html.H1('Ocupación de Camas UCI IESS-MANTA Durante los Meses de Abril y Mayo 2019'),
        html.Img(src='assets/pctscovid.jpg')
    ], className = 'banner'),

    html.Div([
        html.Div([
            html.P('Covid-19. Selecciona tu busqueda', className = 'fix_label', style={'color':'black', 'margin-top': '2px'}),
            dcc.RadioItems(id = 'dosis-radioitems', 
                            labelStyle = {'display': 'inline-block'},
                            options = [
                                {'label' : 'Pacientes atendidos', 'value' : 'pacientes_atendidos'},
                                {'label' : 'Pacientes No atendidos', 'value' : 'pacientes_no_atendidos'}
                            ], value = 'pacientes_atendidos',
                            style = {'text-aling':'center', 'color':'black'}, className = 'dcc_compon'),
        ], className = 'create_container2 five columns', style = {'margin-bottom': '20px'}),
    ], className = 'row flex-display'),

    html.Div([
        html.Div([
            dcc.Graph(id = 'my_graph', figure = {})
        ], className = 'create_container2 eight columns'),

        html.Div([
            dcc.Graph(id = 'pie_graph', figure = {})
        ], className = 'create_container2 five columns')
    ], className = 'row flex-display'),

], id='mainContainer', style={'display':'flex', 'flex-direction':'column'})

@app.callback(
    Output('my_graph', component_property='figure'),
    [Input('dosis-radioitems', component_property='value')])

def update_graph(value):

    if value == 'pacientes_atendidos':
        fig = px.bar(
            data_frame = df,
            x = 'dia_atencion',
            y = 'pacientes_atendidos')
    else:
        fig = px.bar(
            data_frame= df,
            x = 'dia_atencion',
            y = 'pacientes_no_atendidos')
    return fig

@app.callback(
    Output('pie_graph', component_property='figure'),
    [Input('dosis-radioitems', component_property='value')])

def update_graph_pie(value):

    if value == 'pacientes_atendidos':
        fig2 = px.pie(
            data_frame = df,
            names = 'dia_atencion',
            values = 'pacientes_atendidos')
    else:
        fig2 = px.pie(
            data_frame = df,
            names = 'dia_atencion',
            values = 'pacientes_no_atendidos'
        )
    return fig2

if __name__ == ('__main__'):
    app.run_server(port=5050)
