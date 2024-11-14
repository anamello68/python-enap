import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

url = 'https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv'

df = pd.read_csv(url)

st.title('Localização das comunidades quilombolas (2022)') 

# Exibe o DataFrame
st.write("Dados dos Quilombolas:")
st.dataframe(df)

df.drop(columns=['Unnamed: 0'], inplace=True)
list = ['Lat_d', 'Long_d']
# convertendo para numeros
df[list] = df[list].apply(pd.to_numeric, errors='coerce')

estados = sorted(df['NM_UF'].unique())
estadoFiltro = st.selectbox(
    'Qual estado selecionar?',
     estados)
dadosFiltrados = df[df['NM_UF'] == estadoFiltro]

if st.checkbox('Mostrar tabela'):
   st.write(dadosFiltrados)
st.map(dadosFiltrados, latitude="Lat_d", longitude="Long_d")
