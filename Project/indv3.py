#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Вариант 1
Требуется реализовать абстрактный базовый класс,
определив в нем абстрактные методы и свойства.
Эти методы определяются в производных классах.
В базовых классах должны быть объявлены абстрактные методы ввода/вывода,
которые реализуются в производных классах.
Создать абстрактный базовый класс Figure
с абстрактными методами вычисления площади и периметра.
Создать производные классы: Rectanglе (прямоугольник), Circle (круг),
Trapezium (трапеция) со своими функциями площади и периметра.
"""

from abc import ABC, abstractmethod
from math import pi


class Figure(ABC):
    def __init__(self, h) -> None:
        self.h = h

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def square(self):
        pass


class Rectangle(Figure):
    def __init__(self, h, a) -> None:
        super().__init__(h)
        self.a = a

    def perimeter(self):
        return 2 * (self.h + self.a)

    def square(self):
        return self.h * self.a


class Circle(Figure):
    def __init__(self, h) -> None:
        super().__init__(h)

    def perimeter(self):
        return pi * self.h

    def square(self):
        return pi * (self.h / 2) ** 2


class Trapezium(Figure):
    def __init__(self, h, a, b, c, d) -> None:
        super().__init__(h)
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def square(self):
        return ((self.a + self.b) * self.h) / 2


def main():
    rect = Rectangle(30, 50)
    print(f"Периметр прямоугольника: {rect.perimeter()}")
    print(f"Площадь прямоугольника: {rect.square()}")

    circ = Circle(30)
    print(f"Периметр круга: {circ.perimeter()}")
    print(f"Площадь круга: {circ.square()}")

    trap = Trapezium(8, 14, 26, 10, 10)
    print(f"Периметр трапеции: {trap.perimeter()}")
    print(f"Площадь трапеции: {trap.square()}")


if __name__ == "__main__":
    main()
