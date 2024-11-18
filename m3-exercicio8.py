import requests
import pandas as pd
import streamlit as st

url = 'https://dadosabertos.camara.leg.br/api/v2/deputados?ordem=ASC&ordenarPor=nome'
resposta = requests.get(url)
dados = resposta.json()
df = pd.DataFrame(dados['dados'])
st.write("Tabela completa de deputados")
st.write(df)

# Criar uma coluna que combina 'id' e 'nome'
df['id_nome'] = df['id'].astype(str) + ' - ' + df['nome']

# Usar o selectbox para mostrar a coluna 'id_nome'
selected = st.selectbox('Selecione um ID', df['id_nome'])

# Extrair o id a partir da seleção
selected_id = selected.split(' - ')[0].strip()

# Exibir o id selecionado
st.write(f'ID Selecionado: {selected_id}')

dadosFiltrados = df[df['id'] == selected_id]
st.write(dadosFiltrados)
