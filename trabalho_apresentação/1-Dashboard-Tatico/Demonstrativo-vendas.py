#Criar Dashboard Tatico focado em vendas 


#importando bibliotecas  
import streamlit as st 
import pandas as pd 
import plotly.express as px


# Configurando a página no formato landing page
st.set_page_config(layout="wide")



st.markdown("# Vendas de Veiculos de Luxo ") # ao usar # antes do texto ele ficará em destaque .

# Carregando os dados.
df = pd.read_csv("vendasveiculo.csv",  encoding = "ISO-8859-1", sep=';')
df

#Adicionando abas para melhorar a visualização dos dados
#aba1, aba2, aba3 = st.tabs(['Dataset', 'Receita', 'Vendedores'])




# Opções de gráficos/pela barra lateral podemos escolher o gráfico a ser exibido 
opcoes_graficos = ['Gráfico de Barras', 'Gráfico de Pizza']

# selecione o ano na barra lateral
st.sidebar.title('Selecione o Gráfico Desejado')

# tipo de gráfico
selecao_grafico = st.sidebar.selectbox('Selecione o tipo de gráfico', opcoes_graficos)


# fundo da barra lateral (vermelho)
st.markdown("""
<style>
            
[data-testid=stSidebar] {
    background-color: red;
            

}
</style>
""", unsafe_allow_html=True)

# gráfico de barras
def mostrar_grafico_barras():
    total_vendas_por_estado = df.groupby('Estado')['ValorVenda'].sum().reset_index()
    total_vendas_por_estado = total_vendas_por_estado.sort_values(by='ValorVenda')  # Ordena os dados por ValorVenda
    fig = px.bar(total_vendas_por_estado, x='Estado', y='ValorVenda', title='Total de Vendas por Estado')
    st.plotly_chart(fig)

# gráfico de pizza
def mostrar_grafico_pizza():
    total_vendas_por_fabricante = df.groupby('Fabricante')['ValorVenda'].sum().reset_index()
    fig = px.pie(total_vendas_por_fabricante, values='ValorVenda', names='Fabricante', title='Distribuição de Vendas por Fabricante')
    st.plotly_chart(fig)


# Exibir o gráfico selecionado
if selecao_grafico == 'Gráfico de Barras':
    mostrar_grafico_barras()
elif selecao_grafico == 'Gráfico de Pizza':
    mostrar_grafico_pizza()


# Converter a coluna 'DataNotaFiscal' para o tipo datetime especificando o formato
df['DataNotaFiscal'] = pd.to_datetime(df['DataNotaFiscal'], format='%d/%m/%Y')

# Extrair e criar uma nova coluna 'Mês'
df['Mês'] = df['DataNotaFiscal'].dt.month

# Título para a seleção do ano na barra lateral
st.sidebar.title('Selecione o ano e veja a evolução de vendas ')

# Adicionando a seleção do ano na barra lateral
ano_selecionado = st.sidebar.selectbox('Selecione o ano:', sorted(df['Ano'].unique()))



# Filtrar o ano selecionado
df_ano_selecionado = df[df['Ano'] == ano_selecionado]

# Agrupar os dados filtrados por mês e calcular a soma das vendas para cada mês
vendas_por_mes = df_ano_selecionado.groupby('Mês')['ValorVenda'].sum().reset_index()

# Plotar o gráfico de linha da evolução das vendas por mês no ano selecionado
fig_vendas_por_mes = px.line(vendas_por_mes, x='Mês', y='ValorVenda', title=f'Evolução das Vendas por Mês em {ano_selecionado}')
st.plotly_chart(fig_vendas_por_mes)

#############################################################################




# soma do custo de mão de obra para cada fabricante
custo_mao_de_obra_por_fabricante = df.groupby('Fabricante')['CustoMaoDeObra'].sum().reset_index()

# Ordenar os valores pelo custo de mão de obra em ordem decrescente
custo_mao_de_obra_por_fabricante = custo_mao_de_obra_por_fabricante.sort_values(by='CustoMaoDeObra', ascending=False)

# Criar um gráfico de barras com os totais de mão de obra para cada fabricante
fig = px.bar(custo_mao_de_obra_por_fabricante, x='Fabricante', y='CustoMaoDeObra', title='Custo de Mão de Obra por Fabricante')
st.plotly_chart(fig)


#################################################################################



# Calcular o lucro para cada venda
df['Lucro'] = df['ValorVenda'] - (df['ValorCusto'] + df['TotalDesconto'] + df['CustoEntrega'] + df['CustoMaoDeObra'])

# Agrupar por fabricante e somar os lucros
lucro_por_fabricante = df.groupby('Fabricante')['Lucro'].sum().reset_index()

# Classificar os fabricantes pelo lucro total
lucro_por_fabricante = lucro_por_fabricante.sort_values(by='Lucro', ascending=False)

# Criar um gráfico de barras com os lucros por fabricante
fig = px.bar(lucro_por_fabricante, x='Fabricante', y='Lucro', title='Lucro por Fabricante')
st.plotly_chart(fig)



#################################################################################


# Calcular o total de descontos para cada marca
total_descontos_por_fabricante = df.groupby('Fabricante')['TotalDesconto'].sum().reset_index()

# Classificar os fabricantes com base no total de descontos
total_descontos_por_fabricante = total_descontos_por_fabricante.sort_values(by='TotalDesconto', ascending=False)

# Criar um gráfico de barras com os descontos por fabricante
fig = px.bar(total_descontos_por_fabricante, x='Fabricante', y='TotalDesconto', title='Total de Descontos por Fabricante')
st.plotly_chart(fig)