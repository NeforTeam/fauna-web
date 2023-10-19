from perplexity import Perplexity
import re

class Pyplapi:
    async def get_description(object_name: str):
        perplexity = Perplexity("baracuda000330@gmail.com")
        answer = perplexity.search(f"Give me wikipedia description of {object_name} do not say it`s wikipedia, just give me description text only")
        responce = ""
        for a in answer:
            if a["answer"] is not None:
               responce= a["answer"]
        perplexity.close()
        responce = re.sub(r'\[[^\]]*\]|\n\d*', '', responce)
        return responce
        