#!/usr/bin/python3
"""List the 10 most recent commints from any given GitHub repository"""

import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}.commits".format(
           sys.argv[2], sys.argv[1])

    req = requests.get(url)
    commits = req.json()
    try:
        for i in range(10):
            print(f"{commits[i]['sha']}: {commits[i]['commit']['author']['name']}")
    except IndexError:
        pass
