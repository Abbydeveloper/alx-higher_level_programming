#!/usr/bin/python3
"""Define a function that applies text indentation after specific characters"""


def text_indentation(text):
    """Print text indentation after every '.', '?', ':'

    Args:
    text (string): text to print
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    i = 0
    while (i < len(text) and text[i] == ' '):
        i += 1

    while i < len(text):
        print(text[i], end="")
        if (text[i] == '\n' or text[i] in '.?:'):
            if text[i] in '.?:':
                print('\n')
            i += 1

            while (i < len(text) and text[i] == ' '):
                i += 1
            continue
        i += 1
