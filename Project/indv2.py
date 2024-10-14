#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Составить программу с использованием иерархии классов.
В раздел программы, начинающийся после инструкции if __name__ = '__main__':
добавить код, демонстрирующий возможности разработанных классов.
Создать базовый класс Car (машина), характеризуемый торговой маркой (строка),
числом цилиндров, мощностью.
Определить методы переназначения и изменения мощности.
Создать производный класс Lorry (грузовик),
характеризуемый также грузоподъемностью кузова.
Определить функции переназначения марки и изменения грузоподъемности.
"""


class Car:
    def __init__(self, brand, cylinders, power):
        self.__brand = brand
        self.__cylinders = cylinders
        self.__power = power

    def __str__(self):
        return "Car(brand: {}, cylinders: {}, power: {}".format(
            self.__brand, self.__cylinders, self.__power
        )

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, new_brand):
        self.__brand = new_brand

    @property
    def cylinders(self):
        return self.__cylinders

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, new_power):
        self.__power = new_power


class Lorry(Car):
    def __init__(self, brand, cylinders, power, load_capacity):
        super().__init__(brand, cylinders, power)
        self.__load_capacity = load_capacity

    def __str__(self):
        return "Lorry({}, {}, {}, load_capacity: {})".format(
            self.brand, self.cylinders, self.power, self.load_capacity
        )

    @property
    def load_capacity(self):
        return self.__load_capacity

    @load_capacity.setter
    def load_capacity(self, new_load_capacity):
        self.__load_capacity = new_load_capacity


def main():
    car = Car("Toyota", 4, 150)
    print(car)

    car.power = 180
    print(car)

    lorry = Lorry("Volvo", 6, 400, 10)
    print(lorry)

    lorry.load_capacity = 12
    lorry.brand = "Scania"
    print(lorry)


if __name__ == "__main__":
    main()
