import requests


class CatFact:
    def __init__(self, amount=10):
        self.amount = amount
        self.api_url = "https://cat-fact.herokuapp.com/"

    def get_fact(self):
        retry = 0
        while retry < 10:
            res = requests.get(f"{self.api_url}facts/random?amount={self.amount}")
            cat_facts = res.json()
            for fact in cat_facts:
                if fact["status"]["verified"]:
                    return fact["text"]

            retry += 1
        return "Not found"
