from fastapi import FastAPI
from perplexity_api import Pyplapi as papi
import models

app = FastAPI()

@app.get("/chat")
async def get_animal_model_long(request: models.Request):
    model_list = []
    model_list.append(
        models.ResponceModel(
            type = "text",
            value = await papi.get_chat_answer(request.value)
            )
        )
    for photo_link in await papi.get_photos(request.value):
        model_list.append(
            models.ResponceModel(
                type = "photo",
                value = photo_link
                )
            )
    return models.Responce(model_list)