#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the
body of the response.
"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as request:
            the_page = request.read()
            print(the_page.decode())
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
