import streamlit as st


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
  b = st.selectbox("Selecciona el módulo de análisis 🔎:", ("Estrategia Gobernanza de Datos", "Datos Históricos", "Datos en Tiempo Real", "Modelaciones Predictivas", "Sistemas de Alarmas", "Sistemas de Recomendaciones"), index=None, placeholder="Choose an option")
