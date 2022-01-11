import streamlit as st
import requests
import numpy as np
from bokeh.plotting import figure,output_file,show
from bokeh.models import DatetimeTickFormatter
from datetime import datetime
from datetime import timedelta
import os

st.title("Milestone Project -- Stock Prices")
st.text("Display the previous month of stock data")

#st.sidebar.markdown('## Ticker Symbol')

values=['Closing Price', 'Opening Price', 'Volume']
default_ix=values.index('Closing Price')

user_input = st.sidebar.text_input("Ticker Symbol", 'GOOG')
option = st.sidebar.selectbox('Data Options',values,index=default_ix)

#print(option,default_ix)

if option=='Closing Price':
    dchoice = '4. close'
    yAxLab = 'Price (USD)'
elif option=='Opening Price':
    dchoice = '1. open'
    yAxLab = 'Price (USD)'
else:
    dchoice = '5. volume'
    yAxLab = 'Shares'

apikey = os.environ.get('APIKEY')
#print(apikey)

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol='+user_input+'&interval=60min&outputsize=full&apikey='+apikey
r = requests.get(url)
data = r.json()

#df = pd.DataFrame.from_dict(data, orient = 'index')

dict=data['Time Series (60min)']

times=dict.keys()
dtime=np.array([datetime.strptime(time, '%Y-%m-%d %H:%M:%S') for time in times])

closes=np.array([float(val[dchoice]) for val in dict.values()])

truth=dtime>dtime[0]-timedelta(days=31)

dtime=dtime[truth]
closes=closes[truth]

print(dtime[0],closes[0])


p = figure(title=user_input + ' ' + option,x_axis_label='Date',y_axis_label=yAxLab)
p.line(dtime, closes, line_width=2)
p.xaxis.formatter=DatetimeTickFormatter(years=["%d %B %Y"])
st.bokeh_chart(p, use_container_width=True)
