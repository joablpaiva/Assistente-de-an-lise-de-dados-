import streamlit as st 
import pandas as pd 
import numpy as np 

#Exibição de dados 
df = pd.DataFrame(
    np.random.rand(10,3),
    columns=['Preço','Taxa de ocupação','Taxa de inadimplencia']
)

#Funcionalidades de exibição
#basica 
st.table(df)

#Exibição mais completa 
st.dataframe(df)
st.bar_chart(df)