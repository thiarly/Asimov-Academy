import streamlit as st
import pandas as pd
import plotly.express as px
import locale

# Configura a localização para o Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

st.set_page_config(
    layout="wide",
    page_title="Holding",
)

# Lê o arquivo Excel
df = pd.read_excel("/Users/thiarly/Library/CloudStorage/OneDrive-Personal/Control Personal/Finance/Carteiras/holding.xlsm", sheet_name="pv")

# Filtra o DataFrame com base no evento selecionado
eventos = df['evento'].value_counts().index
ativos = st.selectbox('Selecione um evento', eventos)
df_filtered = df[df['evento'] == ativos]

# Agrupa os valores pelo ativo e soma
df_grouped = df_filtered.groupby('ativo')['valor_bruto'].sum().reset_index()

# Formata os valores em moeda brasileira com "R$" antes do valor
df_grouped['valor_bruto'] = df_grouped['valor_bruto'].apply(lambda x: "R$" + locale.currency(x, grouping=True, symbol=False))

# Ordena o DataFrame pelo valor bruto em ordem decrescente
df_grouped = df_grouped.sort_values(by='valor_bruto', ascending=True)

# Cria um gráfico de barras com o Plotly Express
fig = px.bar(df_grouped, x='ativo', y='valor_bruto', text='valor_bruto')

# Atualiza o layout do gráfico para exibir os valores no topo das barras
fig.update_traces(texttemplate='%{text}', textposition='outside')

# Define o título e rótulos dos eixos
fig.update_layout(
    title=f'Valores Brutos por Ativo para o Evento: {ativos}',
    xaxis_title='Ativo',
    yaxis_title='Valor Bruto (R$)'
)

# Ajusta o tamanho do gráfico para ocupar toda a tela
fig.update_layout(
    autosize=True,
    margin=dict(l=0, r=0, t=40, b=0)
)

# Exibe o gráfico no Streamlit
st.plotly_chart(fig, use_container_width=True)
