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
ax.barh(sexo_counts.index, sexo_counts.values, color='red')
ax.set_xlabel("Nº de Deputados(as)")
ax.set_ylabel("Gênero")
ax.set_title("Nº de Deputados por gênero")

# Exibir no Streamlit
st.pyplot(fig)

# Mostra o gráfico como histograma
st.bar_chart(df['sexo'].value_counts())

# Contar número de deputados por estado
contagem_estados = dadosFiltrados['siglaUf'].value_counts()

# Criar gráfico de barras
fig, ax = plt.subplots()
bars = ax.bar(contagem_estados.index, contagem_estados.values, color='skyblue')
ax.set_title(f"Número de deputados {opcao} por estado")
ax.set_xlabel("Estado")
ax.set_ylabel("Número de Deputados(as)")
# Rotacionar os rótulos do eixo X
ax.tick_params(axis='x', rotation=90)

# Adicionar rótulos nas barras
for bar in bars:
    height = bar.get_height()
    ax.text(
        bar.get_x() + bar.get_width() / 2,  # Posição central na barra
        height,                            # Altura do rótulo
        f'{int(height)}',                  # Texto do rótulo
        ha='center',                       # Alinhamento horizontal
        va='bottom',                       # Alinhamento vertical
        fontsize=8                         # Tamanho da fonte reduzido
    )

# Exibir no Streamlit
st.pyplot(fig)

# Contar o número de homens e mulheres por estado
sexo_counts_by_uf = df.groupby(['siglaUf', 'sexo']).size().unstack(fill_value=0)

# Calcular o total de deputados por estado e o total de homens e mulheres
sexo_counts_by_uf['Total'] = sexo_counts_by_uf.sum(axis=1)
sexo_counts_by_uf['Homens'] = sexo_counts_by_uf['M']
sexo_counts_by_uf['Mulheres'] = sexo_counts_by_uf['F']

# Exibir informações no painel
st.header("Total de Deputados por Estado e Sexo")

# Exibir o total de deputados por estado
for sigla, row in sexo_counts_by_uf.iterrows():
    st.subheader(f"Estado: {sigla}")
    st.write(f"Total de Deputados: {row['Total']}")
    st.write(f"Total de Homens: {row['Homens']}")
    st.write(f"Total de Mulheres: {row['Mulheres']}")

# Criar gráfico de barras
fig, ax = plt.subplots()
sexo_counts_by_uf[['Homens', 'Mulheres']].plot(kind='bar', stacked=True, ax=ax, color=['blue', 'pink'])
ax.set_title("Número de Deputados por Sexo")
ax.set_xlabel("Estado")
ax.set_ylabel("Número de Deputados(as)")
ax.set_xticklabels(sexo_counts_by_uf.index, rotation=45, ha="right")

# Exibir no Streamlit
st.pyplot(fig)
