import streamlit as st
import pandas as pd

# Criação do DataFrame
dados = {
    'nomeServidor': ['Carlos', 'Ana', 'Marcos'],
    'salario': [3500, 4200, 3900]
}
df = pd.DataFrame(dados)

# Título da aplicação
st.title("Seleção de Servidores")

# Criação do multiselect com os nomes dos servidores
servidores_selecionados = st.multiselect(
    'Escolha o(s) servidor(es):',
    options=df['nomeServidor'].tolist()
)

# Exibir os servidores selecionados
st.write("Servidores selecionados:", servidores_selecionados)
