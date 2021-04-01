# Factory Design Pattern
from abc import ABC, abstractmethod

class Shape(ABC):

    @staticmethod
    @abstractmethod
    def draw():
        pass

class Rectangle(Shape):
    @staticmethod
    def draw():
        print("Rectangle Shape")

class Circle(Shape):
    @staticmethod
    def draw():
        print("Circle Shape")

class Square(Shape):
    @staticmethod
    def draw():
        print("Square Shape")

class ShapeFactory:

    @staticmethod
    def get_shape(shape_type):
        if shape_type == '':
            return None
        elif shape_type == 'CIRCLE':
            return Circle()
        elif shape_type == 'RECTANGLE':
            return Rectangle()
        elif shape_type == 'SQUARE':
            return Square()
        return None

class Main:
    shape_factory = ShapeFactory()

    shape1 = shape_factory.get_shape('RECTANGLE')
    if shape1:
        shape1.draw()

    shape2 = shape_factory.get_shape('SQUARE')
    if shape2:
        shape2.draw()

    shape3 = shape_factory.get_shape('')
    if shape3:
        shape3.draw()


if __name__ == '__main__':
    Main()

