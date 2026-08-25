import requests
import pprint
from dotenv import load_dotenv
import os
os.getenv("API_KEY")

load_dotenv()

api_key = os.getenv("API_KEY")
url = f'https://api.watchmode.com/v1/autocomplete-search'

print(api_key)


params = {

    'apiKey': api_key,
    'search_field': "name",
    'search_value': input("Digite o nome do filme:"),
    'search_type': '2'


}

resposta = requests.get(url,params=params)

dados_requisicao = resposta.json()
print(resposta.status_code)
print(resposta.status_code)
  
   

filmes = dados_requisicao['results']


for indice, filme in enumerate(filmes):
    print(indice, "Nome",filme["name"], "Lançamento:",filme["year"])


escolha = int(input("Digite o número do filme correspondente:"))


title_id = filmes[escolha]["id"]
url2 = f'https://api.watchmode.com/v1/title/{title_id}/details'

params2 = {

'apiKey': api_key


}

resposta2 = requests.get(url2,params=params2)
print(resposta.status_code)
dados_requisicao = resposta2.json()


filme_detalhes ="Nome do filme:", dados_requisicao['title'],'Descrição:', dados_requisicao['plot_overview']

pprint.pprint(filme_detalhes)
