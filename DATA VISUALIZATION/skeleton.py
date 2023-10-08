#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Load the data using pandas
data = pd.read_csv(r'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv')

# Initialize the Dash app
app = dash.Dash(__name__)

# Set the title of the dashboard
#app.title = "Automobile Statistics Dashboard"

#---------------------------------------------------------------------------------
# Create the dropdown menu options
dropdown_options = [
    {'label': '...........', 'value': 'Yearly Statistics'},
    {'label': 'Recession Period Statistics', 'value': '.........'}
]
# List of years 
year_list = [i for i in range(1980, 2024, 1)]
#---------------------------------------------------------------------------------------
# Create the layout of the app
app.layout = html.Div([
    #TASK 2.1 Add title to the dashboard
    html.H1("..............."),#May include style for title
    html.Div([#TASK 2.2: Add two dropdown menus
        html.Label("Select Statistics:"),
        dcc.Dropdown(
            id='...........',
            options=...................,
            value='.................',
            placeholder='.................'
        )
    ]),
    html.Div(dcc.Dropdown(
            id='select-year',
            options=[{'label': i, 'value': i} for i in year_list],
            value='...................'
        )),
    html.Div([#TASK 2.3: Add a division for output display
    html.Div(id='..........', className='..........', style={.........}),])
])
#TASK 2.4: Creating Callbacks
# Define the callback function to update the input container based on the selected statistics
@app.callback(
    Output(component_id='......', component_property='....'),
    Input(component_id='..........',component_property='....'))

def update_input_container(.......):
    if selected_statistics =='........': 
        return False
    else: 
        return ......

#Callback for plotting
# Define the callback function to update the input container based on the selected statistics
@app.callback(
    Output(component_id='...', component_property='...'),
    [Input(component_id='...', component_property='...'), Input(component_id='...', component_property='...')])


def update_output_container(....., .....):
    if ..... == 'Recession Period Statistics':
        # Filter the data for recession periods
        recession_data = data[data['Recession'] == 1]
        
#TASK 2.5: Create and display graphs for Recession Report Statistics

#Plot 1 Automobile sales fluctuate over Recession Period (year wise)
        # use groupby to create relevant data for plotting
        yearly_rec=recession_data.groupby('...')['...'].mean().reset_index()
        R_chart1 = dcc.Graph(
            figure=px......(....., 
                x='....',
                y='......',
                title="Average Automobile Sales fluctuation over Recession Period"))

#Plot 2 Calculate the average number of vehicles sold by vehicle type       
        # use groupby to create relevant data for plotting
        average_sales = ...............mean().reset_index()                           
        R_chart2  = dcc.Graph(figure=px....................
        
# Plot 3 Pie chart for total expenditure share by vehicle type during recessions
        # use groupby to create relevant data for plotting
        exp_rec= ....................
        R_chart3 = .............

# Plot 4 bar chart for the effect of unemployment rate on vehicle type and sales
        ................
        ...................


        return [
            html.Div(className='..........', children=[html.Div(children=R_chart1),html.Div(children=.....)],style={.....}),
            html.Div(className='chart-item', children=[html.Div(children=...........),html.Div(.............)],style={....})
            ]

# TASK 2.6: Create and display graphs for Yearly Report Statistics
 # Yearly Statistic Report Plots                             
    elif (input_year and selected_statistics=='...............') :
        yearly_data = data[data['Year'] == ......]
                              
#TASK 2.5: Creating Graphs Yearly data
                              
#plot 1 Yearly Automobile sales using line chart for the whole period.
        yas= data.groupby('Year')['Automobile_Sales'].mean().reset_index()
        Y_chart1 = dcc.Graph(figure=px.line(.................))
            
# Plot 2 Total Monthly Automobile sales using line chart.
        Y_chart2 = dcc.Graph(................)

            # Plot bar chart for average number of vehicles sold during the given year
        avr_vdata=yearly_data.groupby........................
        Y_chart3 = dcc.Graph( figure.................,title='Average Vehicles Sold by Vehicle Type in the year {}'.format(input_year)))

            # Total Advertisement Expenditure for each vehicle using pie chart
        exp_data=yearly_data.groupby(..................
        Y_chart4 = dcc.Graph(...............)

#TASK 2.6: Returning the graphs for displaying Yearly data
        return [
                html.Div(className='.........', children=[html.Div(....,html.Div(....)],style={...}),
                html.Div(className='.........', children=[html.Div(....),html.Div(....)],style={...})
                ]
        
    else:
        return None

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)


# %%
