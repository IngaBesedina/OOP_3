#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
В некой игре-стратегии есть солдаты и герои.
У всех есть свойство, содержащее уникальный номер объекта, и свойство,
в котором хранится принадлежность команде. У солдат есть метод "иду за героем",
который в качестве аргумента принимает объект типа "герой".
У героев есть метод увеличения собственного уровня.
В основной ветке программы создается по одному герою для каждой команды.
В цикле генерируются объекты-солдаты.
Их принадлежность команде определяется случайно.
Солдаты разных команд добавляются в разные списки.
Измеряется длина списков солдат противоборствующих команд и выводится на экран.
У героя, принадлежащего команде с более длинным списком, увеличивается уровень.
Отправьте одного из солдат первого героя следовать за ним.
Выведите на экран идентификационные номера этих двух юнитов.
"""

import random


class Unit:
    def __init__(self, unit_id, team):
        self.__unit_id = unit_id
        self.__team = team

    @property
    def unit_id(self):
        return self.__unit_id

    @unit_id.setter
    def unit_id(self, unit_id):
        self.__unit_id = unit_id

    @property
    def team(self):
        return self.__team

    @team.setter
    def team(self, team):
        self.__team = team


class Soldier(Unit):
    def __init__(self, unit_id, team):
        super().__init__(unit_id, team)

    def follow_hero(self, hero):
        if isinstance(hero, Hero):
            return f"Солдат {self.unit_id} следует за героем {hero.unit_id}"
        else:
            return ValueError


class Hero(Unit):
    def __init__(self, unit_id, team, level=1):
        super().__init__(unit_id, team)
        self.__level = level

    @property
    def level(self):
        return self.__level

    def level_up(self):
        self.__level += 1
        return f"Уровень героя {self.unit_id}: {self.level}"


def main():
    hero1 = Hero(1, "A")
    hero2 = Hero(2, "B")

    soldiers_team_a = []
    soldiers_team_b = []

    for i in range(10):
        team = random.choice(["A", "B"])
        soldier = Soldier(i + 3, team)
        if team == "A":
            soldiers_team_a.append(soldier)
        if team == "B":
            soldiers_team_b.append(soldier)

    len_a = len(soldiers_team_a)
    len_b = len(soldiers_team_b)

    print(f"Команда A: {len_a} солдат")
    print(f"Команда B: {len_b} солдат")

    if len_a > len_b:
        print(hero1.level_up())
    else:
        print(hero2.level_up())

    print("Номера солдат команды А", end=": ")
    for soldier in soldiers_team_a:
        print(soldier.unit_id, end=", ")

    print()
    print(soldiers_team_a[random.randint(0, len_a - 1)].follow_hero(hero1))


if __name__ == "__main__":
    main()
