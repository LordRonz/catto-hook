from os import getenv
from random import randint
from urllib.parse import quote as encode_url

import requests

from data.data import get_quotes


class CatAPI:
    def __init__(self):
        self.api_url = "https://api.thecatapi.com/"

    def get_cat(self):
        if randint(0, 2) == 1:
            return self.get_cat2()

        api_key = getenv("CATAPI_KEY")
        headers = {"x-api-key": api_key}
        res = requests.get(f"{self.api_url}v1/images/search?limit=10", headers=headers)
        cat = res.json()
        for c in cat:
            if c["url"]:
                return c["url"]
        return self.get_cat2()

    def get_cat2(self):
        quote = get_quotes()

        return f"https://cataas.com/cat/says/{encode_url(quote)}?size=60"
