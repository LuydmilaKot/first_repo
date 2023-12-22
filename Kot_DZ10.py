# №1, 2
import time
class Auto:
    def __init__(self, brand, age, mark, color='', weight=''):
        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
        print('move')

    def stop(self):
        print('stop')

    def birthday(self):
        self.age +=1
        print(self.age)

audi = Auto('Audi', 2008, 'A6')
audi.move()
audi.stop()
audi.birthday()

class Truck(Auto):
    def __init__(self, brand, age, mark, max_load, color='', weight=''):
        super().__init__(brand, age, mark, color='', weight='')
        self.max_load = max_load
    def move(self):
        print('attention!')
        super().move()

    def load(self):
        time.sleep(1)
        print('sleep')
        time.sleep(1)

volvo = Truck('Volvo', 2010, 'FH', 10000)
volvo.move()
volvo.load()

renault = Truck('Renault', 2005, 'Master', 5000)
renault.move()
renault.load()

class Car(Auto):
    def __init__(self, brand, age, mark, max_speed, color='', weight=''):
        super().__init__(brand, age, mark, color='', weight='')
        self.max_speed = max_speed
    def move(self):
        super().move()
        print(f'max speed {self.max_speed}')


mercedes = Car('Mercedes', 2010, 'Benz', 300)
mercedes.move()

renault = Car('Renault', 2019, 'Captur', 250)
renault.move()
#########################################################################
# №3 -- решение, найденное в интернете
import math

class Point():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other): #если х == у -> True
        return self.x == other.x and self.y == other.y

    def __add__(self, other): #сложение объектов
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self): #обычный вывод информации
        return f'({self.x}, {self.y})'

    def distance_from_origin(self):
        return math.hypot(self.x, self.y) #расстояние между двумя векторами (координатами)


class Circle(Point):

    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __str__(self):
        return super().__str__()[:-1] + f', radius={self.radius})'

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        radius = self.radius + other.radius
        return Circle(radius, x, y)

    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin() - self.radius)

    def circumference(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        radius = self.radius - other.radius
        return Point(radius, x, y)
