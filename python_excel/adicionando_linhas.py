

from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px

# Configura a página para usar o layout 'wide'
st.set_page_config(layout="wide")

# Carrega os dados
base_pv_path = "/Users/thiarly/Library/CloudStorage/OneDrive-Personal/Control Personal/Finance/Carteiras/holding.xlsm"
base_pv = pd.read_excel(base_pv_path, sheet_name="pv", decimal=",", index_col=5)
base_suporte = pd.read_excel(base_pv_path, sheet_name="suporte", decimal=",", usecols="B:E", index_col=0)

# Sidebar inputs
ativo_lista = base_suporte.index.tolist()
ativo_selecionado = st.sidebar.selectbox("Selecione o ativo", ativo_lista)

meta_anual = st.sidebar.number_input("Meta anual", value=0.0, step=0.01)

data_com = st.sidebar.date_input("Data com", value=pd.to_datetime('today'))
data_pagamento = st.sidebar.date_input("Data do pagamento", value=pd.to_datetime('today'))

mes = st.sidebar.selectbox("Selecione o mês", list(range(1, 13)))
ano = st.sidebar.selectbox("Selecione o ano", list(range(2020, 2032)))

evento = st.sidebar.selectbox("Selecione o evento", ["DIVIDENDO", "JCP", "RENDIMENTO", "SOBRA DE EVENTO" ])
segmento = st.sidebar.selectbox("Selecione o segmento", ["AÇÕES", "FII"])
setor = st.sidebar.selectbox("Selecione o setor", ["BANCO", "CONSTRUÇÃO", "ELÉTRICA", "EQUIPAMENTOS", "HOLDING", "SAÚDE", "TECNOLOGIA", "SANEAMENTO", "SEGURO", "MINERIO", "PETROLEO"])


quantidade = st.sidebar.number_input("Quantidade", value=0, step=1)
dpa_bruto = st.sidebar.number_input("DPA bruto", value=0.0, step=0.01)


# Cálculos baseados nas seleções
dpa_liquido = dpa_bruto * 0.15 if evento == "JCP" else dpa_bruto
valor_bruto = quantidade * dpa_bruto
valor_liquido = quantidade * dpa_liquido

# Exibir os resultados calculados na sidebar
st.sidebar.write("DPA líquido:", dpa_liquido)
st.sidebar.write("Valor bruto:", valor_bruto)
st.sidebar.write("Valor líquido:", valor_liquido)



if st.sidebar.button('Adicionar'):
    # Adiciona a linha no DataFrame
    base_pv.loc[ativo_selecionado, "META ANUAL"] = meta_anual
    base_pv.loc[ativo_selecionado, "DATA COM"] = data_com
    base_pv.loc[ativo_selecionado, "DATA PAGAMENTO"] = data_pagamento
    base_pv.loc[ativo_selecionado, "MÊS"] = mes
    base_pv.loc[ativo_selecionado, "ANO"] = ano
    base_pv.loc[ativo_selecionado, "EVENTO"] = evento
    base_pv.loc[ativo_selecionado, "SEGMENTO"] = segmento
    base_pv.loc[ativo_selecionado, "SETOR"] = setor
    base_pv.loc[ativo_selecionado, "QUANTIDADE"] = quantidade
    base_pv.loc[ativo_selecionado, "DPA BRUTO"] = dpa_bruto
    base_pv.loc[ativo_selecionado, "DPA LÍQUIDO"] = dpa_liquido
    base_pv.loc[ativo_selecionado, "VALOR BRUTO"] = valor_bruto
    base_pv.loc[ativo_selecionado, "VALOR LÍQUIDO"] = valor_liquido

    # Salva o DataFrame
    base_pv.to_excel(base_pv_path, sheet_name="pv", decimal=",", index=True)
    base_suporte.to_excel(base_pv_path, sheet_name="suporte", decimal=",", index=True)

# Exibe os DataFrames
st.write(base_pv)