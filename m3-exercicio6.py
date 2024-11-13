import pandas as pd
import streamlit as st

url = 'https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv'

df = pd.read_csv(url)
df.head()

st.title('Localização das comunidades quilombolas (2022)')  
