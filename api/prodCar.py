from pydantic import BaseModel

class ProdCar(BaseModel):
    id:int
    name:str
    price:float
    image:str
    qtd: int