import requests
import json

url = 'https://eulucas1.github.io/api-petshops/petshops.json'
response = requests.get(url)
print(response)

if response.status_code == 200:
    dados_json = response.json()
    dados_petshop = {}
    for item in dados_json:
        nome_do_petshop = item['company']
        if nome_do_petshop not in dados_petshop:
            dados_petshop[nome_do_petshop] = []
        
        dados_petshop[nome_do_petshop].append({
            "item": item['item'],
            "price": item['price'],
            "description": item['description']
        })


else: 
    print(f'O erro corresponde ao {response.status_code}')

for nome_do_petshop, dados in dados_petshop.items():
    nome_do_arquivo = f'{nome_do_petshop}.json'
    with open(nome_do_arquivo,'w') as arquivo_petshop:
        json.dump(dados,arquivo_petshop,indent=4)