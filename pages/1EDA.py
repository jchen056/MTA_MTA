import pandas as pd
import numpy as np
import streamlit as st
from datetime import datetime
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import calendar
import streamlit.components.v1 as components
from PIL import Image
from base64 import b64encode

st.header("Exploratory Data Analysis")
# @st.cache_data
# def read_csv(path="Data/MTA_Subway_Hourly_Ridership__Beginning_February_2022.csv"):
#     return pd.read_csv(path)


# hourly_data = read_csv()
# hourly_data["datetime"] = hourly_data["transit_timestamp"].apply(
#     lambda x: datetime.strptime(x, "%m/%d/%Y %I:%M:%S %p"))
# hourly_data["hour"] = hourly_data["datetime"].apply(lambda x: x.hour)
# hourly_data['month'] = hourly_data["datetime"].apply(lambda x: x.month)
# hourly_data['date']=hourly_data['datetime'].apply(lambda x: datetime(x.year, x.month, x.day))
# hourly_data["weekdays"] = hourly_data["datetime"].apply(lambda x: x.weekday())

# hourly_data_avg_ridership_per_hr=hourly_data.groupby(
#     "hour")['ridership'].agg(['mean','std']).reset_index()
# avg_ridership_75_quantile=hourly_data_avg_ridership_per_hr["mean"].quantile(0.75)
# hourly_data_avg_ridership_per_hr['color']=np.where(hourly_data_avg_ridership_per_hr['mean']>avg_ridership_75_quantile,
#                                                   "orange","blue")

# hourly_data_total_ridership = hourly_data.groupby(
#     "hour")['ridership'].sum().reset_index()
# hourly_data_total_ridership.rename(
#     columns={'ridership': "total ridership"}, inplace=True)
# hourly_data_total_ridership['color']=np.where(
#     hourly_data_total_ridership['total ridership']>hourly_data_total_ridership['total ridership'].quantile(0.75),
#     'crimson','lightslategray')


# hourly_data_avg_ridership_days = hourly_data.groupby(
#     "weekdays")['ridership'].agg(['mean','std']).reset_index()
# hourly_data_avg_ridership_days['weekdays'] = hourly_data_avg_ridership_days['weekdays'].apply(
#     lambda x: calendar.day_name[x])

# hourly_data_total_ridership_days = hourly_data.groupby(
#     "weekdays")['ridership'].sum().reset_index()
# hourly_data_total_ridership_days.rename(
#     columns={'ridership': "total ridership"}, inplace=True)
# hourly_data_total_ridership_days['weekdays'] = hourly_data_total_ridership_days['weekdays'].apply(
#     lambda x: calendar.day_name[x])


# datapoints_count_hr=hourly_data.groupby(["hour"]).size().reset_index()
# datapoints_count_hr.rename(columns={0:"Data Count"},inplace=True)
# datapoints_count_days=hourly_data.groupby("weekdays").size().reset_index()
# datapoints_count_days.rename(columns={0:"Data Count"},inplace=True)
# datapoints_count_days['weekdays'] = datapoints_count_days['weekdays'].apply(
#     lambda x: calendar.day_name[x])

# hr_data_1yr=hourly_data[(hourly_data['datetime']>=datetime(2022,4,1)) & (hourly_data['datetime']<datetime(2023,4,1))]
# datapoints_count_month=hr_data_1yr.groupby('month').size().reset_index()
# datapoints_count_month.rename(columns={0:"Data Count"},inplace=True)
# hourly_data_avg_ridership_month=hr_data_1yr.groupby('month')['ridership'].agg(['mean','std']).reset_index()
# hourly_data_avg_ridership_month['color']=np.where(
#     hourly_data_avg_ridership_month['mean']>hourly_data_avg_ridership_month['mean'].quantile(0.75),
#     'magenta','lightgreen')
# hourly_data_total_ridership_month=hr_data_1yr.groupby('month')['ridership'].sum().reset_index()
# hourly_data_total_ridership_month.rename(
#     columns={'ridership': "total ridership"}, inplace=True)
# hourly_data_total_ridership_month['color']=np.where(
# hourly_data_total_ridership_month['total ridership']>hourly_data_total_ridership_month['total ridership'].quantile(0.75),
# 'yellow','goldenrod')
# fig = make_subplots(
#     rows=3, cols=3,
#     subplot_titles=("Data Count by Hours","Average Hourly Ridership","Total Hourly Ridership",
#                     "Data Count by Days", "Average Hourly Ridership","Total Hourly Ridership",
#                    'Data Count by Months',"Average Hourly Ridership","Total Hourly Ridership"))

# fig.add_trace(go.Bar(x=datapoints_count_hr['hour'],
#                     y=datapoints_count_hr['Data Count'],
#                      showlegend=False
#                     ),row=1,col=1)
# fig.update_xaxes(title_text="Hours",row=1,col=1)

# fig.add_trace(go.Bar(x=hourly_data_avg_ridership_per_hr['hour'],
#                     y=hourly_data_avg_ridership_per_hr['mean'],
#                     error_y=dict(type='data',array=hourly_data_avg_ridership_per_hr['std'].to_list()),
#                       marker=dict(color=hourly_data_avg_ridership_per_hr['color']),
#                      showlegend=False
#                     ),row=1,col=2)
# fig.update_xaxes(title_text="Hours",row=1,col=2)

# fig.add_trace(go.Bar(x=hourly_data_total_ridership.hour,
#                      y=hourly_data_total_ridership["total ridership"],
#                     marker=dict(color=hourly_data_total_ridership['color']),
#                     showlegend=False),
#               row=1, col=3)
# fig.update_xaxes(title_text="Hours",row=1,col=3)

# fig.add_trace(go.Bar(y=datapoints_count_days.weekdays,
#                     x=datapoints_count_days["Data Count"],
#                     orientation='h',
#                     showlegend=False),
#              row=2,col=1)
# fig.add_trace(go.Bar(y=hourly_data_avg_ridership_days.weekdays,
#                      x=hourly_data_avg_ridership_days["mean"],
#                       error_x=dict(type='data',array=hourly_data_avg_ridership_days['std'].to_list()),
#                      orientation='h',
#                      showlegend=False
#                     ),
#               row=2, col=2)
# # fig.update_yaxes(type='log',row=2,col=1)
# fig.add_trace(go.Bar(y=hourly_data_total_ridership_days.weekdays,
#                      x=hourly_data_total_ridership_days["total ridership"],
#                       orientation='h',
#                     showlegend=False),
#               row=2, col=3)
# fig.add_trace(go.Bar(x=datapoints_count_month.month,
#                     y=datapoints_count_month['Data Count'],
#                     showlegend=False),
#              row=3,col=1)
# fig.update_xaxes(title_text="Months (Apr 2022-Mar 2023)",row=3,col=1)
# fig.add_trace(go.Bar(x=hourly_data_avg_ridership_month['month'],
#                     y=hourly_data_avg_ridership_month['mean'],
#                     error_y=dict(type='data',array=hourly_data_avg_ridership_month['std'].to_list()),
#                      marker=dict(color=hourly_data_avg_ridership_month['color']),
#                      showlegend=False,
#                     ),
#              row=3,col=2)
# fig.update_xaxes(title_text="Months (Apr 2022-Mar 2023)",row=3,col=2)
# fig.add_trace(go.Bar(x=hourly_data_total_ridership_month['month'],
#                     y=hourly_data_total_ridership_month['total ridership'],
#                     showlegend=False,
#                     marker=dict(color=hourly_data_total_ridership_month['color'])),
#              row=3,col=3)
# fig.update_xaxes(title_text="Months (Apr 2022-Mar 2023)",row=3,col=3)
# fig.update_layout(height=1000, width=1000)
# fig.write_html("visualizations/time_visualizations.html")

# ridership_by_borough=hourly_data.groupby('borough')['ridership'].agg(['sum','mean',
#                                                                       'std','count'])
# top7_stations=hourly_data.groupby('station_complex')['ridership'].agg(['sum','mean',
#                     'std','count']).sort_values('mean',ascending=False).head(7)
# top7_stations.index=[station.split('(')[0][:-1] for station in top7_stations.index]
# bottom7_stations=hourly_data.groupby('station_complex')['ridership'].agg(['sum','mean',
#                     'std','count']).sort_values('mean',ascending=True).head(7)
# bottom7_stations.index=[station.split('(')[0][:-1] for station in bottom7_stations.index]

# fig = make_subplots(rows=3, cols=3,
#                     subplot_titles=("Data Count by Borough","Average Hourly Ridership","Total Hourly Ridership",
#                                    "Data Count by Stations","Average Hourly Ridership", "Total Hourly Ridership",
#                                    "Data Count by Stations","Average Hourly Ridership", "Total Hourly Ridership"))
# fig.add_trace(go.Bar(x=ridership_by_borough.index,
#                     y=ridership_by_borough['count'],
#                     showlegend=False),
#              row=1,col=1)
# # fig.update_yaxes(type='log',row=1,col=1)
# fig.add_trace(go.Bar(x=ridership_borough.index,
#                     y=ridership_by_borough['mean'],
#                     error_y=dict(type='data',array=ridership_by_borough['std'].to_list()),
#                     showlegend=False),
#                      row=1,col=2)
# fig.add_trace(go.Bar(x=ridership_by_borough.index,
#                     y=ridership_by_borough['sum'],
#                     showlegend=False),row=1,col=3)

# fig.add_trace(go.Bar(y=top7_stations.index,
#                     x=top7_stations["count"],
#                      orientation='h',
#                      showlegend=False),row=2,col=1)

# fig.add_trace(go.Bar(y=top7_stations.index,
#                     x=top7_stations["mean"],
#                      error_x=dict(type="data",array=top7_stations["std"].to_list()),
#                      orientation='h',
#                      showlegend=False),row=2,col=2)
# fig.update_yaxes(visible=False,row=2,col=2)

# fig.add_trace(go.Bar(y=top7_stations.index,
#                     x=top7_stations["sum"],
#                      orientation='h',
#                      showlegend=False),row=2,col=3)
# fig.update_yaxes(visible=False,row=2,col=3)


# fig.add_trace(go.Bar(y=bottom7_stations.index,
#                     x=bottom7_stations["count"],
#                      orientation='h',
#                      showlegend=False),row=3,col=1)

# fig.add_trace(go.Bar(y=bottom7_stations.index,
#                     x=bottom7_stations["mean"],
#                      error_x=dict(type="data",array=bottom7_stations["std"].to_list()),
#                      orientation='h',
#                      showlegend=False),row=3,col=2)
# fig.update_yaxes(visible=False,row=3,col=2)

# fig.add_trace(go.Bar(y=bottom7_stations.index,
#                     x=bottom7_stations["sum"],
#                      orientation='h',
#                      showlegend=False),row=3,col=3)
# fig.update_yaxes(visible=False,row=3,col=3)
# fig.update_layout(width=1000,height=1000)
# fig.write_html("visualizations/location_visualizations.html")

# weather=pd.read_csv("Data/weather.csv")
# daily_data=hourly_data.groupby('date')['ridership'].agg(['mean','std','sum']).reset_index()
# daily_date_with_weather=pd.merge(daily_data,weather,how='left',left_on='date',right_on='Date')
# fig = make_subplots(rows=4, cols=4,
#                     subplot_titles=("Temperature Distribution",
#                                     "Precipitation Distribution",
#                                     "Snowfall Distribution",
#                                     "Snow Depth Distribution",
#                                    '','','','',
#                                     '','','','',
#                                     'Ridership by Temperature','Ridersip by Precipitation'
#                                    ))
# # temp_dist = ff.create_distplot([daily_date_with_weather.Avg_Temperature.to_list()],
# #                          group_labels=["Temperature"], bin_size=5)
# labels=["Temperature","Precipitation","Snowfall"," Snow Depth"]
# colors=["blue","red","green","orange"]
# parameters_bins=['Temperature_Bin','PRCP_Bin']
# for i,parameter in enumerate(['Avg_Temperature','PRCP',"SNOW","SNWD"]):
#     weather_distribution=px.histogram(daily_date_with_weather, x=parameter,
#                                       nbins=20)
#     fig.add_trace(weather_distribution.data[0],row=1,col=i+1)
#     fig.update_xaxes(title_text=labels[i],row=1,col=i+1)
#     weather_distribution2=px.scatter(x=daily_date_with_weather[parameter],
#                                    y=np.random.normal(loc=0,scale=0.01,
#                                                       size=len(daily_date_with_weather[parameter])
#                                                      ))
#     fig.add_trace(weather_distribution2.data[0],row=2,col=i+1)
#     fig.update_xaxes(title_text=labels[i],row=2,col=i+1)

#     weather_box=px.box(daily_date_with_weather, x=parameter)
#     fig.add_trace(weather_box.data[0],row=3,col=i+1)
#     fig.update_xaxes(title_text=labels[i],row=3,col=i+1)
# fig.update_yaxes(title_text="Count",row=1,col=1)

# for i,parameter_bin in enumerate(parameters_bins):
#     weather_into_bins=daily_date_with_weather.groupby(parameter_bin)['sum'].agg(['mean','std','size'])
#     fig.add_trace(go.Bar(x=weather_into_bins.index,
#                     y=weather_into_bins['mean'],
#                     error_y=dict(type='data',array=weather_into_bins['std'].to_list()),
#                      showlegend=False
#                     ),row=4,col=i+1)
# fig.update_yaxes(title_text="Average Total Daily Ridership",row=4,col=1)
# fig.update_layout(height=800, width=1000,title_text="Weather Analysis")
# fig.show()
tab1, tab2, tab3,tab4 = st.tabs(["Time", "Geography", "Weather","Station vs Station"])
with tab1:
    st.markdown("""
                - **Rush Hours**: 7-8 AM and 3-6 PM
                - Weekdays are busier than weekends
                - Some months are busier than others""")
    
    st.caption("Data from DATA.NY.GOV; generated by _Plotly_")
    
    html_file_time = open(
        "visualizations/time_visualizations.html", 'r', encoding='utf-8')
    source_code = html_file_time.read()
    components.html(source_code, width=1000, height=1000)
with tab2:
    st.markdown("""
- **Brooklyn has more data**; Brooklyn has the most stations(157), followed by Manhattan(120), Queens(78), BX(68), and SI(2). 
- **Manhattan has the most traffic**(a.k.a ridership).
- Top 7 busiest subway stations: Times Sq-42 St,Grand Central-42 St, 34 St-Herald Sq,14 St-Union Sq, Fulton St,34 St-Penn Station, and 59 St-Columbus Circle""")
    st.caption("Data from DATA.NY.GOV; generated by _Plotly_")
    st.write("Time Spatial Analysis: "+"https://github.com/jchen056/MTA_MTA/blob/main/visualizations/time_spatial.gif")
    
    html_file_time = open(
        "visualizations/location_visualizations.html", 'r', encoding='utf-8')
    source_code = html_file_time.read()
    components.html(source_code, width=1000, height=1000)

with tab3:
    tab_31, tab_32 = st.tabs(['Weather Distrbution', 'Time Series'])
    with tab_31:
        st.markdown("Light rainfall is considered less than 0.10 inches of rain per hour. Moderate rainfall measures 0.10 to 0.30 inches of rain per hour. Heavy rainfall is more than 0.30 inches of rain per hour. Source: WeatherShack.com. ")
        st.caption("Data from DATA.NY.GOV and NOAA; generated by _Plotly_")
        html_file_time = open(
            "visualizations/weather.html", 'r', encoding='utf-8')
        source_code = html_file_time.read()
        components.html(source_code, width=980, height=1000)
    with tab_32:
        st.markdown("""
Temperature has seasonal trends but ridership continues to increases from the low points recorded in 2020""")
        st.caption("Data from DATA.NY.GOV and NOAA; generated by _Plotly_")
        html_file_time = open(
            "visualizations/weather_and_ridership.html", 'r', encoding='utf-8')
        source_code = html_file_time.read()
        components.html(source_code, width=980, height=1000)

with tab4:
    st.caption("Data from DATA.NY.GOV; generated by _Plotly_")
    station_names=['1 Av (L)', '103 St (1)', '103 St (6)', '104 St (J,Z)',
       '110 St (6)', '111 St (7)', '111 St (A)', '111 St (J)',
       '116 St (2,3)', '116 St (6)', '116 St (B,C)', '121 St (J,Z)',
       '125 St (1)', '125 St (2,3)', '135 St (2,3)', '135 St (B,C)',
       '14 St (A,C,E)/8 Av (L)', '145 St (3)', '145 St (A,B,C,D)',
       '155 St (B,D)', '155 St (C)', '157 St (1)', '167 St (4)',
       '169 St (F)', '170 St (4)', '175 St (A)', '18 Av (D)', '18 Av (F)',
       '18 Av (N)', '18 St (1)', '181 St (1)', '181 St (A)', '191 St (1)',
       '2 Av (F)', '20 Av (D)', '20 Av (N)', '21 St (G)', '215 St (1)',
       '23 St (1)', '23 St (6)', '23 St (C,E)', '23 St (F,M)',
       '23 St (R,W)', '238 St (1)', '25 Av (D)', '25 St (R)', '28 St (1)',
       '3 Av (L)', '30 Av (N,W)', '33 St (6)', '34 St-Hudson Yards (7)',
       '36 Av (N,W)', '45 St (R)', '46 St (M,R)', '50 St (C,E)',
       '50 St (D)', '52 St (7)', '53 St (R)', '55 St (D)', '57 St (F)',
       '59 St (N,R)', '63 Dr-Rego Park (M,R)', '69 St (7)', '7 Av (B,Q)',
       '7 Av (F,G)', '71 St (D)', '72 St (Q)', '75 Av (E,F)',
       '75 St-Elderts Ln (J,Z)', '77 St (6)', '77 St (R)', '79 St (1)',
       '79 St (D)', '8 Av (N)', '80 St (A)', '86 St (1)', '86 St (N)',
       '86 St (Q)', '88 St (A)', '9 Av (D)', '96 St (6)', '96 St (Q)',
       'Aqueduct Racetrack (A)', 'Avenue I (F)', 'Avenue M (Q)',
       'Avenue N (F)', 'Avenue U (F)', 'Avenue U (N)', 'Avenue X (F)',
       'Bay 50 St (D)', 'Bay Pkwy (D)', 'Bay Pkwy (N)', 'Bedford Av (L)',
       'Bowery (J,Z)', 'Broadway (G)',
       'Brooklyn Bridge-City Hall (4,5,6)/Chambers St (J,Z)',
       'Buhre Av (6)', 'Christopher St-Sheridan Sq (1)',
       'Church Av (2,5)', 'DeKalb Av (L)', 'Ditmas Av (F)',
       'Dyckman St (A)', 'Forest Av (M)', 'Fort Hamilton Pkwy (D)',
       'Fulton St (G)', 'Graham Av (L)', 'Grant Av (A)', 'Halsey St (J)',
       'Halsey St (L)', 'Houston St (1)', 'Hunters Point Av (7)',
       'Junius St (3)', 'Kings Hwy (F)', 'Kings Hwy (N)',
       'Lafayette Av (C)', 'Marble Hill-225 St (1)', 'Morgan Av (L)',
       'Ralph Av (C)', 'Rector St (1)', 'Sutter Av (L)', 'Wilson Av (L)',
       'Woodlawn (4)', 'Woodside-61 St (7)', 'York St (F)',
       'Zerega Av (6)', '103 St (B,C)', '103 St-Corona Plaza (7)',
       '104 St (A)', '116 St-Columbia University (1)', '125 St (4,5,6)',
       '125 St (A,B,C,D)', '137 St-City College (1)',
       '138 St-Grand Concourse (4,5)', '14 St (F,M,1,2,3)/6 Av (L)',
       '145 St (1)', '14 St-Union Sq (L,N,Q,R,W,4,5,6)',
       '149 St-Grand Concourse (2,4,5)', '15 St-Prospect Park (F,G)',
       '161 St-Yankee Stadium (B,D,4)', '163 St-Amsterdam Av (C)',
       '167 St (B,D)', '168 St (A,C,1)', '170 St (B,D)', '174 St (2,5)',
       '174-175 Sts (B,D)', '176 St (4)', '182-183 Sts (B,D)',
       '183 St (4)', '190 St (A)', '207 St (1)', '21 St-Queensbridge (F)',
       '219 St (2,5)', '225 St (2,5)', '231 St (1)', '233 St (2,5)',
       '28 St (6)', '28 St (R,W)', '3 Av-138 St (6)', '3 Av-149 St (2,5)',
       '33 St-Rawson St (7)', '34 St-Herald Sq (B,D,F,M,N,Q,R,W)',
       '34 St-Penn Station (1,2,3)', '36 St (D,N,R)',
       '34 St-Penn Station (A,C,E)', '36 St (M,R)', '39 Av (N,W)',
       '4 Av (F,G)/9 St (R)', '40 St-Lowery St (7)', '46 St-Bliss St (7)',
       '47-50 Sts-Rockefeller Center (B,D,F,M)', '49 St (N,R,W)',
       '5 Av-53 St (E,M)', '5 Av-59 St (N,R,W)', '50 St (1)',
       '57 St-7 Av (N,Q,R,W)', '59 St-Columbus Circle (A,B,C,D,1)',
       '65 St (M,R)', '66 St-Lincoln Center (1)', '67 Av (M,R)',
       '68 St-Hunter College (6)', '7 Av (B,D,E)', '72 St (1,2,3)',
       '72 St (B,C)',
       '74-Broadway (7)/Jackson Hts-Roosevelt Av (E,F,M,R)',
       '8 St-New York University (R,W)',
       '81 St-Museum of Natural History (B,C)', '82 St-Jackson Hts (7)',
       '85 St-Forest Pkwy (J)', '86 St (4,5,6)', '86 St (B,C)',
       '86 St (R)', '90 St-Elmhurst Av (7)', '96 St (1,2,3)',
       '96 St (B,C)', 'Alabama Av (J)', 'Allerton Av (2,5)',
       'Astor Place (6)', 'Aqueduct-North Conduit Av (A)',
       'Astoria Blvd (N,W)', 'Atlantic Av (L)',
       'Astoria-Ditmars Blvd (N,W)',
       'Atlantic Av-Barclays Ctr (B,D,N,Q,R,2,3,4,5)', 'Avenue H (Q)',
       'Avenue J (Q)', 'Avenue P (F)', 'Avenue U (Q)', 'Bay Pkwy (F)',
       'Bay Ridge Av (R)', 'Bay Ridge-95 St (R)', 'Baychester Av (5)',
       'Beach 105 St (A,S)', 'Beach 25 St (A)', 'Beach 36 St (A)',
       'Beach 44 St (A)', 'Beach 60 St (A)',
       'Beach 67 St-Arverne By The Sea (A)', 'Beach 98 St (A,S)',
       'Beach 90 St (A,S)', 'Bedford Park Blvd (B,D)', 'Bergen St (2,3)',
       'Bedford Park Blvd-Lehman College (4)', 'Bergen St (F,G)',
       'Bedford-Nostrand Avs (G)', 'Beverley Rd (Q)', 'Beverly Rd (2,5)',
       'Bowling Green (4,5)', 'Briarwood-Van Wyck Blvd (E,F)',
       'Broad St (J,Z)', 'Brighton Beach (B,Q)', 'Broad Channel (A,S)',
       'Broadway (N,W)', 'Broadway Junction (A,C,J,L,Z)', 'Brook Av (6)',
       'Bronx Park East (2,5)',
       'Broadway-Lafayette St (B,D,F,M)/Bleecker St (6)',
       'Burke Av (2,5)', 'Burnside Av (4)', 'Bushwick Av-Aberdeen St (L)',
       'Canal St (1)', 'Canal St (A,C,E)', 'Canal St (J,N,Q,R,W,Z,6)',
       'Canarsie-Rockaway Pkwy (L)', 'Central Av (M)', 'Carroll St (F,G)',
       'Castle Hill Av (6)', 'Cathedral Pkwy-110 St (1)',
       'Cathedral Pkwy-110 St (B,C)', 'Central Park North-110 St (2,3)',
       'Chambers St (1,2,3)',
       'Chambers St (A,C)/WTC (E)/Park Pl (2,3)/Cortlandt (R,W)',
       'Chauncey St (J,Z)', 'Church Av (B,Q)', 'Church Av (F,G)',
       'City Hall (R,W)', 'Clark St (2,3)', 'Classon Av (G)',
       'Cleveland St (J)', 'Clinton-Washington Avs (C)',
       'Clinton-Washington Avs (G)', 'Cortelyou Rd (Q)',
       'Coney Island-Stillwell Av (D,F,N,Q)', 'Court Sq (E,G,M,7)',
       'Court St (R)/Borough Hall (2,3,4,5)', 'Crescent St (J,Z)',
       'Cypress Av (6)', 'Cypress Hills (J)',
       'Crown Heights-Utica Av (3,4)', 'DeKalb Av (B,Q,R)',
       'Delancey St (F)/Essex St (J,M,Z)', 'Dyckman St (1)',
       'East 105 St (L)', "East 143 St-St Mary's St (6)",
       'East 149 St (6)', 'East 180 St (2,5)', 'East Broadway (F)',
       'Eastchester-Dyre Av (5)', 'Eastern Pkwy-Brooklyn Museum (2,3)',
       'Elder Av (6)', 'Elmhurst Av (M,R)', 'Euclid Av (A,C)',
       'Far Rockaway-Mott Av (A)', 'Flatbush Av-Brooklyn College (2,5)',
       'Flushing Av (G)', 'Flushing Av (J,M)', 'Flushing-Main St (7)',
       'Fordham Rd (4)', 'Fordham Rd (B,D)',
       'Forest Hills-71 Av (E,F,M,R)', 'Fort Hamilton Pkwy (F,G)',
       'Franklin St (1)', 'Fort Hamilton Pkwy (N)',
       'Franklin Av (2,3,4,5)/Botanic Garden (S)', 'Franklin Av (C,S)',
       'Freeman St (2,5)', 'Fresh Pond Rd (M)',
       'Fulton St (A,C,J,Z,2,3,4,5)', 'Gates Av (J,Z)',
       'Grand Army Plaza (2,3)', 'Grand Av-Newtown (M,R)',
       'Grand St (B,D)', 'Grand Central-42 St (S,4,5,6,7)',
       'Grand St (L)', 'Greenpoint Av (G)', 'Gun Hill Rd (2,5)',
       'Gun Hill Rd (5)', 'Harlem-148 St (3)', 'Hewes St (J,M)',
       'High St (A,C)', 'Howard Beach-JFK Airport (A)', 'Hoyt St (2,3)',
       'Hoyt-Schermerhorn Sts (A,C,G)', 'Hunts Point Av (6)',
       'Inwood-207 St (A)', 'Intervale Av (2,5)', 'Jackson Av (2,5)',
       'Jamaica Center-Parsons-Archer (E,J,Z)', 'Jamaica-179 St (F)',
       'Jefferson St (L)', 'Jamaica-Van Wyck (E)',
       'Jay St-MetroTech (A,C,F,R)', 'Junction Blvd (7)',
       'Kew Gardens-Union Turnpike (E,F)', 'Kings Hwy (B,Q)',
       'Kingsbridge Rd (4)', 'Kingston Av (3)', 'Kingsbridge Rd (B,D)',
       'Kingston-Throop Avs (C)', 'Kosciuszko St (J)',
       'Knickerbocker Av (M)', 'Lexington Av (N,R,W)/59 St (4,5,6)',
       'Liberty Av (C)', 'Lexington Av-53 St (E,M)/51 St (6)',
       'Lexington Av-63 St (F,Q)', 'Livonia Av (L)', 'Longwood Av (6)',
       'Lorimer St (J,M)', 'Lorimer St (L)/Metropolitan Av (G)',
       'Marcy Av (J,M,Z)', 'Middletown Rd (6)', 'Mets-Willets Point (7)',
       'Montrose Av (L)', 'Middle Village-Metropolitan Av (M)',
       'Morris Park (5)', 'Morrison Av-Soundview (6)', 'Mosholu Pkwy (4)',
       'Mt Eden Av (4)', 'Myrtle Av (J,M,Z)', 'Myrtle-Willoughby Avs (G)',
       'Nassau Av (G)', 'Neck Rd (Q)', 'Myrtle-Wyckoff Avs (L,M)',
       'Neptune Av (F)', 'Nereid Av (2,5)', 'Nevins St (2,3,4,5)',
       'New Lots Av (3)', 'New Lots Av (L)',
       'New Utrecht Av (N)/62 St (D)', 'Newkirk Av (2,5)',
       'Newkirk Plaza (B,Q)', 'Northern Blvd (M,R)', 'Norwood Av (J,Z)',
       'Nostrand Av (3)', 'Norwood-205 St (D)', 'Nostrand Av (A,C)',
       'Ocean Pkwy (Q)', 'Ozone Park-Lefferts Blvd (A)', 'Park Pl (S)',
       'Parkchester (6)', 'Parkside Av (Q)', 'Parsons Blvd (F)',
       'Pelham Bay Park (6)', 'Pelham Pkwy (2,5)', 'Pelham Pkwy (5)',
       'Prince St (R,W)', 'Pennsylvania Av (3)', 'President St (2,5)',
       'Prospect Av (2,5)', 'Prospect Av (R)', 'Prospect Park (B,Q,S)',
       'Queens Plaza (E,M,R)', 'Queensboro Plaza (N,W,7)',
       'Rector St (R,W)', 'Rockaway Av (3)', 'Rockaway Av (C)',
       'Rockaway Blvd (A)', 'Rockaway Park-Beach 116 St (A,S)',
       'Saratoga Av (3)', 'Roosevelt Island (F)', 'Seneca Av (M)',
       'Sheepshead Bay (B,Q)', 'Shepherd Av (C)', 'Simpson St (2,5)',
       'Smith-9 Sts (F,G)', 'Spring St (6)',
       'South Ferry (1)/Whitehall St (R,W)', 'Spring St (C,E)',
       'St George', 'St Lawrence Av (6)', 'Steinway St (M,R)',
       'Sterling St (2,5)', 'Sutphin Blvd (F)',
       'Sutphin Blvd-Archer Av-JFK Airport (E,J,Z)',
       'Sutter Av-Rutland Rd (3)',
       'Times Sq-42 St (N,Q,R,W,S,1,2,3,7)/42 St (A,C,E)/Bryant Pk (B,D,F,M)/5 Av (7)',
       'Tompkinsville', 'Tremont Av (B,D)', 'Union St (R)',
       'Utica Av (A,C)', 'Van Cortlandt Park-242 St (1)',
       'Van Siclen Av (3)', 'Van Siclen Av (C)', 'Van Siclen Av (J,Z)',
       'Vernon Blvd-Jackson Av (7)', 'WTC Cortlandt (1)',
       'Wakefield-241 St (2)', 'Wall St (2,3)', 'Wall St (4,5)',
       'West 4 St-Washington Sq (A,B,C,D,E,F,M)',
       'West 8 St-New York Aquarium (F,Q)',
       'West Farms Sq-East Tremont Av (2,5)', 'Whitlock Av (6)',
       'Westchester Sq-East Tremont Av (6)', 'Winthrop St (2,5)',
       'Woodhaven Blvd (J,Z)', 'Woodhaven Blvd (M,R)']
    options = st.multiselect(label='Select two stations for comparison',options=station_names,
    default=['116 St-Columbia University (1)', 'Flushing-Main St (7)'],max_selections=2)

    for option in options:
        html_file_station_time=open(
            'visualizations/station_times/'+option.split('(')[0].strip()+'.html','r', encoding='utf-8')
        source_code = html_file_station_time.read()
        components.html(source_code, width=1000, height=1000)
        with st.expander("Click here to see more"):
            html_file_station_time=open(
            'visualizations/station/'+option.split('(')[0].strip()+'.html','r', encoding='utf-8')
            source_code = html_file_station_time.read()
            components.html(source_code, width=1000, height=1000)

        st.markdown("""---""")



    
