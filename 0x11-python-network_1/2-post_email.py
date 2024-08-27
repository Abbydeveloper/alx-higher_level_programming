#!/usr/bin/python3
"""Take a URL and an email, send a POST request to the passed URL with the email as a paramet, and display the body of the response"""


if __name__ == "__main__":
    import sys
    from urllib import request
    import urllib.parse

    url = sys.argv[1]
    email = sys.argv[2]
    val = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(val)
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(url) as resp:
        body = response.read()
        print(body.decode('utf-8'))
