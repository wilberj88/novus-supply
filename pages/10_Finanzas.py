import streamlit as st
# Import the requests library 
import requests 


st.set_page_config(
  page_title="Novus Mando Fifa",
  page_icon="⚽",
  layout="wide"
)

st.write("""
# 🎮 Novus Mando 🚚 Supply Chain 🏭 FINANZAS
""")

st.sidebar.markdown("Desarrollado por [Novus Mando] (www.novussolutions.io)")




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
