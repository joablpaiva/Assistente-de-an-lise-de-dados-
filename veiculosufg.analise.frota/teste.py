import pandas as pd 
import streamlit as st 
import plotly.express as px 
import numpy as np


# Carregando os dados do arquivo CSV
dados = pd.read_csv("frota-de-veiculos-ufmg-2020.csv",encoding = "ISO-8859-1", sep=';',header=2)



#carregando arquivos csv 

file_path = "frota-de-veiculos-ufmg-2020.csv"
df = pd.read_csv(file_path)

#Função para conveter valores de cruzeiros em reais .

def convert_cruzeiros_to_reais(value):
    if isinstance(value, str) and value.startswith("*"):
        value = value_replace("*", "").replace(".", "").replace(",", "")
        return float(value)/2750  #Assumindo que 1 real = 2750 cuzeiros 
    else:
        return value
#Aplicar a função à coluna 'Valor de Aquisição'
    
#Salvar o dataframe atualizado 
df.to_csv(file_path, index=False)

#Mostrar o dataframe atualizado 
st.write(df)