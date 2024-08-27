#!/usr/bin/python3
"""Take a URL and an email, send a POST request to the passed URL with the
email as a parameter, and display the body of the response"""


if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as resp:
            body = resp.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
