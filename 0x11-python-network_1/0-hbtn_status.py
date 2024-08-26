#!/usr/bin/python3
"""Fetch https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    from urllib import request
    with request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        text = resp.read()
        print('Body response:')
        print('\t- type: {}'.format(type(text)))
        print('\t- text: {}'.format(text))
        print('\t utf8 content: {}'.format(text.decode('utf-8')))
