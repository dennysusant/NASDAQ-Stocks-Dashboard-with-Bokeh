
from ctypes import sizeof
import requests
from bokeh.io import curdoc
from bokeh.models import ColumnDataSource,DatetimeTickFormatter,Select
from bokeh.layouts import layout
from bokeh.plotting import figure
from datetime import datetime
from math import radians # Rotate axis ticks
import numpy as np
import finnhub
from bokeh.layouts import gridplot,row
import pandas as pd

# Get Nasdaq Stock List
nasdaq=pd.read_csv('nasdaq.csv')
nasdaq=nasdaq['Symbol']
nasdaqlist=[]
for item in nasdaq:
    nasdaqlist.append((item,item))


def get_data(stocks):
    finnhub_client = finnhub.Client(api_key="c7j7g52ad3if6uehd9ng")
    data=finnhub_client.quote(stocks)
    data=data['c']
    return data
# Create Figure
p=figure(x_axis_type='datetime', width=500, height=300)

#Create Data
def create_value():
    data=0
    return data

# Create data source
source=ColumnDataSource(dict(x=[], y=[]))
p.circle(x='x', y='y', color='firebrick', line_color='firebrick', source=source)
p.line(x='x', y='y', source= source)


def update():
    new_data=dict(x=[datetime.now()],y=[get_data(select.value)])
    source.stream(new_data,rollover=200)
    # print(new_data)
    p.title.text='Now Streaming %s Price' % select.value
    # print(select.value)

# Callback Function
def update_intermed(attrname,old,new):
    source.data=dict(x=[],y=[])
    update()

date_pattern=['%Y-%m-%d\n%H:%M:%S']

p.xaxis.formatter=DatetimeTickFormatter(
    seconds=date_pattern,
    minsec=date_pattern,
    minutes=date_pattern,
    hourmin=date_pattern,
    hours=date_pattern,
    days=date_pattern,
    months=date_pattern,
    years=date_pattern,
)
p.xaxis.major_label_orientation=radians(60)
p.xaxis.axis_label='Date'
p.yaxis.axis_label='Price'

#Create Selection Widget
options=nasdaqlist
select=Select(title='Stocks', value='AAPL',options=options,max_width=100)
select.on_change('value',update_intermed)

# Second Graph
p1=figure(x_axis_type='datetime', width=500, height=300)
source2=ColumnDataSource(dict(x=[], y=[]))
p1.circle(x='x', y='y', color='firebrick', line_color='firebrick', source=source2)
p1.line(x='x', y='y', source= source2)


def update2():
    new_data2=dict(x=[datetime.now()],y=[get_data(select2.value)])
    source2.stream(new_data2,rollover=200)
    p1.title.text='Now Streaming %s Price' % select2.value
    # print(select2.value)

# Callback Function
def update_intermed2(attrname,old,new):
    source2.data=dict(x=[],y=[])
    update2()

date_pattern=['%Y-%m-%d\n%H:%M:%S']

p1.xaxis.formatter=DatetimeTickFormatter(
    seconds=date_pattern,
    minsec=date_pattern,
    minutes=date_pattern,
    hourmin=date_pattern,
    hours=date_pattern,
    days=date_pattern,
    months=date_pattern,
    years=date_pattern,
)
p1.xaxis.major_label_orientation=radians(60)
p1.xaxis.axis_label='Date'
p1.yaxis.axis_label='Price'
options=nasdaqlist
select2=Select(title='Stocks', value='TSLA',options=options,max_width=100)
select2.on_change('value',update_intermed2)


#Third Graph
p2=figure(x_axis_type='datetime', width=500, height=300)
source3=ColumnDataSource(dict(x=[], y=[]))
p2.circle(x='x', y='y', color='firebrick', line_color='firebrick', source=source3)
p2.line(x='x', y='y', source= source3)


def update3():
    new_data3=dict(x=[datetime.now()],y=[get_data(select3.value)])
    source3.stream(new_data3,rollover=200)
    p2.title.text='Now Streaming %s Price' % select3.value
    # print(select3.value)

# Callback Function
def update_intermed3(attrname,old,new):
    source3.data=dict(x=[],y=[])
    update3()

date_pattern=['%Y-%m-%d\n%H:%M:%S']

p2.xaxis.formatter=DatetimeTickFormatter(
    seconds=date_pattern,
    minsec=date_pattern,
    minutes=date_pattern,
    hourmin=date_pattern,
    hours=date_pattern,
    days=date_pattern,
    months=date_pattern,
    years=date_pattern,
)
p2.xaxis.major_label_orientation=radians(60)
p2.xaxis.axis_label='Date'
p2.yaxis.axis_label='Price'
options=nasdaqlist
select3=Select(title='Stocks', value='GOOG',options=options,max_width=100)
select3.on_change('value',update_intermed3)


#Fourth Graph
p3=figure(x_axis_type='datetime', width=500, height=300)
source4=ColumnDataSource(dict(x=[], y=[]))
p3.circle(x='x', y='y', color='firebrick', line_color='firebrick', source=source4)
p3.line(x='x', y='y', source= source4)


def update4():
    new_data4=dict(x=[datetime.now()],y=[get_data(select4.value)])
    source4.stream(new_data4,rollover=200)
    p3.title.text='Now Streaming %s Price' % select4.value

# Callback Function
def update_intermed4(attrname,old,new):
    source4.data=dict(x=[],y=[])
    update4()

date_pattern=['%Y-%m-%d\n%H:%M:%S']

p3.xaxis.formatter=DatetimeTickFormatter(
    seconds=date_pattern,
    minsec=date_pattern,
    minutes=date_pattern,
    hourmin=date_pattern,
    hours=date_pattern,
    days=date_pattern,
    months=date_pattern,
    years=date_pattern,
)
p3.xaxis.major_label_orientation=radians(60)
p3.xaxis.axis_label='Date'
p3.yaxis.axis_label='Price'
options=nasdaqlist
select4=Select(title='Stocks', value='MSFT',options=options,max_width=100)
select4.on_change('value',update_intermed4)


# Config Layout
lay_out=layout(gridplot([[p,select,p1,select2],[p2,select3,p3,select4]]))
curdoc().add_root(lay_out)
curdoc().title='Streaming Stocks Price'
curdoc().theme = 'contrast'

#Because finnhub api is limited we set the update for 5 sec
curdoc().add_periodic_callback(update,5000)
curdoc().add_periodic_callback(update2,5000)
curdoc().add_periodic_callback(update3,5000)
curdoc().add_periodic_callback(update4,5000)