import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar os dados
df_vendas = pd.read_csv('dados_vendas.csv')
df_campanhas = pd.read_csv('dados_campanhas.csv')
df_clientes = pd.read_csv('dados_clientes.csv')

# Título do dashboard
st.title('Dashboard Analítico')

# Análise de Crescimento de Vendas
st.subheader('Crescimento de Vendas')
fig_crescimento_vendas = px.line(df_vendas, x='Data', y='Vendas', title='Crescimento de Vendas ao Longo do Tempo')
st.plotly_chart(fig_crescimento_vendas)

# Análise de ROI por Campanha de Marketing
st.subheader('ROI por Campanha de Marketing')
df_campanhas['ROI'] = (df_campanhas['Lucro'] / df_campanhas['Custo']) * 100
fig_roi_campanhas = px.bar(df_campanhas, x='Campanha', y='ROI', title='ROI por Campanha de Marketing')
st.plotly_chart(fig_roi_campanhas)

# Análise de ROI por Canal de Marketing
st.subheader('ROI por Canal de Marketing')
df_roi_campanha = df_campanhas.groupby('Campanha')[['Lucro', 'Custo']].sum().reset_index()
df_roi_campanha['ROI'] = (df_roi_campanha['Lucro'] / df_roi_campanha['Custo']) * 100
fig_roi_campanhas = px.pie(df_roi_campanha, values='ROI', names='Campanha', title='ROI por Canal de Marketing')
st.plotly_chart(fig_roi_campanhas)

# Análise de ROI por Segmento de Cliente
st.subheader('ROI por Segmento de Cliente')
df_clientes['ROI'] = (df_clientes['Receita'] - df_clientes['Custo']) / df_clientes['Custo']
fig_roi_segmento = px.histogram(df_clientes, x='Segmento', y='ROI', title='ROI por Segmento de Cliente')
st.plotly_chart(fig_roi_segmento)