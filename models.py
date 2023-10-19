from pydantic import BaseModel
class AnimalShortModel:
    def __init__(self, name: str, photo_link: str):
        self.name = name
        self.photo_link = photo_link

class AnimalLongModel:
    def __init__(self, name: str, photo_link: str, description: str):
        self.name= name
        self.photo_link= photo_link
        self.description= description