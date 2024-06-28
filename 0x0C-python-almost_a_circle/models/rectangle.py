#!/usr/bin/python3

"""Rectangle Module"""


class Rectangle(Base):
    """Rectangle class inherits from the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the Rectangle class"""

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super9).__init__(id)

    @property
    def width(self):
        """Retrieve the width attribute"""

        return self.__width

    @property
    def height(self):
        """Retrieve the height attribute"""

        return self.__height

    @property
    def x(self):
        """Retrieve the x attribute"""

        return self.__x

    @property
    def y(self):
        """Retrieve the y attribute"""

        return self.__y
