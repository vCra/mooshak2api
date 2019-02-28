import requests

from mooshak2api.factory import GenericObject


class Contest(GenericObject):
    def save(self, connection):




def get(connection, contest_id):
    r = requests.get(f"{connection.endpoint}data/contests/{contest_id}/", headers=connection.headers_with_auth())
    return Contest().load_from_dict(r.json())


def all(connection):
    r = requests.get(f"{connection.endpoint}data/contests/", headers=connection.headers_with_auth())
    results = []
    for c in r.json():
        results.append(Contest().load_from_dict(c))
    return results
