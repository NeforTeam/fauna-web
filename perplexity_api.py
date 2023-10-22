from perplexity import Perplexity
import re

class Pyplapi:
    async def get_chat_answer(request: str):
        perplexity = Perplexity("baracuda000330@gmail.com")
        text_answer = perplexity.search(request)
        #perplexity.search(f"Give me wikipedia description of {request} do not say it`s wikipedia, just give me description text only")
        responce = ""
        for iter in text_answer:
            responce = iter["answer"]
        perplexity.close()
        responce = re.sub(r'\[[^\]]*\]|\n\d*', '', responce)
        return responce
    

    async def get_photos(object_name: str):
        perplexity = Perplexity("baracuda000330@gmail.com")
        photo_answer = perplexity.search(f"Give me photos of {object_name}")
        photo_links = []
        try:
            for iter in photo_answer:
                for photo_link in iter["image_metadata"]:
                     photo_links.append(photo_link["image"])
            return photo_links
        except Exception as e:
            return []