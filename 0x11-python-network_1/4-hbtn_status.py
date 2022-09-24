#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
using requests
"""

if __name__ == "__main__":
    import requests

    thehtml = ""
    theurl = "https://alx-intranet.hbtn.io/status"
    response = requests.get(theurl)
    print('Body response:')
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
