#!/usr/bin/python3
"""
Write a Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and finally displays the body of the response.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) == 2:
        thehtml = ""
        listargs = argv[1:]
        theurl = 'http://0.0.0.0:5000/search_user'
        if listargs[1]:
            donnees = {'q': listargs[1]}
        else:
            donnees = {'q': ''}
        response = requests.post(theurl, donnees)

        try:
            dicdata = response.json()
            if dicdata:
                print("[{}] {}".format(dicdata.get('id'), dicdata.get('name')))
            else:
                print("No result")
        except ValueError as e:
            print("Not a valid JSON")
