import pandas as pd
import streamlit as st
import numpy as np
st.sidebar.title("dashboard interactivo: Crecimiento del PIB")
st.image("proyecto/assets/uahc.jpg")
st.title("introduccion a programacion en python y r")
pais = st.sidebar.selectbox("Seleccione el pais", ["Alemania", "Australia", "Austria", "Bélgica", "Canadá", "Chile", "Colombia", "Corea, República de", "Costa Rica", "Dinamarca", "República Eslovaca", "Eslovenia", "España", "Estados Unidos", "Estonia", "Finlandia", "Francia", "Grecia", "Hungría", "Irlanda", "Islandia", "Israel", "Italia", "Japón", "Letonia", "Lituania", "Luxemburgo", "México", "Noruega", "Nueva Zelandia", "Países Bajos", "Polonia", "Portugal", "Reino Unido", "República Checa", "Suecia", "Suiza", "Turquía"])
st.sidebar.write("Integrantes:")
st.sidebar.text("Cristian Gatica")
st.sidebar.text("Eloy Cisterna")
df = pd.read_csv('proyecto/datos_ocde.csv')
df_melt = df.melt(
    id_vars=['Country Name', 'Country Code'],
    var_name='Año',
    value_name='PIB',
)
df_melt['Año'] = df_melt['Año'].astype(int)
df_clean = df_melt.dropna(subset=['PIB'])
promedio_ocde = df_clean.groupby('Año')['PIB'].mean()
df_pais = (
    df_clean[df_clean['Country Name'] == pais]
    .set_index('Año')['PIB']
    .rename(pais)
)
df_grafico = pd.concat([df_pais, promedio_ocde.rename('Promedio OCDE')], axis=1)
df_grafico.index = df_grafico.index.astype(str)
st.subheader(f'Crecimiento del PIB: {pais} vs Promedio OCDE')
st.line_chart(df_grafico)
st.markdown("<h3 style='color: red;'>Métricas anuales</h3>", unsafe_allow_html=True)
anio = st.slider("", 1961, 2025, 2010)
pib_pais = df_grafico.loc[str(anio), pais]
pib_prom = df_grafico.loc[str(anio), "Promedio OCDE"]
dif = pib_pais - pib_prom
col1, col2, col3 = st.columns(3)
col1.metric(f"Promedio PIB ({pais})", f"{pib_pais:.1f}")
col2.metric("Promedio PIB General", f"{pib_prom:.1f}")
col3.metric("Diferencia", f"{dif:.1f}")
