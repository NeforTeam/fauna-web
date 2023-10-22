from pydantic import BaseModel

class ResponceModel:
    def __init__(self, type: str, value: str):
        self.type = type
        self.value = value

class Responce:
    def __init__(self, models: list):
        self.models=models

class Request(BaseModel):
    value: str