import streamlit as st
import requests
import numpy as np
import pandas as pd
from bokeh.plotting import figure,output_file,show

st.title("Test Program")

st.sidebar.markdown('## Ticker Symbol')

user_input = st.sidebar.text_input("Ticker Symbol", 'GOOG')

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+user_input+'&interval=5min&apikey=EGO54BOG5AMJTV2H'
r = requests.get(url)
data = r.json()

df = pd.DataFrame.from_dict(data, orient = 'index')

p = figure()
show(p)
