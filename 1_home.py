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

a = st.selectbox("Selecciona un Mando 🎮 🚚 Supply Chain 🏭", ("Demanda", "Inventario", "Producción", "Almacenamiento", "Distribución", "Comercialización", "Ventas", "PostVentas", "Finanzas", "Impacto"), index=None, placeholder="Choose an option")

if a:
  b = st.selectbox("Selecciona el módulo de análisis 🔎", ("Histórico y 2024", "Estrategia", "Alarmas", "Recomendaciones"), index=None, placeholder="Choose an option")
