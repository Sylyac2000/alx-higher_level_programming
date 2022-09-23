#!/bin/bash
#a Bash script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -s -X POST -F "email=test@gmail.com" -F "subject =I will always be here for PLD" "$1"
