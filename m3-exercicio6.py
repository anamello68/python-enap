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

# Agrupar por estado e contar o número de comunidades
comunidades_por_estado = df.groupby('NM_UF').size().sort_values(ascending=False)
    
# Plotar o gráfico de barras
fig, ax = plt.subplots(figsize=(10, 6))
comunidades_por_estado.plot(kind='bar', color='skyblue', ax=ax)
ax.set_title('Número de Comunidades por Estado')
ax.set_xlabel('Estado')
ax.set_ylabel('Número de Comunidades')
plt.xticks(rotation=45)
plt.tight_layout()
    
# Exibir o gráfico no Streamlit
st.pyplot(fig)
