import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') #leer los datos
hist_button = st.button ('construir histograma') # crear un boton
disp_button = st.button ('construir diagrama de dispersion') # crear un boton

if hist_button: # al hacer clic en el boton
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    
    #mostrar un grafico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if disp_button: # al hacer clic en el boton
    # escribir un mensaje
    st.write("creacion de un diagrama de dispersion para el conjunto de anuncios de venta de coches")
    
    #crear un histograma
    fig2 = px.scatter(car_data, x="odometer", y="price")
    
    # mostrar un grafico Plotly interactivo