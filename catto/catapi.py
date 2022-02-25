import requests


class CatAPI:
    def __init__(self):
        self.api_url = "https://api.thecatapi.com/"

    def get_cat(self):
        res = requests.get(f"{self.api_url}v1/images/search")
        cat = res.json()
        return cat[0]['url']
