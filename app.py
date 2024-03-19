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

# # Filtrado de datos
# st.sidebar.header('Filtrar Datos')
# marca = st.sidebar.selectbox('Seleccionar Marca', car_data['model'].unique())
# filtro_marca = car_data[car_data['model'] == marca]

st.subheader('Analicemos un poco el precio')

# Estadísticas descriptivas del precio
st.subheader("Estadísticas descriptivas del precio")
st.write(f"Precio promedio: {round(car_data['price'].mean())}")
st.write(f"Mediana del precio: {round(car_data['price'].median())}")
st.write(f"Desviación estándar del precio: {round(car_data['price'].std())}")

# Gráfico de caja del precio    
st.subheader("Analizando la distribución del precio")
price_boxplot=px.box(car_data, x='price', labels={"price":"Precio"})
st.plotly_chart(price_boxplot, use_container_width=True)

# # Visualización de datos adicionales
# st.subheader('Gráfico de Barras por Marca')
# fig_bar = px.bar(car_data, x='model', y='price')
# st.plotly_chart(fig_bar)

# Iniciando otra sección
st.subheader('Ahora vamos a conocer más sobre este conjunto de datos')

# Primer botón
build_histogram = st.checkbox('Histograma del kilometraje')
if build_histogram: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Esta es la frecuencia del kilometraje observada en los vehículos')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer", labels={"odometer":"Kilometraje registrado"})
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
    # use_container_width=True:  útil para garantizar que el gráfico se ajuste correctamente al diseño de la página y se vea bien en diferentes tamaños de pantalla.

# Segundo botón
build_scatter=st.checkbox("Relación entre el precio y el kilometraje")
if build_scatter: # al hacer clic en el botón
    # escribir un mensaje
    st.write('¿Notas alguna relación entre el kilometraje y el precio de los vehículos?')
            
    # crear un histograma
    fig_2 = px.scatter(car_data, x="odometer", y="price", labels={"odometer":"Kilometraje","price":"Precio"}) # crear un gráfico de dispersión
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_2, use_container_width=True)
    # use_container_width=True:  útil para garantizar que el gráfico se ajuste correctamente al diseño de la página y se vea bien en diferentes tamaños de pantalla.

# Tercer botón
build_histogram_2=st.checkbox("Distribución del estado de los vehículos ")
if build_scatter: # al hacer clic en el botón
    # escribir un mensaje
    st.write('¿Notas alguna relación entre el kilometraje y el precio de los vehículos?')
            
    # crear un histograma
    fig_3 = px.histogram(car_data, x="condition",labels={"price":"Precio"})
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_3, use_container_width=True)

# Cuarto botón
build_scatter_2=st.checkbox("Relación entre el precio y el año del modelo")
if build_scatter_2: # al hacer clic en el botón
    # escribir un mensaje
    st.write('¿Observas alguna relación clara?')
            
    # crear un histograma
    fig_4 = px.scatter(car_data, x="model_year", y="price",labels={"model_year":"Año del modelo","price":"Precio"}) # crear un gráfico de dispersión
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_4, use_container_width=True)
    # use_container_width=True:  útil para garantizar que el gráfico se ajuste correctamente al diseño de la página y se vea bien en diferentes tamaños de pantalla.

# Quinto botón
build_circle=st.checkbox("Distribución de tipos de combustible")
if build_circle: # al hacer clic en el botón
    # escribir un mensaje
    st.write('¿Cuál es el tipo de combustible aceptado con mayor presencia en el conjunto de datos?')
            
    # crear un histograma
    fig_pie = px.pie(car_data, names='fuel',labels={"fuel":"Combustible"})
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_pie, use_container_width=True)


