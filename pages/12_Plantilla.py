import streamlit as st
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

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html = True)
