#!/usr/bin/python3
"""Take in a URL and an email address, send a post request to the
URL with the email as a parameter and display the body of the response"""


import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.post(url, data={'email': sys.argv[2]})
    print(req.text)
