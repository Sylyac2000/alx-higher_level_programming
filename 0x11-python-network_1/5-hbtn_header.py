#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in the
header of the response.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) == 2:
        listargs = argv[1:]
        theurl = listargs[0]

        response = requests.get(theurl)
        headers = response.headers
        if 'X-Request-Id' in headers:
            print(headers['X-Request-Id'])
