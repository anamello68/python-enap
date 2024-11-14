import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
#import altair as alt

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

qtdeMunicipios = len(df['NM_MUNIC'].unique())
st.write("A quantidade de municípios com localização quilombola é " + str(qtdeMunicipios))

qtdeComunidades = len(df['NM_AGLOM'].unique())
st.write("A quantidade de comunidades quilombolas é " + str(qtdeComunidades))

st.header('Número de comunidades por UF')
st.bar_chart(df['NM_UF'].value_counts())

uf_counts = df['NM_UF'].value_counts().sort_values(ascending=False)
uf_counts_df = pd.DataFrame({'UF': uf_counts.index, 'Quantidade': uf_counts.values})

# Cria um gráfico de barras ordenado com Altair
chart = alt.Chart(uf_counts_df).mark_bar(color="skyblue").encode(
    x=alt.X('Quantidade:Q', title='Quantidade de Comunidades'),
    y=alt.Y('UF:N', sort='-x', title='Unidade Federativa')
).properties(
    title="Número de comunidades por UF - ordenado"
)

# Exibe o gráfico de barras com Streamlit
st.altair_chart(chart, use_container_width=True)

st.header('Os dez municípios com mais comunidades quilombolas')
st.bar_chart(df['NM_MUNIC'].value_counts()[:10])

numero = st.slider('Selecione um número de linhas a serem exibidas', min_value = 0, max_value = 100)
st.write(df.head(numero))
