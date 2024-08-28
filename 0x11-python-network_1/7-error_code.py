#!/usr/bin/python3
"""Take a URL, send a request to the URL and display the obdy of the response"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.post(url, data={'email': sys.argv[2]})
    print(req.text)
