import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from plotly.subplots import make_subplots
import json
db = pd.read_excel(r"data\uk annual growth rate by region(cleaned).xlsx",
                   sheet_name="Dataset"
                   )
with open(r'data\map.geojson', 'r') as myfile:
    data=myfile.read()

obj = json.loads(data)
fig1 = go.Figure()
fig1.update_layout(xaxis_title='Year',
                  yaxis_title='Annual growth(%)',
                  xaxis_type='category'
                  )
fig1.add_trace(go.Scatter(x=[2013,2014,2015,2016,2017,2018],y=db.iloc[1,1:],name=db.iloc[1,0]))
fig1.add_trace(go.Scatter(x=[2013,2014,2015,2016,2017,2018],y=db.iloc[2,1:],name=db.iloc[2,0]))
fig1.add_trace(go.Scatter(x=[2013,2014,2015,2016,2017,2018],y=db.iloc[3,1:],name=db.iloc[3,0]))
fig1.add_trace(go.Scatter(x=[2013,2014,2015,2016,2017,2018],y=db.iloc[4,1:],name=db.iloc[4,0]))
fig1.add_trace(go.Scatter(x=[2013,2014,2015,2016,2017,2018],y=db.iloc[5,1:],name=db.iloc[5,0]))
fig1.add_trace(go.Scatter(x=[2013,2014,2015,2016,2017,2018],y=db.iloc[6,1:],name=db.iloc[6,0]))
fig1.add_trace(go.Scatter(x=[2013,2014,2015,2016,2017,2018],y=db.iloc[7,1:],name=db.iloc[7,0]))
fig1.add_trace(go.Scatter(x=[2013,2014,2015,2016,2017,2018],y=db.iloc[8,1:],name=db.iloc[8,0]))
fig1.add_trace(go.Scatter(x=[2013,2014,2015,2016,2017,2018],y=db.iloc[9,1:],name=db.iloc[9,0]))

fig = px.choropleth_mapbox(db,
                           geojson=obj,
                           color="2013",
                           locations="Geography",
                           featureidkey="properties.name",
                           center={"lat": 54.560886, "lon": -2.2125118},
                           mapbox_style="carto-positron",
                           zoom=5
                           )





app = dash.Dash(__name__)
server = app.server
app.layout = html.Div([
    html.Div([
        html.H1("UK ANNUAL GROWTH BY REGION 2013-2018"),
        html.H2("Choropleth Map of England and Wales",id="geotitle"),
        dcc.Graph(id="geo",figure=fig),
        dcc.Slider(id="slider",
                   min=2013,
                   max=2018,
                   step=1,
                   marks={2013:{'label':'2013'},
                          2014:{'label':'2014'},
                          2015:{'label':'2015'},
                          2016:{'label':'2016'},
                          2017:{'label':'2017'},
                          2018:{'label':'2018'}},
                   value=2013,
                   updatemode='drag')]),
    html.Div([
        html.H2("Time Series Graph",id="times"),
        dcc.Graph(id="Line",figure=fig1),
        dcc.Dropdown(id="dropdown",
                     options=[
                         {'label': db.iloc[1,0], 'value': db.iloc[1,0]},
                         {'label': db.iloc[2,0], 'value': db.iloc[2,0]},
                         {'label': db.iloc[3,0], 'value': db.iloc[3,0]},
                         {'label': db.iloc[4,0], 'value': db.iloc[4,0]},
                         {'label': db.iloc[5,0], 'value': db.iloc[5,0]},
                         {'label': db.iloc[6,0], 'value': db.iloc[6,0]},
                         {'label': db.iloc[7,0], 'value': db.iloc[7,0]},
                         {'label': db.iloc[8,0], 'value': db.iloc[8,0]},
                         {'label': db.iloc[9,0], 'value': db.iloc[9,0]},
                         ],
                     value=(db.iloc[1,0],
                            db.iloc[2,0],
                            db.iloc[3,0],
                            db.iloc[4,0],
                            db.iloc[5,0],
                            db.iloc[6,0],
                            db.iloc[7,0],
                            db.iloc[8,0],
                            db.iloc[9,0]),
                     multi=True)])
    ])

@app.callback(Output(component_id='geo',component_property='figure'),
            [Input(component_id='slider',component_property='value')]
             )


def update_figure(value):
    fig = px.choropleth_mapbox(db,
                           geojson=obj,
                           color=str(value),
                           locations="Geography",
                           featureidkey="properties.name",
                           center={"lat": 54.560886, "lon": -2.2125118},
                           mapbox_style="carto-positron",
                           zoom=5
                           )
    return fig

@app.callback(Output(component_id='Line',component_property='figure'),
            [Input(component_id='dropdown',component_property='value')]
               )

def update1_figure(value1):
    fig1 = go.Figure()
    fig1.update_layout(xaxis_title='Year',
                       yaxis_title='Annual growth(%)',
                       xaxis_type='category'
                       )
    for a in range(1,10):
        if db.iloc[a,0] in value1:
            fig1.add_trace(go.Scatter(x=[2013,2014,2015,2016,2017,2018],y=db.iloc[a,1:],name=db.iloc[a,0]))
        else:
            continue
    return fig1
  
        
    
    

                
if __name__ == '__main__':
    app.run_server(debug=False)





