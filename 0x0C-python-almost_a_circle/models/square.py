#!/usr/bin/python3
"""Square Modle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square Class"""

        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Retrieve the value of size"""

        return self.__width

    @size.setter
    def size(self, value):
        """Set the value of the size attribute"""

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value
        self.__height = value

    def __str__(self):
        """String representation of a Square instance"""

        string = "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.__width)
        return (string)
