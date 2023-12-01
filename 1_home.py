import streamlit as st
from streamlit_card import card
from streamlit_extras.grid import grid
from streamlit_extras.colored_header import colored_header
import folium
from streamlit_folium import st_folium
import time
from streamlit_echarts import st_echarts
import pytrends
from pytrends.request import TrendReq
import requests
import pandas as pd
from streamlit_extras.let_it_rain import rain 
import plotly.graph_objects as go


st.set_page_config(
  page_title="Novus Mando Supply",
  page_icon="🏭",
  layout="wide"
)

st.write("""
# 🎮 Novus Mando 🚚 Supply Chain 🏭
""")

st.sidebar.markdown("Desarrollado por Novus Mando, S.L. (www.novussolutions.io)")

a = st.selectbox("Selecciona un Mando 🎮 de la Cadena de Suministro:", ("Demanda", "Inventario", "Producción", "Almacenamiento", "Distribución", "Comercialización", "Ventas", "PostVentas", "Finanzas", "Impacto"), index=None, placeholder="Choose an option")

if a:
  b = st.selectbox("Selecciona el módulo de análisis 🔎:", ("Estrategia Gobernanza de Datos", "Datos Históricos", "Datos en Tiempo Real", "Sistemas de Alarmas", "Sistemas de Recomendaciones"), index=None, placeholder="Choose an option")
  if b == "Estrategia Gobernanza de Datos":
    colored_header(
      label="Mando 2: Estrategia de Datos e Inteligencia Artificial",
      description="Procesos, Indicadores y Monitoreo",
      color_name="violet-70",
    )
    st.markdown(
      """
      - 🗣️ _    Titularidad
      - ♻️ _    Ciclo de Vida
      - 🏗️ _     Arquitectura
      - 🧮 _     Modelación
      - ⏲️ _     Operación
      - 🛂 _     Seguridad
      - 🚫 _     Privacidad
      - 🤝 _     Conciliación
      - 💡 _     Referentes
      - 🌊 _     Lago
      - ⚠️ _     Elementos Críticos
      - ℹ️ _     Metadata
      - ✅ _     Calidad
      - 🔄 _     Integración
      - ✝️ _     Políticas
      - ▶️ _     Estándares
      - 🔁 _     Procesos
      """
    )

  if b == "Datos Históricos":
    colored_header(
      label="Mando 1: Modelación Histórica",
      description="Costos, Ventas, Rentabilidades",
      color_name="violet-70",
    )
    c = st.selectbox('Selecciona un año de análisis', ('2018', '2019', '2020', '2021', '2022', '2023', '2024'))
    if c:
        st.write('Desempeño financiero en el año ', b)
        col4, col5 = st.columns(2)
        with col4:
            fig1 = go.Figure(data=[go.Sankey(
              node = dict(
                pad = 15,
                thickness = 20,
                line = dict(color = "black", width = 0.5),
                label = ["Fuente1", "Fuente2", "Fuente 3", "Online", "Offline", "Ingresos Totales"],
                color = "blue"
              ),
              link = dict(
                source = [0, 1, 2, 3, 4], # indices correspond to labels, eg A1, A2, A1, B1, ...
                target = [3, 4, 3, 5, 5],
                value = [8, 4, 5, 13, 4]
            ))])
          
            fig1.update_layout(title_text="Ingresos", font_size=10)
            st.plotly_chart(fig1, theme="streamlit")
        
        with col5:
            fig1 = go.Figure(data=[go.Sankey(
              node = dict(
                pad = 15,
                thickness = 20,
                line = dict(color = "black", width = 0.5),
                label = ["Egresos Totales", "Necesidades", "Gastos", "Inversiones", "Vivienda", "Estudio", "Alimentación", "Transporte", "Entretenimiento", "Viajes", "Acciones", "Activos", "Criptomonedas", "Bonos"],
                color = "red"
              ),
              link = dict(
                source = [0, 0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 3, 3], # indices correspond to labels, eg A1, A2, A1, B1, ...
                target = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
                value = [44, 44, 44, 10, 20, 10, 22, 22, 10, 14, 10, 10, 10]
            ))])
          
            fig1.update_layout(title_text="Gastos", font_size=10)
            st.plotly_chart(fig1, theme="streamlit")
    
        
        col1, col2, col3 = st.columns(3)
        with col1:
          acelerometro1 = {
                "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
                "series": [
                    {
                        "name": "Pressure",
                        "type": "gauge",
                        "axisLine": {
                            "lineStyle": {
                                "width": 10,
                            },
                        },
                        "progress": {"show": "true", "width": 10},
                        "detail": {"valueAnimation": "true", "formatter": "{value}"},
                        "data": [{"value": 50, "name": "Liquidez"}],
                    }
                ],
            }
        
          st_echarts(options=acelerometro1)
        
        with col2:
          acelerometro2 = {
                "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
                "series": [
                    {
                        "name": "Pressure",
                        "type": "gauge",
                        "axisLine": {
                            "lineStyle": {
                                "width": 10,
                            },
                        },
                        "progress": {"show": "true", "width": 10},
                        "detail": {"valueAnimation": "true", "formatter": "{value}"},
                        "data": [{"value": 85, "name": "Endeudamiento"}],
                    }
                ],
            }
        
          st_echarts(options=acelerometro2)
            
        with col3:
          acelerometro3 = {
                "tooltip": {"formatter": "{a} <br/>{b} : {c}%"},
                "series": [
                    {
                        "name": "Pressure",
                        "type": "gauge",
                        "axisLine": {
                            "lineStyle": {
                                "width": 10,
                            },
                        },
                        "progress": {"show": "true", "width": 10},
                        "detail": {"valueAnimation": "true", "formatter": "{value}"},
                        "data": [{"value": 20, "name": "Solvencia"}],
                    }
                ],
            }
          st_echarts(options=acelerometro3)


