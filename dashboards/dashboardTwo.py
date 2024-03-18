import streamlit as st 
import pandas as pd 
import numpy as np 

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] >  .main {{
background-image: url("https://i.postimg.cc/4xNnkfX/Untitled-design.png");
background-size: cover;
background-position: center center ;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
</style>
"""

st.markdown(page_bg_img,unsafe_allow_html=True)

#Exibição de dados 

#Funcionalidades de exibição
#basica
#st.table(df)
#Exibição mais completa 
#st.dataframe(df)
#Exibindo grafico de linha 
#st.line_chart(df)

st.sidebar.header("Dashboard")
st.sidebar.caption("Clique no botão para exibir o gráfico.")

if st.sidebar.button("Exibir Gráfico"):
    st.header("Meu Gráfico")
    df = pd.DataFrame(
    np.random.rand(10,3),
    colums=['Preço','Taxa de ocupação', 'Taxa de inadimplência']
    )
    st.bar_chart(df)
    st.sidebar.code(df)
    