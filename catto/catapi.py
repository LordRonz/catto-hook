from os import getenv
from random import randint

import requests

from data.data import get_quotes


class CatAPI:
    def __init__(self):
        self.api_url = "https://api.thecatapi.com/"

    def get_cat(self):
        # if randint(0, 1) == 1:
        #     return self.get_cat2()

        api_key = getenv("CATAPI_KEY")
        headers = {"x-api-key": api_key}
        res = requests.get(f"{self.api_url}v1/images/search", headers=headers)
        cat = res.json()
        return cat[0]["url"]

    def get_cat2(self):
        quote = get_quotes()

        return f"https://cataas.com/cat/says/{quote}?size=60&color=red"
