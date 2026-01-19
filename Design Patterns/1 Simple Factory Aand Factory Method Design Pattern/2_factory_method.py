"""
Simple Factory Pattern centralizes object creation logic into one class instead of spreading if/else everywhere.
Client → Factory → Concrete Object
"""

from abc import ABC, abstractmethod

# Product Interface
class Shape(ABC):
    """
    It enforces: Every concrete Shape must implement draw()
    """
    @abstractmethod
    def draw(self):
        return "Shape: "

# Concrete Products
class Circle(Shape):
    def draw(self):
        return super().draw() + "Drawing a Circle"

class Square(Shape):
    def draw(self):
        return super().draw() + "Drawing a Square"

class Rectangle(Shape):
    def draw(self):
        return super().draw() + "Drawing a Rectangle"


# Interface for Factory Method
class ShapeFactory:
    @abstractmethod
    def create_shape(self) -> Shape:
        pass

class CircleFactory(ShapeFactory):
    def create_shape(self) -> Shape:
        return Circle()


class SquareFactory(ShapeFactory):
    def create_shape(self) -> Shape:
        return Square()


class RectangleFactory(ShapeFactory):
    def create_shape(self) -> Shape:
        return Rectangle()

# Client code
if __name__ == "__main__":
    circle_factory = CircleFactory()
    square_factory = SquareFactory()
    rectangle_factory = RectangleFactory()

    shape1 = circle_factory.create_shape()
    shape2 = square_factory.create_shape()
    shape3 = rectangle_factory.create_shape()

    print(shape1.draw())
    print(shape2.draw())
    print(shape3.draw())