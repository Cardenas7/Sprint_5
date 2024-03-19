import streamlit as st
import pandas as pd
import plotly.express as px

# Título principal
st.header("Análisis de precios de autos")

# Cargamos el dataset
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

# Mostrando el dataset
st.subheader('Este es el conjunto de datos con el que trabaja esta aplicación web')
st.write(car_data)

# Filtrado de datos
st.sidebar.header('Filtrar Datos')
marca = st.sidebar.selectbox('Seleccionar Marca', car_data['model'].unique())
filtro_marca = car_data[car_data['model'] == marca]

# Iniciando otra sección
st.subheader('Ahora vamos a realizar un análisis exploratorio de los datos')

# Primer botón
hist_button = st.button('Construir histograma') # crear un botón
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    # use_container_width=True:  útil para garantizar que el gráfico se ajuste correctamente al diseño de la página y se vea bien en diferentes tamaños de pantalla.

# Segundo botón
scatter_button=st.button("Construir gráfico de dispersión")
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig_2 = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_2, use_container_width=True)
    # use_container_width=True:  útil para garantizar que el gráfico se ajuste correctamente al diseño de la página y se vea bien en diferentes tamaños de pantalla.

