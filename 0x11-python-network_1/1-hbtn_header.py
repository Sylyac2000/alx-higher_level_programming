#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in the
header of the response.
"""

if __name__ == "__main__":
    from urllib import request
    from sys import argv

    if len(argv) == 2:
        thehtml = ""
        listargs = argv[1:]
        theurl = listargs[0]
        req = request.Request(theurl)
        with request.urlopen(req) as response:
            thehtml = response.headers
            if 'X-Request-Id' in thehtml:
                print(thehtml['X-Request-Id'])
