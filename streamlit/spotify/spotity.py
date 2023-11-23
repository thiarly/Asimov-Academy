import streamlit as st
import pandas as pd

st.set_page_config(
    layout="wide",
    page_title="Spotify",
)

df = pd.read_csv('/Users/thiarly/Desktop/GitHub/Asimov-Academy/streamlit/spotify/spotify.csv')

df.set_index('Track', inplace=True)

artists = df['Artist'].value_counts().index

artist = st.selectbox('Artista', artists)
df_filtered = df[df['Artist'] == artist]
st.bar_chart(df_filtered['Stream'])
