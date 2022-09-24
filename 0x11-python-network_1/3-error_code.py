#!/usr/bin/python3
"""
A Python script that takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id variable found in the
header of the response.
"""

if __name__ == "__main__":
    from urllib import request, error
    from sys import argv

    if len(argv) == 2:
        thehtml = ""
        listargs = argv[1:]
        theurl = listargs[0]

        try:
            req = request.Request(theurl)
            with request.urlopen(req) as response:
                print(response.read().decode('utf-8'))
        except error.HTTPError as e:
            print("Error code: {}".format(e.code))
