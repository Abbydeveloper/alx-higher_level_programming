#!/usr/bin/python3
"""Module 100 - My Int"""


class MyInt(int):
    """Class inherits from int"""

    def __eq__(self, other):
        """Change equality to become inequality"""

        return super().__ne__(other)

    def __ne__(self, other):
        """Change inequality to become equality"""

        return super().__eq__(other)
