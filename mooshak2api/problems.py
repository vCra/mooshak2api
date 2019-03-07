import requests

from mooshak2api import contests
from mooshak2api.contests import Contest
from mooshak2api.factory import GenericObject


class Problem(GenericObject):
    """
    A problem of a Contest.
     It must contain a Contest ID, as the REST API does not allow accessing problems directly

    """
    def __init__(self, contest_id, *args, **kwargs):
        super(Problem, self).__init__(*args, **kwargs)
        self.contest_id = contest_id
    contest_id = None

    def update(self, connection):
        r = requests.put(
            f"{connection.endpoint}data/contests/{self.contest_id}/problems/{self.id}",
            headers=connection.headers_with_auth(),
            json=self.as_json()
        )
        return r

    def delete(self, connection):
        r = requests.delete(
            f"{connection.endpoint}data/contests/{self.contest_id}/problems/{self.id}",
            headers=connection.headers_with_auth()
        )
        return r

    def get_contest(self, connection):
        return contests.get(connection, self.contest_id)


def get(connection, contest, problem_id):
    if type(contest) is Contest:
        contest = contest.id
    r = requests.get(f"{connection.endpoint}data/contests/{contest}/problems/{problem_id}",
                     headers=connection.headers_with_auth())
    problem = Problem(contest).load_from_dict(r.json())
    return problem


def all(connection, contest):
    if type(contest) is Contest:
        contest = contest.id
    r = requests.get(
        f"{connection.endpoint}data/contests/{contest}/problems/",
        headers=connection.headers_with_auth())
    results = []
    for c in r.json():
        results.append(Problem(contest).load_from_dict(c))
    return results
