import requests as r

from config import JSONPLACEHOLDER_HOST


class BaseResource:
    def get(self, path: str, params=None):
        return r.get(url=JSONPLACEHOLDER_HOST + path, params=params)

    def post(self, path: str, json_str: dict):
        return r.post(url=JSONPLACEHOLDER_HOST + path, json=json_str)

    def delete(self, path: str):
        return r.delete(url=JSONPLACEHOLDER_HOST + path)

    def put(self, path: str, json_str: dict):
        return r.put(url=JSONPLACEHOLDER_HOST + path, json=json_str)

    def patch(self, path: str, json_str: dict):
        return r.patch(url=JSONPLACEHOLDER_HOST + path, json=json_str)
