import math
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): # Вычисляет площадь фигуры
        pass

    @abstractmethod
    def perimeter(self): # Вычисляет периметр фигуры
        pass


class Rectangle(Shape):
    def __init__(self, length, width): # Инициализация нового экземпляра класса Rectangle
        self.length = length # длина прямоугольника
        self.width = width # ширина прямоугольника

    def area(self): # Вычисление площади прямоугольника
        return self.length * self.width

    def perimeter(self): # Вычисление периметра прямоугольника
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius): # Инициализация нового экземпляра класса Circle
        self.radius = radius

    def area(self): # Вычисление площади окружности
        return math.pi * self.radius ** 2

    def perimeter(self): # Вычисление длины окружности
        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, a, b, c): # Инициализация нового экземпляра класса Triangle
        self.a = a
        self.b = b
        self.c = c

    def area(self): # Вычисление площади треугольника по формуле Герона
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self): # Вычисление периметра треугольника
        return self.a + self.b + self.c

def print_shape_info(shape): # Вывод информации о фигуре
 print("Area: {shape.area()}")
 print("Perimeter: {shape.perimeter()}")
