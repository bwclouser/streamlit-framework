import streamlit as st
import requests
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from bokeh.plotting import figure,output_file,show
from datetime import datetime

st.title("Test Program")

st.sidebar.markdown('## Ticker Symbol')

user_input = st.sidebar.text_input("Ticker Symbol", 'GOOG')

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+user_input+'&interval=5min&apikey=EGO54BOG5AMJTV2H'
r = requests.get(url)
data = r.json()

#df = pd.DataFrame.from_dict(data, orient = 'index')

dict=data['Time Series (5min)']

times=dict.keys()
dtime=[datetime.strptime(time, '%Y-%m-%d %H:%M:%S') for time in times]

closes=[float(val['4. close']) for val in dict.values()]

print(dtime[0],closes[0])


p = figure(title=user_input + ' Stock Price',x_axis_label='Date',y_axis_label='Price (USD)')
p.line(dtime, closes, line_width=2)

st.bokeh_chart(p, use_container_width=True)
