import streamlit as st
import pandas as pd

# Título da aplicação
st.title("Carregamento de Dados de Servidores")

# Upload do arquivo CSV
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")

# Verifica se o arquivo foi carregado
if uploaded_file is not None:
    # Leitura do arquivo para um DataFrame
    df = pd.read_csv(uploaded_file)
    
    # Exibe o DataFrame
    st.write("Dados dos Servidores:")
    st.dataframe(df)

    # Criação do multiselect para selecionar os nomes dos servidores
    servidores_selecionados = st.multiselect(
        'Escolha o(s) servidor(es):',
        options=df['Nome'].tolist() if 'Nome' in df.columns else []
    )
    df_filtrado = df[df['Nome'] == servidores_selecionados]
    # Exibir os servidores selecionados
    st.write("Servidores selecionados:", df_filtrado)
