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


