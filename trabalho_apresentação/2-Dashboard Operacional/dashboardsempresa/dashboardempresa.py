import pandas as pd
import streamlit as st 
import plotly.express as px 

# Carregue o arquivo Excel para o DataFrame df_estoque
df_estoque = pd.read_excel("estoque.xlsx")
# Carregando os dados do arquivo CSV
df_pedidos = pd.read_csv("C:\\Users\\joabl\\Projetos\\Assistente-de-analise-de-dados\\dashboardsempresa\\pedidos.novo.csv", encoding="ISO-8859-1", sep=';')



# Salve os DataFrames como JSON
df_estoque.to_json("estoque.json", orient="records")



# Título do dashboard
st.title("Estoque")
df_estoque

# Título do dashboard
st.title("Pedidos")
df_pedidos

# Título do dashboard
#st.title("Dashboard de Pedidos  e Estoque")


# Título do dashboard
st.title("Dados de Estoque")


# Gráfico de barras para mostrar o estoque por produto
fig_estoque = px.bar(df_estoque, x='Produto', y='Estoque', title='Estoque por Produto')
st.plotly_chart(fig_estoque)



# Gráfico de dispersão para mostrar o estoque mínimo e o estoque atual
st.subheader('Estoque Mínimo vs Estoque Atual')
fig_estoque_minimo = px.bar(df_estoque, x='Produto', y=['Estoque', 'Estoque Mínimo'], barmode='group', title='Estoque Mínimo vs Estoque Atual')
st.plotly_chart(fig_estoque_minimo)


# Título do dashboard
st.title("Dados de Pedidos")

###########################################################################



# Carregar os dados
df_estoque = pd.read_excel("estoque.xlsx")
df_pedidos = pd.read_csv("C:\\Users\\joabl\\Projetos\\Assistente-de-analise-de-dados\\dashboardsempresa\\pedidos.novo.csv", encoding="ISO-8859-1", sep=';')

# Convertendo a coluna 'Data' para o tipo datetime com formato correto
df_pedidos['Data'] = pd.to_datetime(df_pedidos['Data'], format='%d/%m/%Y')

# Título do dashboard
st.title("Dashboard da Empresa")

# Adicionar um seletor de data para filtrar os pedidos por período de tempo
st.sidebar.title('Filtrar por Data')

# Garantindo que min_date e max_date sejam objetos datetime64[ns]
min_date = pd.to_datetime(df_pedidos['Data'].min())
max_date = pd.to_datetime(df_pedidos['Data'].max())

start_date = st.sidebar.date_input("Data de início", min_value=min_date, max_value=max_date, value=min_date)
end_date = st.sidebar.date_input("Data de término", min_value=min_date, max_value=max_date, value=max_date)

# Convertendo start_date e end_date para datetime64[ns]
start_date = pd.to_datetime(start_date)
end_date = pd.to_datetime(end_date)

# Filtrar os pedidos por período de tempo selecionado
df_pedidos_filtrados = df_pedidos[(df_pedidos['Data'] >= start_date) & (df_pedidos['Data'] <= end_date)]

# Gráfico de barras para mostrar o estoque por produto
st.subheader('Estoque por Produto')
fig_estoque = px.bar(df_estoque, x='Produto', y='Estoque', title='Estoque por Produto')
st.plotly_chart(fig_estoque)


# Agregar os dados por mês
df_pedidos_filtrados['Data'] = pd.to_datetime(df_pedidos_filtrados['Data'])
df_pedidos_filtrados['Mês'] = df_pedidos_filtrados['Data'].dt.strftime('%Y-%m')  # Converter para string no formato 'YYYY-MM'
df_vendas_agregadas = df_pedidos_filtrados.groupby('Mês')['Qtde. Pedido'].sum().reset_index()

# Gráfico de barras para mostrar as vendas agregadas por mês
fig_vendas_agregadas = px.bar(df_vendas_agregadas, x='Mês', y='Qtde. Pedido', title='Vendas Agregadas por Mês')
st.plotly_chart(fig_vendas_agregadas)

# Análise de clientes (exemplo: contagem de pedidos por cliente)
st.subheader('Análise de Clientes')
df_clientes = df_pedidos_filtrados.groupby('Cliente').size().reset_index(name='Número de Pedidos')
fig_clientes = px.bar(df_clientes, x='Cliente', y='Número de Pedidos', title='Número de Pedidos por Cliente')
st.plotly_chart(fig_clientes)