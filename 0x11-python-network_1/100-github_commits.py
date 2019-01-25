#!/usr/bin/python3
"""list 10 commits (from the most recent to oldest) of the
repository “rails” by the user “rails”
"""
import requests
import sys


def takeDate(elem):
    """Helper function to sort GitHub commit results by date"""
    return elem.get("commit").get("author").get("date")

if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)

    r = requests.get(url)
    try:
        result = r.json()
    except:
        print("Not a valid JSON")
    result.sort(key=takeDate, reverse=True)
    for i in range(10):
        sha = result[i].get("sha")
        name = result[i].get("commit").get("author").get("name")
        print("{}: {}".format(sha, name))
