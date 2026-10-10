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
    
    st.dataframe(data, use_column_width=True)

    fig = px.bar(data, x="Evento", y="Anomalia_Maxima", color="Intensidad", title="Anomalía Térmica Máxima (°C)")
    st.plotly_chart(fig, use_column_width=True)

elif anio_estudio == "1982 - 1983":
    st.header("📌 Detalle del Evento: 1982 - 1983 (El Niño Global Extraordinario)")
    st.write("""
    * **Magnitud e Impacto:** Considerado uno de los eventos más destructivos del siglo XX a nivel global y nacional. Las anomalías térmicas superficiales del mar superaron los **+4.5°C** en la costa norte (Piura y Tumbes).
    * **Consecuencias Climáticas:** Lluvias torrenciales extraordinarias que transformaron zonas áridas, desbordes masivos de ríos e inundaciones. Paradójicamente, provocó sequías severas e irreversibles en el sur andino del Perú.
    * **Impacto Socioeconómico:** Colapso temporal de la industria pesquera (migración profunda de la anchoveta) y pérdidas catastróficas en la agricultura de exportación y autoconsumo.
    """)

elif anio_estudio == "1997 - 1998":
    st.header("📌 Detalle del Evento: 1997 - 1998 (El Niño Global Extraordinario)")
    st.write("""
    * **Magnitud e Impacto:** Alcanzó anomalías térmicas récord de hasta **+5.0°C** en el Pacífico oriental. Fue el primer fenómeno pronosticado con modelos científicos modernos por el ENFEN, permitiendo mitigación anticipada.
    * **Consecuencias Climáticas:** Formación de lagunas temporales en el desierto de Sechura, precipitaciones intensas en toda la costa norte y centro, y alteración drástica de los patrones de viento y humedad atmosférica.
    * **Impacto Socioeconómico:** Severos daños en la infraestructura vial (puentes caídos, carreteras interrumpidas) y reestructuración de planes de prevención de desastres en el Estado peruano.
    """)

elif anio_estudio == "2017 (El Niño Costero)":
    st.header("📌 Detalle del Evento: 2017 (El Niño Costero Atípico)")
    st.write("""
    * **Magnitud e Impacto:** Un fenómeno focalizado e intenso frente al norte peruano y ecuatoriano (Región Niño 1+2), impulsado por el debilitamiento de los vientos alisios y la llegada de ondas Kelvin cálidas. La anomalía máxima alcanzó **+3.2°C**.
    * **Consecuencias Climáticas:** Lluvias urbanas intensas y repentinas, activación de quebradas secas que generaron huaicos sorpresivos en zonas urbanas altamente pobladas, incluyendo Lima (Chosica, Huachipa), Trujillo y Chiclayo.
    * **Impacto Socioeconómico:** Afectación directa a miles de damnificados urbanos, colapso de redes de saneamiento y pérdidas en viviendas precarias y áreas de cultivo costero.
    """)

elif anio_estudio == "2023 - 2024":
    st.header("📌 Detalle del Evento: 2023 - 2024 (Impacto Reciente y Combinado)")
    st.write("""
    * **Magnitud e Impacto:** Caracterizado por la superposición de condiciones de El Niño Global en el Pacífico central y anomalías cálidas locales persistentes frente a la costa peruana. La anomalía máxima se registró alrededor de **+2.8°C**.
    * **Consecuencias Climáticas:** Olas de calor marino prolongadas durante el invierno y primavera, temperaturas ambientales extremas récord en la costa peruana y retraso en la temporada de lluvias andinas.
    * **Impacto Socioeconómico:** Incremento exponencial de los casos de dengue a nivel nacional debido al aumento de la temperatura ambiental, junto con alertas tempranas para el sector agrícola y pesquero.
    """)

st.divider()
st.subheader("🌾 Sectores Afectados")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("### 🌱 Agricultura")
    st.write("Estrés hídrico, plagas por aumento de temperatura y pérdidas en cultivos clave como papa, maíz y algodonero.")
with col2:
    st.markdown("### 🐟 Pesca")
    st.write("Migración temporal de la anchoveta hacia aguas profundas o al sur, afectando la producción de harina y aceite de pescado.")
with col3:
    st.markdown("### 🏥 Salud")
    st.write("Proliferación de vectores de enfermedades infecciosas y endémicas, con brotes históricos de dengue en múltiples regiones.")

st.divider()
st.subheader("📚 Referencias Bibliográficas y Fuentes Confiables")
st.write("1. **ENFEN** (2024). *Informes técnicos sobre la evolución de El Niño Costero y Global.*")
st.write("2. **MINAM** (2014). *Dossier: El Fenómeno El Niño en el Perú - Causas, historia e impactos.*")
st.write("3. **SENAMHI** (2023-2026). *Reportes meteorológicos, anomalías térmicas y de precipitaciones oficiales.*")
st.write("4. **Banco Central de Reserva del Perú - BCRP** (2022). *Revista Moneda N° 170: Análisis macroeconómico de los choques climáticos.*")

st.divider()
st.caption("Dashboard Académico e Informativo | Desarrollado para Análisis Climático en el Perú 🇵🇪")
