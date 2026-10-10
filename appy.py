import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(
    page_title="El Fenómeno El Niño en el Perú",
    page_icon="🌊",
    layout="wide"
)

# Estilos CSS con colores institucionales y cálidos
st.markdown("""
    <style>
    .stApp {
        background-color: #F8F9FA;
    }
    .cover-title {
        color: #C0392B;
        text-align: center;
        font-size: 2.8rem;
        font-weight: bold;
        margin-bottom: 0px;
    }
    .cover-subtitle {
        color: #2980B9;
        text-align: center;
        font-size: 1.4rem;
        margin-bottom: 25px;
    }
    .card {
        background-color: #FFFFFF;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
        border-left: 5px solid #E74C3C;
        margin-bottom: 20px;
    }
    .ref-section {
        background-color: #EAEDED;
        padding: 15px;
        border-radius: 8px;
        font-size: 0.9rem;
    }
    </style>
""", unsafe_allow_html=True)

# Carátula llamativa
st.markdown('<p class="cover-title">🌊 El Fenómeno El Niño en el Perú</p>', unsafe_allow_html=True)
st.markdown('<p class="cover-subtitle">Análisis Histórico, Datos Reales, Comparativas y Gráficas Interactivas (1982 - Actualidad)</p>', unsafe_allow_html=True)

# Imagen ilustrativa desde enlace seguro
st.image("https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=1000", use_column_width=True, caption="Ilustración analítica del impacto climático en la costa peruana.")

st.divider()

# Barra lateral para interactuar
st.sidebar.header("🎛️ Panel de Exploración")
anio_estudio = st.sidebar.selectbox(
    "Selecciona un evento histórico clave",
    ["Todos / Comparativa General", "1982 - 1983 (Extraordinario)", "1997 - 1998 (Extraordinario)", "2017 (El Niño Costero)", "2023 - 2024 (Impacto Reciente)"]
)

region = st.sidebar.selectbox(
    "Filtrar región más afectada",
    ["Todas las regiones costeras", "Piura", "Tumbes", "Lambayeque", "La Libertad", "Ica"]
)

st.sidebar.info("💡 Este dashboard recopila datos oficiales y científicos del ENFEN, SENAMHI y MINAM.")

# Contenido Principal
if anio_estudio == "Todos / Comparativa General":
    st.subheader("📊 Comparativa Histórica de Anomalías Térmicas e Impactos")
    st.write("A continuación, se presenta una base de datos histórica con la anomalía máxima de temperatura superficial del mar (°C) registrada en eventos pasados:")

    # Datos oficiales / históricos clave
    data = pd.DataFrame({
        "Evento / Año": ["1982-1983", "1997-1998", "2017 (Costero)", "2023-2024"],
        "Anomalía Máxima (°C)": [4.5, 5.0, 3.2, 2.8],
        "Intensidad": ["Extraordinario", "Extraordinario", "Fuerte", "Moderado/Fuerte"]
    })
    
    st.dataframe(data, use_container_width=True)

    st.markdown("### 📈 Gráfica Interactiva (Plotly): Anomalías Térmicas por Evento")
    
    # Gráfica interactiva con Plotly
    fig = px.bar(
        data, 
        x="Evento / Año", 
        y="Anomalía Máxima (°C)", 
        color="Intensidad",
        text="Anomalía Máxima (°C)",
        color_discrete_sequence=["#E74C3C", "#F39C12", "#3498DB"]
    )
    fig.update_traces(textposition='outside')
    fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig, use_container_width=True)

else:
    st.subheader(f"📌 Detalle del Evento: {anio_estudio}")
    if "1982" in anio_estudio:
        st.write("El evento de **1982-1983** fue catalogado como uno de los más destructivos del siglo XX. La anomalía térmica superó los +4.5°C en la costa norte, generando lluvias torrenciales récord en Piura y sequías severas en el sur andino.")
    elif "1997" in anio_estudio:
        st.write("El fenómeno de **1997-1998** alcanzó anomalías de hasta +5.0°C en el Pacífico central y oriental. Fue el primer evento pronosticado con modelos científicos modernos, aunque causó graves daños en infraestructura vial y agrícola.")
    elif "2017" in anio_estudio:
        st.write("El **El Niño Costero de 2017** se caracterizó por un calentamiento localizado muy intenso frente al norte peruano (Región Niño 1+2), provocando huaicos e inundaciones sorpresivas en Lima, Trujillo y Piura.")
    else:
        st.write("Los periodos recientes **2023-2024** estuvieron marcados por la superposición de El Niño Global y anomalías cálidas locales, incrementando notablemente los índices de calor extremo y la propagación de vectores como el dengue.")

st.divider()

# Sección de Sectores de Impacto
st.subheader("🌾 Sectores Clave Afectados en el Perú")
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1500937386664-56d1dfef3854?w=500", use_column_width=True)
    st.markdown("#### 🌱 Agricultura y Ganadería")
    st.write("Disminución en rendimientos de cultivos clave como papa y quinua debido al estrés hídrico y plagas por calor.")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1544551763-46a013bb70d5?w=500", use_column_width=True)
    st.markdown("#### 🐟 Pesca y Ecosistemas")
    st.write("La anchoveta migra hacia aguas profundas o al sur, afectando temporalmente la industria pesquera y la fauna marina.")
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1584515979956-d9f6e5d09982?w=500", use_column_width=True)
    st.markdown("#### 🏥 Salud Pública")
    st.write("Incremento de enfermedades sensibles al clima y la temperatura, destacando los brotes de dengue e infecciones.")
    st.markdown('</div>', unsafe_allow_html=True)

st.divider()

# Referencias y Fuentes Oficiales
st.markdown("### 📚 Referencias Bibliográficas y Fuentes Confiables")
st.markdown("""
<div class="ref-section">
1. <b>Comité Multisectorial Encargado del Estudio Nacional del Fenómeno El Niño (ENFEN).</b> (2024). <i>Informes técnicos sobre la evolución de El Niño Costero y Global.</i><br>
2. <b>Ministerio del Ambiente (MINAM).</b> (2014). <i>Dossier: El Fenómeno El Niño en el Perú - Causas, historia e impactos.</i><br>
3. <b>Servicio Nacional de Meteorología e Hidrología del Perú (SENAMHI).</b> (2023-2026). <i>Reportes de precipitaciones y anomalías térmicas.</i><br>
4. <b>Banco Central de Reserva del Perú (BCRP).</b> (2022). Revista Moneda N° 17
