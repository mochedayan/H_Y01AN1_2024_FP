import streamlit as st

#ejercicio5:generar e imprimir los números pares entre 0 y 100
st.title("ejercicio de números impares")

st.subheader("Ejercicio 5: Números pares entre 0 y 100")
pares_0_100 = [i for i in range(0,101) if i %2 == 0]
st.write("Números pares entre 0 y 100:")
st.write(pares_0_100)