import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import requests

# Buscar as deputadas - siglaSexo=F
url = 'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=F&ordem=ASC&ordenarPor=nome'
resposta = requests.get(url)
dados = resposta.json()
df_mulheres = pd.DataFrame(dados['dados'])
# Criar a coluna sexo para fazer os filtros
df_mulheres['sexo'] = 'F'

# Buscar os deputados - siglaSexo=M
url = 'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=M&ordem=ASC&ordenarPor=nome'
resposta = requests.get(url)
dados = resposta.json()
df_homens = pd.DataFrame(dados['dados'])
# Criar a coluna sexo para fazer os filtros
df_homens['sexo'] = 'M'

# Concatenar os dataframes
df = pd.concat([df_mulheres, df_homens])

# Mostrar o dataframe completo
st.write("Tabela completa de deputados")
st.write(df)

# Selecionar os deputados por gênero
opcao = st.selectbox(
    'Qual gênero você gostaria de selecionar?',
     df['sexo'].unique())

st.write('Você selecionou: ', opcao)

# Mostrar o dataframe filtrado por gênero
dadosFiltrados = df[df['sexo'] == opcao]

if st.checkbox('Mostrar tabela'):
  st.write(dadosFiltrados)

st.header('Nº de Deputados por gênero')

# Obter os dados de forma adequada
sexo_counts = df['sexo'].value_counts()

fig, ax = plt.subplots()
# Passar os índices como eixo Y e os valores como eixo X
ax.barh(sexo_counts.index, sexo_counts.values, color='skyblue')
ax.set_xlabel("Nº de Deputados(as)")
ax.set_ylabel("Gênero")
ax.set_title("Nº de Deputados por gênero")

# Exibir no Streamlit
st.pyplot(fig)
#st.bar_chart(df['sexo'].value_counts())

