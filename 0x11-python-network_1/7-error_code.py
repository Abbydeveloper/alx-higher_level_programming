#!/usr/bin/python3
"""Take a URL, send a request to the URL and display
the obdy of the response"""

import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = requests.get(url)
    try:
        req.raise_for_status()
        print(req.text)
    except Exception as e:
        print("Error code: {}".format(req.status_code))
