#Agregamos streamlit a nuestro servidor
from seaborn.palettes import dark_palette
import streamlit as st
#Agregamos librerias necesarias
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
#Embellecemos con seaborn
sns.set_style("darkgrid")
#Titulo de la app
st.title("Visualización de casos COVID-19 Chile 2021")
#Texto de bienvenida
st.markdown('### Bienvenido al visualizador (Mostrando los primeros 10 datos disponibles)')
#Cargamos los datos
df = pd.read_csv("https://raw.githubusercontent.com/MinCiencia/Datos-COVID19/master/output/producto3/TotalesPorRegion.csv")
#Mostramos los 10 primeros datos de la tabla
st.dataframe(df.head(10))
#Agregaremos 2 columnas
col1,col2 = st.columns(2)
#Seleccionamos la región
with col1:
    region = st.radio("Región", df.Region.unique())
#Seleccionamos categoría
with col2:
    categoria = st.radio("Categoría", df.Categoria.unique())
#Imprimimos las selecciones
st.markdown("### Mostrando los "+categoria +" de la región: "+region)
#Graficamos
ilocs=df.iloc[:,2:-1]
super_filtro = df[(df.Region==region)&(df.Categoria==categoria)]
#st.table(ilocs.head(10))
st.table(super_filtro)
fig,ax = plt.subplots()
to_plot = super_filtro.iloc[:,2:-1]
ax.plot(to_plot.T)
ax.set_title(region)
ax.set_ylabel(categoria)
ax.set_xlabel("Fecha")
xs = np.arange(0,super_filtro.shape[1]-2,30)
plt.xticks(xs,rotation=90)
st.pyplot(fig)
