from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px


# Configura a página para usar o layout 'wide'
st.set_page_config(layout="wide")

# Carrega os dados
base_pv = pd.read_excel("/Users/thiarly/Library/CloudStorage/OneDrive-Personal/Control Personal/Finance/Carteiras/holding.xlsm", sheet_name="pv", decimal=",", index_col=5)

# # Converte as datas e formata como string no formato desejado
base_pv['data_com'] = pd.to_datetime(base_pv['data_com'], errors='coerce').dt.strftime('%d/%m/%Y')
base_pv['pagamento'] = pd.to_datetime(base_pv['pagamento'], errors='coerce').dt.strftime('%d/%m/%Y')



colunas = list(base_pv.columns)
colunas_selecionadas = st.sidebar.multiselect("Selecione as colunas", colunas, default=colunas)

col1, col2 = st.sidebar.columns(2)
col_filtro = col1.selectbox("Selecione uma coluna:", colunas)
valor_filtro = col2.selectbox("Selecione um valor:", list(base_pv[col_filtro].unique()))

status_filtrar = col1.button("Filtrar")
status_limpar = col2.button("Limpar") 

if status_filtrar:
    st.dataframe(base_pv.loc[base_pv[col_filtro] == valor_filtro, colunas_selecionadas])
elif status_limpar:
    st.dataframe(base_pv[colunas_selecionadas], height=800)
else:
    st.dataframe(base_pv[colunas_selecionadas], height=800)
