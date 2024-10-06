import streamlit as st

#titulo de la aplicación
st.title("Introducción a variables y tipos de datos en Python")

#creando descripción inicial
st.write("Python es un lenguaje de programación dinámico donde ...")

#Sección para variable de tipo entero
st.header("Ejemplo 1: Enteros")
st.write("En python, un entero (integer) es un número sin decimales por ejemplo:")

#input para que el usuario pueda ingresar un number
int_variable = st.number_input("Ingrese un número entero:", value = 42, step = 1)

#mostrando el valor
st.code("int_variable = {int_variable} # Tipo: {Type(int_variable)}")