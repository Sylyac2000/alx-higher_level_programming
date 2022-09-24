#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    q = argv[1] if len(argv) == 2 else ""
    theurl = 'http://bebef3794618.4bd1fe4c.alx-cod.online:5000/search_user'
    response = requests.post(theurl, data={'q': q})
    try:
        responsedict = response.json()
        id, name = responsedict.get('id'), responsedict.get('name')
        if len(responsedict) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(responsedict.get('id'), responsedict.get('name')))
    except:
        print("Not a valid JSON")
