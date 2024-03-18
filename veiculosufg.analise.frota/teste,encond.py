import pandas as pd

# Tente diferentes encodings até encontrar o correto
encodings = ['utf-8', 'latin1', 'iso-8859-1']

for encoding in encodings:
    try:
        dados = pd.read_csv(r"C:\Users\joabl\Projetos\Assistente-de-an-lise-de-dados-\veiculosufg\frota-de-veiculos-ufmg-2020.csv", encoding="ISO-8859-1", sep=';', header=2)
        # Se conseguir ler o arquivo sem erros, pare o loop
        break
    except UnicodeDecodeError:
        # Se ocorrer um erro de decodificação, tente o próximo encoding
        continue

# Agora que o arquivo foi lido com sucesso, você pode continuar co