from typing import Union
from fastapi import FastAPI
import wiki_api as wiki_api
from pydantic import BaseModel

app = FastAPI()


class AnimalShortModel(BaseModel):
    name: str
    photo_link: str
    wiki_link: str

class AnimalBigModel(BaseModel):
    name: str
    photo_link: str
    wiki_link: str
    description: str

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/get_animal_short_model")
def send_photo(animal_name: str):
    # goto ai and get name of animal

    # goto wiki and get animal photo link
    return {}


@app.post("/get_animal_big_model")
def send_photo(animal_name: str):
    # goto wiki and get animal description

    # goto CHAT api and get better descr
    return wiki_api.get_wiki_description()