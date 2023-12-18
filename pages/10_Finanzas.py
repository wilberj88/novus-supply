import streamlit as st
# Import the requests library 
import requests 
import pandas as pd
from lightweight_charts.widgets import StreamlitChart


st.set_page_config(
  page_title="Novus Mando",
  page_icon="🎮",
  layout="wide"
)

st.write("""
# 🎮 Novus Mando 🚚 Supply Chain 🏭 FINANZAS
""")

st.sidebar.markdown("Desarrollado por [Novus Mando] (www.novussolutions.io)")


api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbHVlIjoiNjU4MGJkMDkxNDBjZmQ3MjNkMTQyNDFhIiwiaWF0IjoxNzAyOTM2NDQ5LCJleHAiOjMzMjA3NDAwNDQ5fQ.dxJczsaCJE5gAmbSd6xD3-0k5yaFruoaNLYMxLz2Oaw"
btc_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=BTC/USDT&interval=1m').json()
st.dataframe(btc_price)


url = f'https://api.taapi.io/candles?secret={api_key}&exchange=binance&symbol=BTC/USDT&interval=1d&period=365'
hist_json = requests.get(url).json()
hist_df = pd.DataFrame(hist_json).drop('timestampHuman', axis = 1).rename(columns = {'timestamp':'time'})
hist_df.time = pd.to_datetime(hist_df.time, unit = 's')
st.dataframe(hist_df.tail())



# Define indicator
indicator = "rsi"
  
# Define endpoint 
endpoint = f"https://api.taapi.io/{indicator}"
  
# Define a parameters dict for the parameters to be sent to the API 
parameters = {
    'secret': 'TAAPI_SECRET',
    'exchange': 'binance',
    'symbol': 'BTC/USDT',
    'interval': '1h'
    } 
  
# Send get request and save the response as response object 
response = requests.get(url = endpoint, params = parameters)
  
# Extract data in json format 
result = response.json() 

# Print result
st.write(result)
