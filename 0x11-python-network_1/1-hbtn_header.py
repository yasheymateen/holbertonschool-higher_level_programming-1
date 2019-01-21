#!/usr/bin/python3
"""Script that takes url, sends a request to the URL, and displays the value
of the X-Request-Id variable found in the response header
"""
import sys
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        # file-like response object has info method that returns a dictionary
        # like object that describes the page fetched, particularly the headers
        headers = response.info()
        print(headers.get('X-Request-Id'))
