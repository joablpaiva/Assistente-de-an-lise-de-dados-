import pandas as pd
def json_to_csv(json_file,csv_file):
    #Carregar dados JSON
    data = pd.read_json(json_file)

    #Converter para CSV
    data.to_csv(csv_file, index=False)

#Uso 
json_to_csv("aluno.json", "arquivo.csv")

