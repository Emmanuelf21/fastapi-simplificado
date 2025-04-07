from fastapi import FastAPI
import json
from product import Product

app = FastAPI()

pathProd = "./data/products.json"
pathCar = "./data/carrinho.json"
dadosProd = open(pathProd)
dadosCar = open(pathCar)

@app.get("/products")
def exibir_produtos():
    data = json.loads(dadosProd.read())
    return data

@app.get("/carrinho")
def exibir_carrinho():
    data = json.loads(dadosCar.read())
    return data

@app.post("/products")
def novo_produto(product: Product):
    data = json.loads(dadosProd.read())
    data['products'].append(product.dict())
    
    with open(pathProd, 'w') as f:
        json.dump(data, f)
    return {'Status':'Produto adicionado'}