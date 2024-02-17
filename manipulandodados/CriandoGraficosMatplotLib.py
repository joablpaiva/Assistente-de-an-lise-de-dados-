import matplotlib.pyplot as plt 

#Dados para o gráfico 
idades =[23,78,22,19,45]
nomes = ['João','Ana','Carlos','Maria','Pedro']

plt.bar(nomes, idades)
plt.xlabel('Nomes')
plt.ylabel('Idades')
plt.title('Idades por Nome')
plt.show()

