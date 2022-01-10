import streamlit as st
import requests
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from bokeh.plotting import figure,output_file,show
from bokeh.models import DatetimeTickFormatter
from datetime import datetime
from datetime import timedelta
import os

st.title("Milestone Project -- Stock Prices")

#st.sidebar.markdown('## Ticker Symbol')

user_input = st.sidebar.text_input("Ticker Symbol", 'GOOG')

apikey = os.environ.get('APIKEY')
#print(apikey)

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+user_input+'&interval=60min&outputsize=full&apikey='+apikey
r = requests.get(url)
data = r.json()

#df = pd.DataFrame.from_dict(data, orient = 'index')

dict=data['Time Series (60min)']

times=dict.keys()
dtime=np.array([datetime.strptime(time, '%Y-%m-%d %H:%M:%S') for time in times])

closes=np.array([float(val['4. close']) for val in dict.values()])

truth=dtime>dtime[0]-timedelta(days=31)

dtime=dtime[truth]
closes=closes[truth]

print(dtime[0],closes[0])


p = figure(title=user_input + ' Stock Price',x_axis_label='Date',y_axis_label='Price (USD)')
p.line(dtime, closes, line_width=2)
p.xaxis.formatter=DatetimeTickFormatter(years=["%d %B %Y"])
st.bokeh_chart(p, use_container_width=True)
