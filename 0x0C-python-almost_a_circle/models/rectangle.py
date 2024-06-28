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

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Retrieve the height attribute"""

        return self.__height

    @height.setter
    def height(self, value):
        """Set the height attribute"""

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """Retrieve the x attribute"""

        return self.__x

    @x.setter
    def x(self, value):
        """Set the x attribute"""

        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """Retrieve the y attribute"""

        return self.__y

    @y.setter
    def y(self, value):
        """Set the y attribute"""

        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Return the area of the Rectangle instance"""

        return (self.__height * self.__width)

    def display(self):
        """Printin stdout the Rectangle instance with the character
        #"""

        for a in range(self.__y):
            print()
        for i in range(self.__height):
            for b in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print('#', end="")
            print("")

    def __str__(self):
        """Return teh strig representation of a Rectangle instance"""

        return ("[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """update value of a Rectangle insance"""

        if args is not None and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for (key, value) in kwargs.items():
                if key == 'id':
                    self.id = value
                if key == 'width':
                    self.width = value
                if key == 'height':
                    self.height = value
                if key == 'x':
                    self.x = value
                if key == 'y':
                    self.y = value

    def to_dictionary(self):
        """Return the dictionary representation of a rectangle"""

        rect = {
                'id': id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y
                }
        return (rect)
