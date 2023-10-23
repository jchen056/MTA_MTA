import pandas as pd
import numpy as np
import streamlit as st
from datetime import datetime
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import calendar
import streamlit.components.v1 as components

# @st.cache_data
# def read_csv(path="Data/MTA_Subway_Hourly_Ridership__Beginning_February_2022.csv"):
#     return pd.read_csv(path)


# hourly_data = read_csv()
# hourly_data["datetime"] = hourly_data["transit_timestamp"].apply(
#     lambda x: datetime.strptime(x, "%m/%d/%Y %I:%M:%S %p"))
# hourly_data["hour"] = hourly_data["datetime"].apply(lambda x: x.hour)
# hourly_data['month'] = hourly_data["datetime"].apply(lambda x: x.month)
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

tab1, tab2, tab3 = st.tabs(["Time", "Geography", "Time-spatial"])
with tab1:
    html_file_time = open(
        "visualizations/time_visualizations.html", 'r', encoding='utf-8')
    source_code = html_file_time.read()
    components.html(source_code, width=1000, height=1000)
with tab2:
    html_file_time = open(
        "visualizations/location_visualizations.html", 'r', encoding='utf-8')
    source_code = html_file_time.read()
    components.html(source_code, width=1000, height=1000)
