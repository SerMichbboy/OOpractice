from functools import partial
from itertools import chain
import random
import time


class Person:
    def __init__(self, name, chlen):
        self.hp = 100
        self.mp = 0
        self.dmg = 10
        self.armor = 0
        self.name = name
        self.dick = chlen
        self.attack_methods = [self._punch] * 10 + [self._dick_punch] * 1
        self.crit_dmg = 0.25
        self.crit_chance = 0.07

    def _punch(self, enemy):
        dmg = round(self.dmg * (1 - enemy.armor))
        dmg = random.randint(0, dmg)
        print(f"Удар яростным кулаком!")
        return dmg

    def _dick_punch(self, enemy):
        dmg = round(self.dmg * (1 - enemy.armor))
        dmg = random.randint(0, dmg) + 10
        print(f"Атака членом по лбу!")
        return dmg + dmg * (self.dick / 100)

    def attack(self, enemy):
        method = random.choice(self.attack_methods)
        dmg = method(enemy)
        if random.randint(0, 100) < self.crit_chance * 100:
            dmg += dmg * self.crit_dmg
            print('Критическая пиздюля!')
        enemy.hp -= dmg
        print(f"Въебал {dmg}")


class Human(Person):
    def __init__(self, name, chlen, prof):
        super().__init__(name, chlen)
        self.mp += 40
        self.armor += 0.4
        prof(self)


class Ork(Person):
    def __init__(self, name, chlen, prof):
        super().__init__(name, chlen)
        self.hp += 10
        self.mp += 20
        self.dmg += 12
        self.armor += 0
        prof(self)


def leg_punch(person, enemy):
    dmg = round(person.dmg * (1 - enemy.armor)) + 5
    dmg = random.randint(0, dmg)
    print(f"Удар c ноги по ебальнику!")
    return dmg


class Warrior:
    def __init__(self, person):
        person.dmg += 5
        person.armor += 0.2
        person.hp += 10
        person.attack_methods = [x for x in chain(person.attack_methods, [partial(leg_punch, person)] * 5)]


man = Human('Vasya', 15, Warrior)
ork = Ork('Zuldan', 25, Warrior)

while man.hp > 0 and ork.hp > 0:
    print(f"Бьет {man.name}")
    man.attack(ork)
    time.sleep(0.5)
    print(f"Бьет {ork.name}")
    ork.attack(man)
    time.sleep(0.5)
winner = man if man.hp > ork.hp else ork
loser = ork if winner == man else man
print(f"{winner.name} разъебал {loser.name} в щепки")


class PC:
    def __init__(self, mem, hard_mem, model, cpu):
        self.mem = mem
        self.hard_mem = hard_mem
        self.model = model
        self.cpu = cpu


class Desktop(PC):
    def __init__(self, mem, hard_mem, model, cpu, mon, mouse, keyboard):
        super().__init__(mem, hard_mem, model, cpu)
        self.mon = mon
        self.mouse = mouse
        self.keyboard = keyboard


class Notebooks(PC):
    def __init__(self, mem, hard_mem, model, cpu, size, display):
        super().__init__(mem, hard_mem, model, cpu)
        self.size = size
        self.display = display


nb = Notebooks(1000, 10000, 2105, 'intel', 16, 'IPS')

for x, y in nb.__dict__.items():
    print(x, y)


class Calendar:
    __slots__ = 'day', 'month', 'year'

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def get_info(self):
        a = input()
        if a == 'month':
            print(f'Месяц {self.month}')
        elif a == 'day':
            print(f'День {self.day}')
        else:
            print(f'Год {self.year}')


cal = Calendar(1, 2, 1992)
print(cal.get_info())
