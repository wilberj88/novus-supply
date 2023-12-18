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

if "symbols_list" not in st.session_state:
    st.session_state.symbols_list = None

st.markdown(
    """
    <style>
        footer {display: none}
        [data-testid="stHeader"] {display: none}
    </style>
    """, unsafe_allow_html = True
)

#with open('style.css') as f:
#    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)

api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbHVlIjoiNjU4MGJkMDkxNDBjZmQ3MjNkMTQyNDFhIiwiaWF0IjoxNzAyOTM2NDQ5LCJleHAiOjMzMjA3NDAwNDQ5fQ.dxJczsaCJE5gAmbSd6xD3-0k5yaFruoaNLYMxLz2Oaw"

title_col, emp_col, btc_col, eth_col, xmr_col, sol_col, xrp_col = st.columns([1,0.2,1,1,1,1,1])

with title_col:
    st.markdown('<p class="dashboard_title">Crypto<br>Dashboard</p>', unsafe_allow_html = True)

with btc_col:
    with st.container():
        btc_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=BTC/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="btc_text">BTC / USDT<br></p><p class="price_details">{btc_price}</p>', unsafe_allow_html = True)

with eth_col:
    with st.container():
        eth_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=ETH/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="eth_text">ETH / USDT<br></p><p class="price_details">{eth_price}</p>', unsafe_allow_html = True)

with xmr_col:
    with st.container():
        xmr_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=XMR/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="xmr_text">XMR / USDT<br></p><p class="price_details">{xmr_price}</p>', unsafe_allow_html = True)

with sol_col:
    with st.container():
        sol_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=SOL/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="sol_text">SOL / USDT<br></p><p class="price_details">{sol_price}</p>', unsafe_allow_html = True)

with xrp_col:
    with st.container():
        xrp_price = requests.get(f'https://api.taapi.io/price?secret={api_key}&exchange=binance&symbol=XRP/USDT&interval=1m').json()['value']
        st.markdown(f'<p class="xrp_text">XRP / USDT<br></p><p class="price_details">{xrp_price}</p>', unsafe_allow_html = True)





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
