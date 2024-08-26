#!/usr/bin/python3
"""Take a URL from command line argument, and display the value of
    the X-Request-Id variable found in the header of the response"""


if __name__ == "__main__":
    import sys
    from urllib import request

    url = sys.argv[1]
    with request.urlopen(url) as resp:
        print(dict(resp.headers).get('X-Request-Id'))
