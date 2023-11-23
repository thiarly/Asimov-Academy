import streamlit as st

st.set_page_config(
    page_title="FIFA2023",
    page_icon=":soccer:",
    layout="wide",
)


df_data = st.session_state["data"]

clubes = df_data["Club"].value_counts().index
club = st.selectbox("Selecione o clube", clubes)

df_filtered_club = df_data[df_data["Club"] == club]

st.image(df_filtered_club["Photo"].iloc[0])
st.title(df_filtered_club["Club"].iloc[0])