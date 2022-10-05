import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

def render_tab(df):

    crimes['week_day'] = crimes['date'].dt.day_name()
    grouped = df[df['Store_type']>0].groupby('prod_cat')['total_amt'].sum()
    fig = go.Figure(data=[go.Pie(labels=grouped.index,values=grouped.values)],layout=go.Layout(title='Udzial grup produktow w sprzedazy'))

    layout = html.Div([html.H1('Kanal Sprzedazy',style={'text-align':'center'}),

                        html.Div([html.Div([dcc.Graph(id='pie-prod-cat',figure=fig)],style={'width':'50%'}),
                        html.Div([dcc.Dropdown(id='prod_dropdown',
                                    options=[{'label':prod_cat,'value':prod_cat} for prod_cat in df['prod_cat'].unique()],
                                    value=df['prod_cat'].unique()[0]),
                                    dcc.Graph(id='barh-prod-subcat')],style={'width':'50%'})],style={'display':'flex'}),
                                    html.Div(id='temp-out')
                        ])

    return layout