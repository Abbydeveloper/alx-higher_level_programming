#!/usr/bin/python3

"""MyInt Module"""


class MyInt(int):
    """MyInt class"""

    def __init__(self, other):
        """Initialize the Myint class"""
        super().__init__()

    def __eq__(self, other):
        """Executes the inequality function"""

        return super().__ne__(other)

    def __ne__(self, other):
        """Executes the equality function"""

        return super().__eq__(other)
