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
    theurl = 'http://0.0.0.0:5000/search_user'
    payload = {'q': q}
    response = requests.post(theurl, data=payload)

    try:
        responsedict = response.json()
        if responsedict:
            print("[{}] {}".format(responsedict.get('id'), responsedict.get('name')))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
