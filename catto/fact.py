from random import randint

import requests


class CatFact:
    def __init__(self, amount=10):
        self.amount = amount
        self.api_url = "https://cat-fact.herokuapp.com/"
        self.api_url_2 = "https://catfact.ninja/"

    def get_fact(self):
        # if randint(0, 1) == 1:
        #     return self.get_fact_2()
        return self.get_fact_2

        retry = 0
        while retry < 10:
            res = requests.get(f"{self.api_url}facts/random?amount={self.amount}", timeout=20)
            try:
                cat_facts = res.json()
            except requests.exceptions.JSONDecodeError:
                continue
            except requests.exceptions.Timeout:
                break
            for fact in cat_facts:
                if fact["status"]["verified"]:
                    return fact["text"]

            retry += 1
        return self.get_fact_2()

    def get_fact_2(self):
        res = requests.get(f"{self.api_url_2}fact", timeout=20)
        fact = res.json()
        return fact["fact"]
