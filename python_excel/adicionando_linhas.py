from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px


# Configura a página para usar o layout 'wide'
st.set_page_config(layout="wide")

# Carrega os dados
base_pv = pd.read_excel("/Users/thiarly/Library/CloudStorage/OneDrive-Personal/Control Personal/Finance/Carteiras/holding.xlsm", sheet_name="pv", decimal=",", index_col=5)
# selecionar colunar especifica excel
base_suporte = pd.read_excel("/Users/thiarly/Library/CloudStorage/OneDrive-Personal/Control Personal/Finance/Carteiras/holding.xlsm", sheet_name="suporte", decimal=",", usecols="B:E", index_col=0)

# # Converte as datas e formata como string no formato desejado
base_pv['data_com'] = pd.to_datetime(base_pv['data_com'], errors='coerce').dt.strftime('%d/%m/%Y')
base_pv['pagamento'] = pd.to_datetime(base_pv['pagamento'], errors='coerce').dt.strftime('%d/%m/%Y')

ativo_lista = base_suporte.index.tolist()
ativo_selecionado = st.sidebar.selectbox("Selecione o ticker", ativo_lista)




st.write(base_pv)
st.write(base_suporte)


