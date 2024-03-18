import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Hola")

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

hist_button = st.button('Construir histograma') # crear un botón
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    # use_container_width=True:  útil para garantizar que el gráfico se ajuste correctamente al diseño de la página y se vea bien en diferentes tamaños de pantalla.

scatter_button=st.button("Construir gráfico de dispersión")
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig_2 = px.scatter(car_data, x="odometer", y="price") # crear un gráfico de dispersión
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_2, use_container_width=True)
    # use_container_width=True:  útil para garantizar que el gráfico se ajuste correctamente al diseño de la página y se vea bien en diferentes tamaños de pantalla.

