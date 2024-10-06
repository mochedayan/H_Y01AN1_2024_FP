import streamlit as st

#titulo de la aplicación
st.title("Introducción a variables y tipos de datos en Python")

#creando descripción inicial
st.write("Python es un lenguaje de programación dinámico donde ...")

#Sección para variable de tipo entero
st.header("Ejemplo 1: Enteros")
st.write("En python, un entero (integrer) es un número sin decimales por ejemplo:")

#Definir una variable
int_variable = 42
st.code(f"int_variable = {int_variable} # Tipo: {Type(int_variable)}")