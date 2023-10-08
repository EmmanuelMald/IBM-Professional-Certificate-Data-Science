
import pandas as pd
import plotly.express as px
import numpy as np
from dash import Dash, html, dcc, Input, Output, callback


URL = r"https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"

df=pd.read_csv(URL)





app=Dash(__name__)

app.layout = html.Div(
        
        children=[
                html.H1("Automobile Sales Statistics Dashboard",
                        style = {
                                    "textAlign":"center",
                                    "color":"#503D36",
                                    "font-size":24
                                }
                        ),
                dcc.Dropdown(
                                options=[
                                        
                                        {"label":"Yearly Statistics", "value": "Yearly Statistics"},
                                        {"label" :"Recession Period Statistics", "value" : "Recession Period Statistics"}
                                        
                                        ],
                                id = "dropdown-statistics",
                                placeholder="Select a report type", # what it will be shown as the title of the dropdown
                                value="Recession Period Statistics" #default value
                            ),
                dcc.Dropdown(
                                   
                                options = [{"label":i, "value":i} for i in [x for x in range(1980,2014,1)]],
                                id = 'select-year',
                                placeholder = "Select a year"        
                            ),
                
                html.Div([
                                html.Div(id='output-container', className='chart-grid', style={'display': 'flex'})
                        ])
                ]
                
        )
               
                
@callback(
         Output(component_id = 'select-year', component_property = "disabled"),
         Input(component_id = "dropdown-statistics", component_property = "value")
 )               
def update_input_container(input_value):
         if input_value == "Yearly Statistics":
                 return False
         else:
                return True

@callback(
        Output(component_id = "output-container", component_property="children"),
        [Input(component_id = "select-year", component_property="value"),
         Input(component_id="dropdown-statistics", component_property="value")
         ]
)
def update_output_container(selected_year,selected_report):
        if selected_report == "Recession Period Statistics":
                data = df[df.Recession == 1]
        
                #Plot 1: Automobile Sales fluctuate over Recession Period (year wise) using line chart 
                # grouping data fro plotting
                yearly_rec = data.groupby("Year", as_index=False)["Automobile_Sales"].mean()  
                
                R_chart1 = dcc.Graph(
                        
                        figure=px.line(yearly_rec, x="Year", y="Automobile_Sales", title="Mean Automobile Sales")
                )
                
                #Plot 2: Calculate the average number of vehicles sold by vehicle type and represent as a bar chart
                
                car_types = data.groupby("Vehicle_Type", as_index=False)["Automobile_Sales"].mean()
                
                R_chart2 = dcc.Graph(
                        figure = px.bar(data_frame=car_types, x = "Vehicle_Type", y = "Automobile_Sales", title = "Average number of vehicles sold by vehicle type")
                )            

                #Plot 3: Pie chart for total expenditure share by vehicle type during recessions
                
                exp_rec = data.groupby("Vehicle_Type", as_index=False)["Advertising_Expenditure"].sum()
                R_chart3 = dcc.Graph(
                        figure = px.pie(exp_rec, values = "Advertising_Expenditure", names = "Vehicle_Type", title = "Total expenditure share by vehicle type")
                )
                
                #Plot 4: Develop a bar chart for the effect of unemployment rate on vehicle type and sales
                R_chart4 = dcc.Graph(
                        figure=px.histogram(data,
                        x='unemployment_rate',
                        color= 'Vehicle_Type',
                        barmode='group',
                        title= 'Effect of Unemployment Rate on Vehicle Type and Sales'
                        ))


                return [
                html.Div(className='chart-item', 
                children=[html.Div(children=[R_chart1,R_chart3]),
                html.Div(children=[R_chart2,R_chart4])],
                style={'display':'flex'})          
                ]
        
                
                 
        elif (selected_year and selected_report=='Yearly Statistics') :
                data = df[df.Year == int(selected_year)]
         
                #plot 1 Yearly Automobile sales using line chart for the whole period.
                yas= data.groupby(data['Year'])['Automobile_Sales'].mean().reset_index()
                Y_chart1 = dcc.Graph(figure=px.line(data, 
                                x='Year', 
                                y='Automobile_Sales',
                                title= 'Average Yearly Automobile Sales'))
                
        # Plot 2 Total Monthly Automobile sales using line chart.
                Y_chart2 = dcc.Graph(figure=px.line(data,
                                x= 'Month', 
                                y='Automobile_Sales',
                                title= f'Total Monthly Automobile Sales in the Year {selected_year}')
                                     )

        # Plot bar chart for average number of vehicles sold during the given year
                avr_vdata=data.groupby(['Year','Vehicle_Type'])['Automobile_Sales'].mean().reset_index()
                Y_chart3 = dcc.Graph(figure=px.bar(avr_vdata,
                        x='Year',
                        y="Automobile_Sales",
                        color= 'Vehicle_Type',
                        barmode='group',
                        title='Average Vehicles Sold by Vehicle Type in the Year {}'.format(selected_year)))
                        
        # Total Advertisement Expenditure for each vehicle using pie chart
                exp_data=data.groupby(data['Vehicle_Type'])['Advertising_Expenditure'].sum().reset_index()
                Y_chart4 = dcc.Graph(figure=px.pie(exp_data, 
                                values = 'Advertising_Expenditure', 
                                names='Vehicle_Type',
                                title = 'Total Advertisement Expenditure by Vehicle Type in the Year {}'.format(selected_year)))

        #TASK 2.6: Returning the graphs for displaying Yearly data

                return [
                html.Div(className='chart-item', 
                children=[html.Div(children=[Y_chart1,Y_chart3]),
                html.Div(children=[Y_chart2,Y_chart4])],
                style={'display':'flex'})           
                ]
        
        else:
                return None       
        
        



if __name__ == '__main__': # Ctrl + C to exit the dashboard
    app.run_server(debug=True)


