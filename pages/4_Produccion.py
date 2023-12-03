import streamlit as st


st.set_page_config(
  page_title="Novus Mando Chains",
  page_icon="🏭",
  layout="wide"
)

st.write("""
# 🎮 Novus Mando 🚚 Supply Chain 🏭 PRODUCCIÓN
""")

st.sidebar.markdown("Desarrollado por [Novus Mando] (www.novussolutions.io)")

b = st.selectbox("Selecciona el módulo de análisis 🔎:", ("Estrategia Gobernanza de Datos", "Datos Históricos", "Datos en Tiempo Real", "Sistemas de Alarmas", "Sistemas de Recomendaciones"), index=None, placeholder="Choose an option")
