import requests
from bs4 import BeautifulSoup

    #URL do clima tempo 
url = "https://www.climatempo.com.br/"

        #Fazendo a requisição para a URL 
response = requests.get(url)

        #Verificando se a requisição foi bem sucedida 
if response.status_code == 200:
        #Parseando o conteúdo da pagina com BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

        #Agora você pode usar o objeto "soup" para encontrar 
        #elementos na página 
        #Por exemplo, para encontrar todos os paragrafos você 
        #pode fazer:
    paragraphs = soup.find_all('p')


    for p in paragraphs:
        print(p.get_text())
else:
    print("Não foi possivel acessar a página .")

   


