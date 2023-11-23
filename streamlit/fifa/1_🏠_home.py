import streamlit as st
import webbrowser
import pandas as pd
from datetime import datetime


st.set_page_config(
    page_title="FIFA2023",
    page_icon=":soccer:",
    layout="wide",
)



if "data" not in st.session_state:
    df_data = st.session_state.data = pd.read_csv("/Users/thiarly/Desktop/GitHub/Asimov-Academy/streamlit/fifa/datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data.sort_values(by=["Overall"], ascending=False)
    st.session_state["data"] = df_data




st.markdown("# FIFA2023 OFFICIAL WEBSITE! ⚽️")
st.sidebar.markdown("Developed by: [Thiarly Cavalcante] (https://www.linkedin.com/in/thiarly-cavalcante-b0aa6056/")

btn = st.button("Acesse os dados do Kaggle")
if btn:
    webbrowser.open_new_tab('https://www.kaggle.com/stefanoleone992/fifa-21-complete-player-dataset')
    
    
st.markdown(
    """
        O conjuto de dados
        [FIFA 21 Complete Player Dataset](https://www.kaggle.com/stefanoleone992/fifa-21-complete-player-dataset)
        foi utilizado para a criação deste aplicativo.
        
        Sample analysis of top n% players (e.g. top 5% of the player) to see if some important attributes as Agility or BallControl or Strength have been popular or not acroos the FIFA versions. An example would be seeing that the top 5% players of FIFA 20 are more fast (higher Acceleration and Agility) compared to FIFA 15. The trend of attributes is also an important indication of how some attributes are necessary for players to win games (a version with more top 5% players with high BallControl stats would indicate that the game is more focused on the technique rather than the physicial aspect).
    """
)