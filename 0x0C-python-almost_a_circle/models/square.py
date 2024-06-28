#!/usr/bin/python3
"""Square Modle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square Class"""

        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation of a Square instance"""

        string = "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.__width)
        return (string)
