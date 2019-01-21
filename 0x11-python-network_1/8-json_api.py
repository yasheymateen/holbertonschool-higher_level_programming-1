#!/usr/bin/python3
"""Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
If the response body is properly JSON formatted and not empty, display the id
and name like this: [<id>] <name>
"""
import requests
import sys

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) == 1:
        letter = ""
    else:
        letter = sys.argv[1]
    r = requests.post(url, data={'q': letter})
    instance = r.json()
    if len(instance) == 0:
        print("No result")
    else:
        print("[{}] {}".format(instance.get('id'), instance.get('name')))
