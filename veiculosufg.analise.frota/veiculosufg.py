import streamlit as st 
import pandas as pd
import plotly.express as  px
import numpy as np


# Carregando os dados do arquivo CSV
dados = pd.read_csv("frota-de-veiculos-ufmg-2020.csv",encoding = "ISO-8859-1", sep=';',header=2)

# Calculando a idade média da frota
idade_media = dados['Idade'].mean()
# Criando o gráfico de barras para a idade média
fig_idade = px.bar(x=["Idade Média"], y=[idade_media], labels={"x": "Medida", "y": "Idade Média"})
st.plotly_chart(fig_idade)

# Calculando o valor médio da frota
valor_medio = dados["Valor Aquisição"].mean()

# Criando o gráfico de pizza para o valor médio
fig_valor = px.pie(values=[valor_medio], names=["Valor Médio"])
st.plotly_chart(fig_valor)

# Departamentos com maior número de veículos
departamentos = dados.groupby("Setor lotação")["Placa"].count().reset_index()

# Criando o gráfico de barras para os departamentos
fig_departamentos = px.bar(departamentos, x="Setor lotação", y="Placa", labels={"x": "Departamento", "y": "Número de Veículos"})
st.plotly_chart(fig_departamentos)


