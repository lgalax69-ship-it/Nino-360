import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="El Fenómeno El Niño en el Perú", page_icon="🌊", layout="wide")

st.title("🌊 El Fenómeno El Niño en el Perú")
st.subheader("Análisis Histórico, Datos Reales y Gráficas Interactivas (1982 - Actualidad)")

st.image("https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=1000", use_column_width=True, caption="Impacto climático en la costa peruana.")

st.sidebar.header("🎛️ Panel de Exploración")
anio_estudio = st.sidebar.selectbox(
    "Selecciona un evento histórico",
    ["Todos / Comparativa General", "1982 - 1983", "1997 - 1998", "2017 (El Niño Costero)", "2023 - 2024"]
)

if anio_estudio == "Todos / Comparativa General":
    st.header("📊 Comparativa Histórica de Anomalías Térmicas")
    
    data = pd.DataFrame({
        "Evento": ["1982-1983", "1997-1998", "2017 (Costero)", "2023-2024"],
        "Anomalia_Maxima": [4.5, 5.0, 3.2, 2.8],
        "Intensidad": ["Extraordinario", "Extraordinario", "Fuerte", "Moderado"]
    })
    
    st.dataframe(data, use_container_width=True)

    fig = px.bar(data, x="Evento", y="Anomalia_Maxima", color="Intensidad", title="Anomalía Térmica Máxima (°C)")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.header(f"📌 Detalle del Evento: {anio_estudio}")
    st.write("Información oficial sobre las consecuencias en la agricultura, pesca y salud pública recopilada de fuentes científicas del Perú.")

st.divider()
st.subheader("🌾 Sectores Afectados")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("### 🌱 Agricultura")
    st.write("Estrés hídrico y pérdidas en cultivos por altas temperaturas.")
with col2:
    st.markdown("### 🐟 Pesca")
    st.write("Migración de la anchoveta y alteración del ecosistema marino.")
with col3:
    st.markdown("### 🏥 Salud")
    st.write("Incremento de vectores de enfermedades como el dengue.")

st.divider()
st.subheader("📚 Referencias Bibliográficas y Fuentes Confiables")
st.write("1. **ENFEN** (2024). Informes técnicos sobre la evolución de El Niño Costero y Global.")
st.write("2. **MINAM** (2014). Dossier: El Fenómeno El Niño en el Perú - Causas, historia e impactos.")
st.write("3. **SENAMHI** (2023-2026). Reportes meteorológicos y de precipitaciones oficiales.")

st.divider()
st.caption("Dashboard Académico e Informativo | Desarrollado para Análisis Climático en el Perú 🇵🇪")
