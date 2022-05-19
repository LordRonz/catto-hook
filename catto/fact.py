import requests
from random import randint


class CatFact:
    def __init__(self, amount=10):
        self.amount = amount
        self.api_url = "https://cat-fact.herokuapp.com/"
        self.api_url_2 = "https://catfact.ninja/"

    def get_fact(self):
        if randint(0, 1) == 1:
            return self.get_fact_2()

        retry = 0
        while retry < 10:
            res = requests.get(f"{self.api_url}facts/random?amount={self.amount}")
            cat_facts = res.json()
            for fact in cat_facts:
                if fact["status"]["verified"]:
                    return fact["text"]

            retry += 1
        return self.get_fact_2()

    def get_fact_2(self):
        res = requests.get(f"{self.api_url_2}fact")
        fact = res.json()
        return fact["fact"]
