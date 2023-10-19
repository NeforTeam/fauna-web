from typing import Union
from fastapi import FastAPI
from perplexity_api import Pyplapi as papi
import models

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/get_animal_short")
async def get_animal_model_short(object_name: str):
    responce = await papi.get_description(object_name)
    return responce


@app.get("/get_animal_long")
async def get_animal_model_long(object_name: str):
    responce = await papi.get_description(object_name)  
    return responce