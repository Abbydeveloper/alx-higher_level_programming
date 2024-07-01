#!/usr/bin/python3

"""Base Module
Base classes for all other classes in this project
"""
import json
import csv
"""|import turtle"""


class Base():
    """Base Class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the base class"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """return the JSON string representation of list_dictioanries"""

        if list_dictionaries is None or list_dictionaries == []:
            return ('[]')
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file"""

        filename = cls.__name__ + '.json'
        with open(filename, mode='w') as jsonfile:
            if list_objs is None:
                jsonfile.write('[]')
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string"""

        if json_string is None or len(json_string) == 0:
            return ([])
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set"""

        if dictionary and dictionary != {}:
            if cls.__name__ == 'Rectangle':
                new_instance = cls(1, 1)
            else:
                new_instance = cls(1)
            new_instance.update(**dictionary)
            return new_instance

    @classmethod
    def load_from_file(cls):
        """Return a list of instances"""

        filename = str(cls.__name__) + '.json'
        try:
            with open(filename, mode='r') as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serialize in CSV"""

        filename = cls.__name__ + '.csv'
        with open(filename, mode='w', newline='') as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write('[]')
            else:
                if cls.__name__ == 'Rectangle':
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
                writer = csv.DictWriter(csvfile, fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserialize in CSV"""

        filename = cls.__name__ + '.csv'
        try:
            with open(filename, mode='r', newline='') as csvfile:
                if cls.__name__ == 'Rectangle':
                    fieldnames = ['id', 'width', 'height', 'x', 'y']
                else:
                    fieldnames = ['id', 'size', 'x', 'y']
                list_dicts = csv.DictReader(csvfile, fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return ([cls.create(**d) for d in list_dicts])
        except IOError:
            return []
    """
    @staticmethod
    def draw(list_rectangles, list_squares):
        Draw Rectangles and Squares using the turtle module

        trtle = turtle.Turtle()
        trtle.screen.bgcolor('#b7312c')
        trtle.pensize(3)
        trtle.shape('turtle')

        trtle.color('#fff')
        for rectangle in list_rectangles:
            trtle.showturtle()
            trtle.up()
            trtle.goto(rectangle.x, rectangle.y)
            trtle.down()
            for i in range(2):
                trtle.forward(rectangle.width)
                trtle.left(90)
                trtle.forward(rectangle.height)
                trtle.left(90)
            trtle.hideturtle()

        trtle.color('#b5e3d8')
        for square in list_squares:
            trtle.showturtle()
            trtle.up()
            trtle.goto(square.x, square.y)
            trtle.down()
            for i in range(2):
                trtle.forward(square.wisth)
                trtle.left(90)
                trtle.forward(square.height)
                trtle.left(90)
            trtle.hideturtle()

        turtle.exitonclick()
    """
