#!/usr/bin/python3

"""Rectangle Module"""

from models.base import Base

class Rectangle(Base):
    """Rectangle class inherits from the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle class"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Retrieve the width attribute"""

        return self.__width

    @width.setter
    def width(self, value):
        """Set the width attribute"""

        self.__width = value

    @property
    def height(self):
        """Retrieve the height attribute"""

        return self.__height

    @height.setter
    def height(self, value):
        """Set the height attribute"""

        self.__height = value

    @property
    def x(self):
        """Retrieve the x attribute"""

        return self.__x

    @x.setter
    def x(self, value):
        """Set the x attribute"""

        self.__x = value

    @property
    def y(self):
        """Retrieve the y attribute"""

        return self.__y

    @y.setter
    def y(self, value):
        """Set the y attribute"""

        self.__y = value
