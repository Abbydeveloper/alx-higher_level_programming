#!/usr/bin/python3
"""Take in a letter and send a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
    else:
        arg = ""
    data = {'q': arg}
    url = "http://0.0.0.0:5000/search_user"
    req = requests.post(url, data)
    try:
        req.raise_for_status()
        json = req.json()
        if len(json) == 0:
            print("No result")
        else:
            print("[{:d}] {}".format(json['id'], json['name']))
    except Exception:
        print("Not a valid JSON")
