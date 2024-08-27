#!/usr/bin/python3
"""Take a URL and an email, send a POST request to the passed URL with the
email as a parameter, and display the body of the response"""


if __name__ == "__main__":
    import sys
    import urllib.request
    import urllib.parse

    url = sys.argv[1]
    email = sys.argv[2]
    val = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(val)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as resp:
        body = response.read()
        print(body.decode('utf-8'))
