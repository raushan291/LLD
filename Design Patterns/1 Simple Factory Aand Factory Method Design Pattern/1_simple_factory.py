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

class Retanagle(Shape):
    def draw(self):
        return super().draw() + "Drawing a Rectangle"


# Simple Factory
class ShapeFactory:
    """
    We use @staticmethod when:
    The method does NOT depend on any instance variables (self) or class variables (cls).
    """
    @staticmethod
    def create_shape(shape_type: str) -> Shape:
        shape_type = shape_type.lower()
        
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        elif shape_type == "rectangle":
            return Retanagle()
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")

# Client code
if __name__ == "__main__":
    shape1 = ShapeFactory.create_shape("circle")
    shape2 = ShapeFactory.create_shape("square")
    shape3 = ShapeFactory.create_shape("rectangle")

    print(shape1.draw())
    print(shape2.draw())
    print(shape3.draw())
