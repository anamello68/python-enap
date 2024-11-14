import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import altair as alt

url = 'https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv'

df = pd.read_csv(url)

st.title('Localização das comunidades quilombolas (2022)') 

# Exibe o DataFrame
st.write("Dados dos Quilombolas:")
st.dataframe(df)

df.drop(columns=['Unnamed: 0'], inplace=True)
list = ['Lat_d', 'Long_d']
# Convertendo para numeros
df[list] = df[list].apply(pd.to_numeric, errors='coerce')

# Dicionário com os estados e suas respectivas siglas
estados_siglas = {
    'ACRE': 'AC',
    'ALAGOAS': 'AL',
    'AMAPÁ': 'AP',
    'AMAZONAS': 'AM',
    'BAHIA': 'BA',
    'CEARÁ': 'CE',
    'ESPÍRITO SANTO': 'ES',
    'GOIÁS': 'GO',
    'MARANHÃO': 'MA',
    'MATO GROSSO': 'MT',
    'MATO GROSSO DO SUL': 'MS',
    'MINAS GERAIS': 'MG',
    'PARÁ': 'PA',
    'PARAÍBA': 'PB',
    'PARANÁ': 'PR',
    'PERNAMBUCO': 'PE',
    'PIAUÍ': 'PI',
    'RIO DE JANEIRO': 'RJ',
    'RIO GRANDE DO NORTE': 'RN',
    'RIO GRANDE DO SUL': 'RS',
    'RONDÔNIA': 'RO',
    'RORAIMA': 'RR',
    'SANTA CATARINA': 'SC',
    'SÃO PAULO': 'SP',
    'SERGIPE': 'SE',
    'TOCANTINS': 'TO'
}

estados_siglas2 = {
    'Acre': 'AC',
    'Alagoas': 'AL',
    'Amapá': 'AP',
    'Amazonas': 'AM',
    'Bahia': 'BA',
    'Ceará': 'CE',
    'Espírito Santo': 'ES',
    'Goiás': 'GO',
    'Maranhão': 'MA',
    'Mato Grosso': 'MT',
    'Mato Grosso do Sul': 'MS',
    'Minas Gerais': 'MG',
    'Pará': 'PA',
    'Paraíba': 'PB',
    'Paraná': 'PR',
    'Pernambuco': 'PE',
    'Piauí': 'PI',
    'Rio de Janeiro': 'RJ',
    'Rio Grande do Norte': 'RN',
    'Rio Grande do Sul': 'RS',
    'Rondônia': 'RO',
    'Roraima': 'RR',
    'Santa Catarina': 'SC',
    'São Paulo': 'SP',
    'Sergipe': 'SE',
    'Tocantins': 'TO'
}

# Criação da nova coluna 'Sigla_UF' usando o dicionário
df['SIGLA_UF'] = df['NM_UF'].map(estados_siglas)

# Criar uma nova coluna concatenando o nome do município com a sigla do Estado
df['NM_MUNIC_UF'] = df['NM_MUNIC'] + ' - ' + df['SIGLA_UF']

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

# Cria um gráfico de barras com rótulos sobre as barras
bar_chart = alt.Chart(uf_counts_df).mark_bar(color="skyblue").encode(
    x=alt.X('Quantidade:Q', title='Quantidade de Comunidades'),
    y=alt.Y('UF:N', sort='-x', title='Unidade Federativa')
).properties(
    title="Número de comunidades por UF - ordenado"
)

# Adiciona rótulos sobre as barras
text = bar_chart.mark_text(
    align='center',  # Alinha o texto no centro da barra
    baseline='middle',  # Alinha verticalmente ao meio da barra
    fontSize=12,  # Define o tamanho da fonte
    color='black'  # Cor do texto
).encode(
    text='Quantidade:Q'  # Coloca o valor da 'Quantidade' como o texto
)

# Junta o gráfico de barras com os rótulos
chart = bar_chart + text

# Exibe o gráfico de barras com Streamlit
st.altair_chart(chart, use_container_width=True)

st.header('Os dez municípios com mais comunidades quilombolas')
st.bar_chart(df['NM_MUNIC_UF'].value_counts()[:10])
df['NM_UF'].value_counts().sort_values(ascending=False).values[0]

col1, col2, col3 = st.columns(3)
col1.metric('# Municípios', len(df['NM_MUNIC'].unique()))
col2.metric('# Comunidades', len(df['NM_AGLOM'].unique()))
col3.metric(df['NM_UF'].value_counts().sort_values(ascending=False).index[0], df['NM_UF'].value_counts().sort_values(ascending=False).values[0])

numero = st.slider('Selecione um número de linhas a serem exibidas', min_value = 0, max_value = 100, value=10)
st.write(df.head(numero))
