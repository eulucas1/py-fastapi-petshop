from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''
    Endpoint que mostra o inicio de todo bom programador!
    
    '''
    return {'Hello':'World'}

@app.get('/api/petshops/')
def get_petshops(petshop: str = Query(None)):
    '''
    Endpoint para ver os produtos dos Pet Shops  
    
    '''
    url = 'https://eulucas1.github.io/api-petshops/petshops.json'
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        if petshop is None:
            return {'Dados':dados_json}

        dados_petshop = []
        for item in dados_json:
            if item['company'] == petshop:
                dados_petshop.append({
                    "item": item['item'],
                    "price": item['price'],
                    "description": item['description']
                })
        return {'Petshop':petshop,'Produtos':dados_petshop}
    else: 
        return {'Erro':f'{response.status_code} - {response.text}'}