import streamlit as st 
import pandas as pd
import plotly.express as  px
import numpy as np


# Carregando os dados do arquivo CSV
dados = pd.read_csv("frota-de-veiculos-ufmg-2020.csv",encoding = "ISO-8859-1", sep=';',header=2)
dados


# Função para converter valores em cruzeiros para reais
def converter_para_reais(valor_cruzeiros):
    valor_sem_asterisco = valor_cruzeiros.replace('*', '')  # Remover o asterisco (*)
    valor_sem_pontos = valor_sem_asterisco.replace('.', '')  # Remover os pontos de separação de milhares
    valor_numerico = float(valor_sem_pontos.replace(',', '.'))  # Converter para float (substituindo ',' por '.' para o formato correto)
    return valor_numerico / 2750  # Conversão de cruzeiros para reais (considerando a cotação de 1 cruzeiro = 0.000363636 reais)


# Carregando os dados do arquivo CSV
dados = pd.read_csv("frota-de-veiculos-ufmg-2020.csv",encoding = "ISO-8859-1") 
                    

dados_com_asterisco = dados[dados['Valor Aquisição'].str.startswith('*')]

# Aplicar a função de conversão para reais na coluna 'Valor Aquisição'
dados_com_asterisco['Valor Aquisição'] = dados_com_asterisco['Valor Aquisição'].apply(converter_para_reais)

# Imprimir os dados convertidos para reais
st.write("Valores convertidos para reais:")
st.write(dados_com_asterisco)

# Imprimir os dados filtrados
st.write("Dados com * no início da coluna 'Valor Aquisição':")
st.write(dados_com_asterisco)