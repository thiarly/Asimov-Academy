import streamlit as st
import pandas as pd
import locale

# Configurando a localidade para Português do Brasil
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

st.set_page_config(
    layout="wide",
    page_title="Spotify",
)

# Carregar dados (ajuste o caminho do arquivo conforme necessário)
df = pd.read_excel("/Users/thiarly/Library/CloudStorage/OneDrive-Personal/Control Personal/Finance/Carteiras/holding.xlsm" , sheet_name="pv")


df.set_index('ativo', inplace=True)

eventos = df['evento'].value_counts().index
ativos = st.sidebar.selectbox('evento', eventos)
segmentos = df['segmento'].value_counts().index
segmento = st.selectbox('segmento', segmentos)

# Seletor de ano no DataFrame original
anos_disponiveis = sorted(df['ano'].unique())
ano_selecionado = st.sidebar.selectbox('Selecionar Ano', anos_disponiveis)
# Filtrando o DataFrame pelo ano selecionado
df_filtered_ano = df[df['ano'] == ano_selecionado]

# Mapeamento dos números para os nomes dos meses em português
mapeamento_meses = {
    1: 'Jan', 2: 'Fev', 3: 'Mar', 4: 'Abr',
    5: 'Mai', 6: 'Jun', 7: 'Jul', 8: 'Ago',
    9: 'Set', 10: 'Out', 11: 'Nov', 12: 'Dez'
}

# Inicializando uma série com todos os meses e valores zero
soma_valores_mes = pd.Series([0]*12, index=pd.CategoricalIndex(mapeamento_meses.values(), ordered=True, categories=mapeamento_meses.values()))

# Atualizando a série com os dados reais do DataFrame
valores_reais = df_filtered_ano.groupby('mes')['valor_bruto'].sum()
for mes, valor in valores_reais.items():
    soma_valores_mes[mapeamento_meses[mes]] = valor

# Gráficos
col1, col2 = st.columns([0.6, 0.4])

with col1:
    st.write("Gráfico - Valor Bruto por Ativo")
    st.bar_chart(df[df['evento'] == ativos].groupby('ativo')['valor_bruto'].sum())

with col2:
    st.write("Gráfico - Valor Líquido por Ativo")
    st.line_chart(df[df['evento'] == ativos].groupby('ativo')['valor_liquido'].sum())

st.write("Gráfico - Valor Bruto por Mês")
st.bar_chart(soma_valores_mes)

st.sidebar.button("Pesquisar")
# display = st.checkbox('Display')

# if display:
#    valor_bruto = st.bar_chart(df_filtered['valor_bruto'])
    
