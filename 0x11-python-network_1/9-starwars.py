#!/usr/bin/python3
"""Takes in a string and sends a search request to the Star Wars API.
"""
import requests
import sys

if __name__ == '__main__':
    val = sys.argv[1]
    search_url = 'https://swapi.co/api/people/?search=' + val

    r = requests.get(search_url)
    json_repr = r.json()
    count = json_repr.get('count')
    print("Number of results: {}".format(count))
    try:
        for i in range(count):
            result = json_repr.get('results')[i].get('name')
            print("{}".format(result))
    except:
        pass
