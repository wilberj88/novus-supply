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
import altair as alt
import plotly.express as px


#######################
# Page configuration
st.set_page_config(
  page_title="Novus Mando Chains",
  page_icon="🏭",
  layout="wide"
)
alt.themes.enable("dark")

#######################
# CSS styling
st.markdown("""
<style>

[data-testid="block-container"] {
    padding-left: 2rem;
    padding-right: 2rem;
    padding-top: 1rem;
    padding-bottom: 0rem;
    margin-bottom: -7rem;
}

[data-testid="stVerticalBlock"] {
    padding-left: 0rem;
    padding-right: 0rem;
}

[data-testid="stMetric"] {
    background-color: #393939;
    text-align: center;
    padding: 15px 0;
}

[data-testid="stMetricLabel"] {
  display: flex;
  justify-content: center;
  align-items: center;
}

[data-testid="stMetricDeltaIcon-Up"] {
    position: relative;
    left: 38%;
    -webkit-transform: translateX(-50%);
    -ms-transform: translateX(-50%);
    transform: translateX(-50%);
}

[data-testid="stMetricDeltaIcon-Down"] {
    position: relative;
    left: 38%;
    -webkit-transform: translateX(-50%);
    -ms-transform: translateX(-50%);
    transform: translateX(-50%);
}

</style>
""", unsafe_allow_html=True)



#######################
# Title
st.write("""
# 🎮 Novus Mando 🚚 Supply Chain 🏭 Home
""")

st.sidebar.markdown("Desarrollado por [Novus Mando] (www.novussolutions.io)")


a = st.selectbox("Selecciona qué quieres optimizar con tu Mando 🎮:", ("Ingresos", "Costos", "Rentabilidad", "Sostenibilidad"), index=None, placeholder="Choose an option")
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

  if b == "Datos en Tiempo Real":
    current_time = time.ctime()
    st.write("In real time monitoring at: ", current_time)

    st.header('Tendencias y Climas Mundiales 🌎')

    colored_header(
        label="Búsquedas online en Google",
        description="Última hora y día",
        color_name="violet-70",
    )

    pytrends = TrendReq(hl='en-US', tz=360)
    col4, col5, col6 = st.columns(3)
    with col4:
        st.write("🇺🇸 USA Top10 Trending Search in last hour")
          # Google Trends data
        df1 = pytrends.trending_searches(pn='united_states')
        st.dataframe(df1.head(10))
    with col5:
        st.write("🇬🇧 UK Top10 Trending Search in last hour")
          # Google Trends data
        df2 = pytrends.trending_searches(pn='united_kingdom')
        st.dataframe(df2.head(10))
    with col6:
        st.write("🇨🇴 COL Top10 Trending Search in last hour")
        df3 = pytrends.trending_searches(pn='colombia')
        st.dataframe(df3.head(10))





    colored_header(
        label="Wheater Now",
        description="América, EU & ASIA",
        color_name="red-70",
    )

    #ALARMS CONFIGURATION
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    API_KEY = "146090ad17fa8843bc9eca97c53926b4"
    sity1 = "New York"
    sity2 = "Bogota"
    sity3 = "Toledo"
    sity4 = "London"
    sity5 = "Pekin"
    sity6 = "Bombai"
    URL1 = BASE_URL + "q=" + sity1 + "&appid=" + API_KEY
    URL2 = BASE_URL + "q=" + sity2 + "&appid=" + API_KEY
    URL3 = BASE_URL + "q=" + sity3 + "&appid=" + API_KEY
    URL4 = BASE_URL + "q=" + sity4 + "&appid=" + API_KEY
    URL5 = BASE_URL + "q=" + sity5 + "&appid=" + API_KEY
    URL6 = BASE_URL + "q=" + sity6 + "&appid=" + API_KEY


    response1 = requests.get(URL1)
    response2 = requests.get(URL2)
    response3 = requests.get(URL3)
    response4 = requests.get(URL4)
    response5 = requests.get(URL5)
    response6 = requests.get(URL6)

    if response1.status_code == 200:
       # getting data in the json format
       data1 = response1.json()
       # getting the main dict block
       main1 = data1['main']
      # getting temperature
       temperature1 = main1['temp']
       # getting the humidity
       humidity1 = main1['humidity']
       # getting the pressure
       pressure1 = main1['pressure']
       # weather report
       report1 = data1['weather']

    if response2.status_code == 200:
       # getting data in the json format
       data2 = response2.json()
       # getting the main dict block
       main2 = data2['main']
      # getting temperature
       temperature2 = main2['temp']
       # getting the humidity
       humidity2 = main2['humidity']
       # getting the pressure
       pressure2 = main2['pressure']
       # weather report
       report2 = data2['weather']

    if response3.status_code == 200:
       # getting data in the json format
       data3 = response3.json()
       # getting the main dict block
       main3 = data3['main']
      # getting temperature
       temperature3 = main3['temp']
       # getting the humidity
       humidity3 = main3['humidity']
       # getting the pressure
       pressure3 = main3['pressure']
       # weather report
       report3 = data3['weather']

    if response4.status_code == 200:
       # getting data in the json format
       data4 = response4.json()
       # getting the main dict block
       main4 = data4['main']
      # getting temperature
       temperature4 = main4['temp']
       # getting the humidity
       humidity4 = main4['humidity']
       # getting the pressure
       pressure4 = main4['pressure']
       # weather report
       report4 = data4['weather']

    if response5.status_code == 200:
       # getting data in the json format
       data5 = response5.json()
       # getting the main dict block
       main5 = data5['main']
      # getting temperature
       temperature5 = main5['temp']
       # getting the humidity
       humidity5 = main5['humidity']
       # getting the pressure
       pressure5 = main5['pressure']
       # weather report
       report5 = data5['weather']

    if response6.status_code == 200:
       # getting data in the json format
       data6 = response6.json()
       # getting the main dict block
       main6 = data6['main']
      # getting temperature
       temperature6 = main6['temp']
       # getting the humidity
       humidity6 = main6['humidity']
       # getting the pressure
       pressure6 = main6['pressure']
       # weather report
       report6 = data6['weather']

    col4, col5, col6 = st.columns(3)

    with col4:
        st.write("🌧 USA ☀️")
        st.write(f"{sity1:-^30}")
        st.write(f"Temperature (Kelvins): {temperature1}")
        st.write(f"Humidity: {humidity1}")
        st.write(f"Pressure: {pressure1}")
        st.write(f"Weather Report: {report1[0]['description']}")
        st.write(f"{sity2:-^30}")
        st.write(f"Temperature (Kelvins): {temperature2}")
        st.write(f"Humidity: {humidity2}")
        st.write(f"Pressure: {pressure2}")
        st.write(f"Weather Report: {report2[0]['description']}")

    with col5:
        st.write("🌧 Europe ☀️")
        st.write(f"{sity3:-^30}")
        st.write(f"Temperature (Kelvins): {temperature3}")
        st.write(f"Humidity: {humidity3}")
        st.write(f"Pressure: {pressure3}")
        st.write(f"Weather Report: {report3[0]['description']}")
        st.write(f"{sity4:-^30}")
        st.write(f"Temperature (Kelvins): {temperature4}")
        st.write(f"Humidity: {humidity4}")
        st.write(f"Pressure: {pressure4}")
        st.write(f"Weather Report: {report4[0]['description']}")

    with col6:
        st.write("🌧 Asia ☀️")
        st.write(f"{sity5:-^30}")
        st.write(f"Temperature (Kelvins): {temperature5}")
        st.write(f"Humidity: {humidity5}")
        st.write(f"Pressure: {pressure5}")
        st.write(f"Weather Report: {report5[0]['description']}")
        st.write(f"{sity6:-^30}")
        st.write(f"Temperature (Kelvins): {temperature6}")
        st.write(f"Humidity: {humidity6}")
        st.write(f"Pressure: {pressure6}")
        st.write(f"Weather Report: {report6[0]['description']}")

  if b == "Sistemas de Alarmas":
    colored_header(
      label="Mando 3: Alarmas Operativas, Financieras y Comerciales",
      description="Procesos, Indicadores y Monitoreo",
      color_name="violet-70",
