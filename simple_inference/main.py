from fastapi import FastAPI
from pydantic import BaseModel

import hello
import datos
import train
import modelo

url_wine='https://docs.google.com/uc?export=download&id=1ZsJWYHxcEdJQdb62diQf8o3fvXFawt1a'
url_house_price='https://docs.google.com/uc?export=download&id=1WsTJN-u4YRrPKqJTp8h8iUSAdfJC8_qn'

app = FastAPI()

@app.get("/")
async def root():
    return hello.hello()

@app.get("/train_model")
async def train_model():
    datos.get_data()
    return train.train()
    
class Wine(BaseModel):
    fixed_acidity: float = 8.0
    volatile_acidity: float = 0.57
    citric_acid: float = 0.23
    residual_sugar: float = 3.2
    chlorides: float = 0.073
    free_sulfur_dioxide: float = 17.0
    total_sulfur_dioxide: float = 119.0
    density: float = 0.99675	
    pH: float = 3.26
    sulphates: float = 0.57
    alcohol: float = 9.3

@app.post("/do_inference")
async def train_model(wine: Wine, model:str='wine'):
    return modelo.modelo(wine,model)