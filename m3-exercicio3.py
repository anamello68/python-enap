import streamlit as st

# Título da aplicação
st.title("Avaliação de Satisfação do Cliente")

# Cria um seletor deslizante com valores de 0 a 100
satisfacao = st.select_slider(
    'Qual é o seu grau de satisfação?',
    options=range(0, 101),  # Escala de 0 a 100
    value=50  # Valor inicial no meio da escala
)

# Mostra a resposta do cliente
st.write(f"Grau de satisfação do cliente: {satisfacao}")
