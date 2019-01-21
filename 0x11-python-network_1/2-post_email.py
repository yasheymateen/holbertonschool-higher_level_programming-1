#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request to the passed URL with
the email as a parameter, and displays the body of the response
"""
import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    values = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        retval = response.read()
        print(retvl.decode())
