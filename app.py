import streamlit as st
import requests

st.title("Test Program")

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=EGO54BOG5AMJTV2H'
r = requests.get(url)
data = r.json()

st.sidebar.markdown('## Ticker Symbol')
