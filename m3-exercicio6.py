import pandas as pd
import streamlit as st

url = 'https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv'

df = pd.read_csv(url)

st.title('Localização das comunidades quilombolas (2022)') 

# Exibe o DataFrame
st.write("Dados dos Quilombolas:")
st.dataframe(df)

# Criação do slider para selecionar o número de linhas
num_linhas = st.slider(
    'Selecione o número de linhas para exibir:',
    min_value=1, max_value=len(df), value=3  # Valor padrão = 3
)

# Exibir as primeiras 'num_linhas' linhas do DataFrame
st.write("Visualizando os dados:")
st.dataframe(df.head(num_linhas))
