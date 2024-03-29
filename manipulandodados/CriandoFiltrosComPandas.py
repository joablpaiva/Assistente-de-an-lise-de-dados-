import pandas as pd 

#Criando um dataframe de exemplo
data = {'Nome':['João','Ana','Maria','Pedro','Daniel'],
        'Idade':[23,78,22,19,45],
        'Cidade':['Belo Horizonte','Fortaleza','Brasília','São Paulo',
                  'Rio de Janeiro']}
df = pd.DataFrame(data)

#Filtrando pessoas com mais de 25 anos 
df_filtrado = df[df['Idade'] > 25]
print(df_filtrado)