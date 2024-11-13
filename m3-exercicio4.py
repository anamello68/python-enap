import streamlit as st

# criando elementos gráficos
'''Informar como colher os dados através de variáveis'''
x = st.checkbox('Sim')
st.write(x)

# fazer o mesmo com alguns dos comandos abaixo
st.title(x)
st.button('Clique')
st.radio('Selecione seu gênero',['Masculino','Feminino'])
st.selectbox('Selecione seu gênero',['Masculino','Feminino'])
st.multiselect('Escolha um departamento',['DCS', 'DE', 'DIR'])
st.select_slider('Selecione uma resposta', ['Ruim', 'Bom', 'Excelente'])
st.slider('Selecione um número', 0,50)
st.number_input('Selecione um número', 0,10)
st.text_input('Endereço de e-mail')
st.date_input('Data de viagem')
st.time_input('Tempo de escola')
st.text_area('Descrição')
st.file_uploader('Atualize uma foto')
st.color_picker('Escolha sua cor favorita')

# mensagens de status
st.success("Você conseguiu!")
st.error("Erro!")
st.warning("Advertência")
st.info("Esta é uma informação")
