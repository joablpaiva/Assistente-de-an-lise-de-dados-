#Dashboard operacioncal 
#Pedidos e estoque 


import streamlit as st 
import pandas as pd 
import plotly.express as px 

st.header('Estoque Atual')


# Carregando os dados, no caso a seguir um arquivo csv.
df = pd.read_csv("C:\\Users\\joabl\\Projetos\\Assistente-de-an-lise-de-dados-\\trabalho_curso\\2-Dashboard Operacional\\Base Estoque.csv",header=0, encoding="ISO-8859-1", sep=';',decimal=",")
df = df.dropna(axis=1, how='all')
df 

# Converter a coluna 'Data Compra' para o tipo datetime
df['Data Compra'] = pd.to_datetime(df['Data Compra'])

# Criar um dashboard 
st.title('Evolução das Compras ao Longo do Tempo')

# Gráfico de linha da quantidade de compras ao longo do tempo
fig_compras_por_tempo = px.bar(df, x='Data Compra', y='Quantidade', title='Evolução das Compras ao Longo do Tempo ')
st.plotly_chart(fig_compras_por_tempo)



st.header('Pedidos para manutenção do estoque')

dfs = pd.read_csv("C:\\Users\\joabl\\Projetos\\Assistente-de-an-lise-de-dados-\\trabalho_curso\\2-Dashboard Operacional\\Base Pedidos-2020.csv", encoding="ISO-8859-1", sep=';', decimal=",")
dfs



