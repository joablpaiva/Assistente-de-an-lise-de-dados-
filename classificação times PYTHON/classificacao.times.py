import pandas as pd
import matplotlib.pyplot as plt

#Definindo os anos 
anos = ["2019","2020","2021","2021","2022","2023","2024","2025"]

#Definindo os times 
times = ["Flamengo","Fuminense","Palmeiras","Corinthians","Atlético Pr","São Paulo","Grêmio"]

#Definindo os pontos para cada time 
pontos = [11,5,10,1,6,3,4]

#Criando o Dataframe
df = pd.DataFrame({'Anos':anos, 'Times':times,'Pontos':pontos})

#print(df)

#Plotando os dados 
plt.figure(figsize=(10,5))
for time in df['Times'].unique():
    plt.plot(df[df["Times"]== time]['Anos'], df[df['Times'] == time]['Pontos'], marker='0', label=time)
plt.title('Pontos por ano')
plt.xlabel('Anos')
plt.ylabel('Pontos')
plt.legend()
plt.grid(True)
plt.show()

