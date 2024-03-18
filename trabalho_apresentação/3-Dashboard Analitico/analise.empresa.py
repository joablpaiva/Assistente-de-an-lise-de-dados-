#Foi solicitado em sala um dashboard analitico onde se apresenta 
#a analise de crescimento e analise de retorno (ROI)

import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# Criando dados de vendas
data_inicio = datetime(2020, 1, 1)
data_fim = datetime(2021, 12, 31)
datas = pd.date_range(data_inicio, data_fim, freq='D')
vendas = [random.randint(100, 1000) for _ in range(len(datas))]
df_vendas = pd.DataFrame({'Data': datas, 'Vendas': vendas})

# Criando dados de campanhas de marketing
campanhas = ['Redes Sociais', 'E-mail Marketing', 'Anúncios Pagos']
custos = [random.randint(1000, 5000) for _ in range(len(campanhas))]
lucros = [random.randint(2000, 8000) for _ in range(len(campanhas))]
df_campanhas = pd.DataFrame({'Campanha': campanhas, 'Custo': custos, 'Lucro': lucros})

# Criando dados de clientes (exemplo fictício)
segmentos = ['Segmento A', 'Segmento B', 'Segmento C']
receitas = [random.randint(10000, 50000) for _ in range(len(segmentos))]
custos_cliente = [random.randint(5000, 20000) for _ in range(len(segmentos))]
df_clientes = pd.DataFrame({'Segmento': segmentos, 'Receita': receitas, 'Custo': custos_cliente})

# Salvar os dados em arquivos CSV
df_vendas.to_csv('dados_vendas.csv', index=False)
df_campanhas.to_csv('dados_campanhas.csv', index=False)
df_clientes.to_csv('dados_clientes.csv', index=False)
