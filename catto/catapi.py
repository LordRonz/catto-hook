import requests
from os import getenv


class CatAPI:
    def __init__(self):
        self.api_url = "https://api.thecatapi.com/"

    def get_cat(self):
        api_key = getenv("CATAPI_KEY")
        headers = {"x-api-key": api_key}
        res = requests.get(f"{self.api_url}v1/images/search", headers=headers)
        cat = res.json()
        return cat[0]["url"]
