#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) == 3:
        thehtml = ""
        listargs = argv[1:]
        theurl = listargs[0]
        donnees = {'email': listargs[1]}

        response = requests.post(theurl, donnees)
        print(response.text)
