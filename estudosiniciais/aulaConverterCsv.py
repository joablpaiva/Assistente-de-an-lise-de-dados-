import csv

with open("testeipea.csv","r") as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv,delimiter=",") 
    
    for i, linha in enumerate(arquivo_csv):
        if i == 0:
            print("Região: " + str(linha))
        else:
            print("ID: " + str(linha))