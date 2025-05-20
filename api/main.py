from fastapi import FastAPI
import json
from product import Product

app = FastAPI()

pathProd = "./data/products.json"
pathCar = "./data/carrinho.json"

@app.get("/products")
def exibir_produtos():
    dadosProd = open(pathProd)
    data = json.loads(dadosProd.read())
    return data

@app.post("/products")
def novo_produto(product: Product):
    dadosProd = open(pathProd)
    data = json.loads(dadosProd.read())
    data['products'].append(product.dict())
    
    f = open(pathProd, 'w')
    f.write(json.dumps(data)) 
    f.close
  
    return {'Status':'Produto adicionado'}

@app.put("/products")
def atualizar_produto(product: Product):
    dadosProd = open(pathProd)
    data = json.loads(dadosProd.read())
    
    novoProd = product.dict()
    
    for prod in data['products']:
        if prod['id']==novoProd['id']:
            pos = data['products'].index(prod)
            
    data['products'].pop(pos)
    data['products'].insert(pos, novoProd)
    
    f = open(pathProd, 'w')
    f.write(json.dumps(data)) 
    f.close
        
    return data['products']

@app.delete("/products/{id}")
def delete_produto(id: int):
    dadosProd = open(pathProd)
    data = json.loads(dadosProd.read())
    
    for produto in data['products']:
        if produto['id']==id:
            data['products'].remove(produto)
            
    f = open(pathProd, 'w')
    f.write(json.dumps(data)) 
    f.close
    
    return data['products']

