import pandas as pd
import numpy as np
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
import streamlit.components.v1 as components
from bokeh.plotting import figure, show, output_file, save
from bokeh.models import HoverTool
from bokeh.layouts import row, column
from bokeh.io import output_notebook
# ColumnDataSource is Bokeh’s own data structure
from bokeh.models import ColumnDataSource
from bokeh.models import Div, Spinner, CustomJS, DateRangeSlider
from datetime import datetime, timedelta
from bokeh.models import DatetimeTickFormatter
from datetime import datetime

st.header("MTA Complaints")
# subway complaints and commendation
# df = pd.read_csv(
#     "/Users/jchen056/Data/MTA_Customer_Feedback_Data__Beginning_2014_20231023.csv")
# subways = df[df['Agency'] == 'Subways'].copy()
# subways_commendation_and_complaints = subways.groupby(
#     ['Year', 'Commendation or Complaint']).size().reset_index()
# subways_commendation_and_complaints.rename(columns={0: 'count'}, inplace=True)
# fig = make_subplots(rows=4, cols=1, subplot_titles=('NYC Buses', 'Subways', 'Long Island Rail Road', 'Metro-North Railroad')
#                     )
# for i, agency in enumerate(['NYC Buses', 'Subways', 'Long Island Rail Road', 'Metro-North Railroad']):
#     agency_info = df[df['Agency'] == agency].copy()
#     commendation_and_complaints = agency_info.groupby(
#         ['Year', 'Commendation or Complaint']).size().reset_index()
#     commendation_and_complaints.rename(columns={0: 'count'}, inplace=True)
#     bar = px.bar(commendation_and_complaints, x="Year",
#                  y="count", color='Commendation or Complaint')
#     for trace in bar.data:
#         fig.add_trace(trace, i+1, 1)
# #     fig.add_trace(go.Bar(x=commendation_and_complaints[commendation_and_complaints['Commendation or Complaint']=='Commendation']['Year'],
# #                     y=commendation_and_complaints[commendation_and_complaints['Commendation or Complaint']=='Commendation']['count'],
# #                     showlegend=True,
# #                          legendgroup="Commendation",
# #                     name='Commendation')
# #                    ,row=i+1,col=1)
# #     fig.add_trace(go.Bar(x=commendation_and_complaints[commendation_and_complaints['Commendation or Complaint']=='Complaint']['Year'],
# #                     y=commendation_and_complaints[commendation_and_complaints['Commendation or Complaint']=='Complaint']['count'],
# #                     showlegend=True,
# #                          legendgroup='Complaint',
# #                          name='Complaint')
# #                    ,row=i+1,col=1)
# fig.update_yaxes(type='log')
# fig.update_xaxes(title='Years')
# fig.update_layout(height=800, width=600)
# fig.update_layout(showlegend=False,
#                   title_text="Commendation and Complaint Count for")
# fig.write_html("visualizations/complaints_visualizations.html")


# df = pd.read_csv(
#     "/Users/jchen056/Data/Fare_Card_History_for_Metropolitan_Transportation_Authority__MTA___Beginning_2010.csv")
# df['From_Date'] = df['From Date'].apply(
#     lambda x: datetime.strptime(x, '%m/%d/%Y'))
# df['To_Date'] = df['To Date'].apply(lambda x: datetime.strptime(x, '%m/%d/%Y'))
# # set output to static HTML file
# output_file(filename="visualizations/payment_timeseries.html")
# # Calling the figure() function
# p = figure(title="Time Series",
#            x_axis_label='datetime', x_axis_type="datetime",
#            y_axis_label='Card Swipes',
#            #          y_axis_type="log",
#            tools=[HoverTool()],
#            tooltips=[("date", "@x_values"), ("Card Swipes", "@y_values)")],
#            height=350, sizing_mode="stretch_width",)
# # Use the properties of the Legend object to customize the legend
# p.legend.title = "Types of MetroCards"
# p.legend.label_text_font = "times"
# p.legend.label_text_font_style = "italic"
# p.legend.label_text_color = "navy"

# p.title.text_font_size = "25px"
# p.title.align = "center"
# p.title.text = "Time Series for Weekly Card Swipes"

# p.xaxis.axis_label = "Date"
# p.yaxis.axis_label = "# of Card Swipes"
# p.toolbar_location = "right"
# p.toolbar.autohide = True

# p.xaxis[0].formatter = DatetimeTickFormatter(months="%b %Y")

# payment_types = ["Full Fare", '30 Day Unlimited', '7 Day Unlimited']
# colors = ['blue', 'red', 'green']
# for i, payment_type in enumerate(payment_types):
#     df_payment = df.groupby('From_Date')[
#         payment_type].agg(['sum', 'mean', 'std'])
#     # ColumnDataSource is Bokeh’s own data structure
#     data = {"x_values": df_payment.index, "y_values": df_payment['sum'], "datestr":
#             [datetime.strftime(i, "%Y-%m-%d")for i in df_payment.index.to_list()]}
#     # create ColumnDataSource based on dict
#     source = ColumnDataSource(data=data)
#     p.line(x='x_values', y='y_values', source=source,
#            color=colors[i], legend_label=payment_type)
#     p.circle(x='x_values', y='y_values', source=source,
#              fill_color=colors[i], size=2, fill_alpha=0.5,
#              line_color=colors[i], legend_label=payment_type
#              )
# hover = p.select(dict(type=HoverTool))
# hover.tooltips = [("date", "@datestr"), ("Card Swipes", "@y_values)")]
# hover.mode = 'mouse'
# save(p)
tab1, tab2, tab3 = st.tabs(["Demand", "Complaint vs Commedation", ""])
with tab1:
    html_file_time = open(
        "visualizations/payment_timeseries.html", 'r', encoding='utf-8')
    source_code = html_file_time.read()
    components.html(source_code, width=1000, height=1000)
with tab2:
    html_file_time = open(
        "visualizations/complaints_visualizations.html", 'r', encoding='utf-8')
    source_code = html_file_time.read()
    components.html(source_code, width=1000, height=1000)
