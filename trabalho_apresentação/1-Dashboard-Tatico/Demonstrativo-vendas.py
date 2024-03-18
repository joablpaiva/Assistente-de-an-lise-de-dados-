#Criar Dashboard Tatico focado em vendas 


#importando bibliotecas  
import streamlit as st 
import pandas as pd 
import plotly.express as px



# Carregando os dados, no caso a seguir um arquivo csv.
df = pd.read_csv("vendasveiculo.csv",  encoding = "ISO-8859-1", sep=';')

# Opções de gráficos/pela barra lateral podemos escolher o gráfico a ser exibido 
opcoes_graficos = ['Gráfico de Barras', 'Gráfico de Pizza']


# Barra lateral para seleção do tipo de gráfico
selecao_grafico = st.sidebar.selectbox('Selecione o tipo de gráfico', opcoes_graficos)


# Define a cor de fundo desejada (vermelho)
st.markdown("""
<style>
            
[data-testid=stSidebar] {
    background-color: red;
            

}
</style>
""", unsafe_allow_html=True)

# Função para criar e exibir o gráfico de barras
def mostrar_grafico_barras():
    total_vendas_por_estado = df.groupby('Estado')['ValorVenda'].sum().reset_index()
    total_vendas_por_estado = total_vendas_por_estado.sort_values(by='ValorVenda')  # Ordena os dados por ValorVenda
    fig = px.bar(total_vendas_por_estado, x='Estado', y='ValorVenda', title='Total de Vendas por Estado')
    st.plotly_chart(fig)

# Função para criar e exibir o gráfico de pizza
def mostrar_grafico_pizza():
    total_vendas_por_fabricante = df.groupby('Fabricante')['ValorVenda'].sum().reset_index()
    fig = px.pie(total_vendas_por_fabricante, values='ValorVenda', names='Fabricante', title='Distribuição de Vendas por Fabricante')
    st.plotly_chart(fig)


# Exibir o gráfico selecionado
if selecao_grafico == 'Gráfico de Barras':
    mostrar_grafico_barras()
elif selecao_grafico == 'Gráfico de Pizza':
    mostrar_grafico_pizza()