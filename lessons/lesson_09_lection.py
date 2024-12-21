class Location: 
    # __<name>__ - magic methods or dunder methods
    # magic method means that it is called implicitly
    # __init__ - constructor
    # self - analogue of "this" in JS
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def get_coordinates(self):
        return self.lat, self.lon
    
    def print_info(self):
        coordinates = self.get_coordinates()
        message = f"Location on the map: {self.name} with coordinates {coordinates}"
        print(message)

oslo = Location("Oslo", 59.9, 10.75)

# oslo => instance/example/object
# Location => class, type, pattern

# print(type(oslo))
# print(oslo)
print(oslo.name)
print(oslo.lat, oslo.lon)
coordinates = oslo.get_coordinates()
print(type(coordinates))
print(coordinates)
oslo.print_info()

# Example with dataclass
print("----------------------------")

from dataclasses import dataclass

@dataclass
class LocationWithDecorator:
    name: str
    lat: float = 0.0
    lon: float = 0.0

    def get_coordinates(self):
        return self.lat, self.lon
    
    def print_info(self):
        coordinates = self.get_coordinates()
        message = f"Location on the map: {self.name} with coordinates {coordinates}"
        print(message)

lviv = LocationWithDecorator("Lviv", 49.84, 24.03)
print(lviv.name)
print(lviv.lat, lviv.lon)
coordinates = lviv.get_coordinates()
print(coordinates)
lviv.print_info()

# ---- Example with encapsulation
print("----------------------------")

class LocationWithEncapsulation:
    def __init__(self, name, lat, lon):
        # public - accessible everywhere
        # protected - accessible in the class and its subclasses (childs)
        # private - accessible only in the class

        self.__name = name
        self.lat = lat
        self.lon = lon

    # def distance_to(self, other):
    #     # https://en.wikipedia.org/wiki/Haversine_formula
    #     r = 6371  # Earth radius in kilometers
    #     lam_1, lam_2 = radians(self.lon), radians(other.lon)
    #     phi_1, phi_2 = radians(self.lat), radians(other.lat)
    #     h = (sin((phi_2 - phi_1) / 2)**2
    #          + cos(phi_1) * cos(phi_2) * sin((lam_2 - lam_1) / 2)**2)
    #     return 2 * r * asin(sqrt(h))

    def get_coordinates(self):
        return self.lat, self.lon
    
    def print_info(self):
        coordinates = self.get_coordinates()
        message = f"Location on the map: {self.__name} with coordinates {coordinates}"
        print(message)


kyiv = LocationWithEncapsulation("Kyiv", 50.45, 30.52)

# print(kyiv.name) # will be an error
# print(kyiv.__name) # also will be an error
print(kyiv._LocationWithEncapsulation__name) # will work - but it is not recommended - it is a bad practice

# ---- Example with inheritance
print("----------------------------")

class Person:
    def __init__(self, name, year, city):
        self.name = name
        self.year = year
        self.city = city

    def print_info(self):
         print(f"I'm {self.name}, {self.year} years old from {self.city}")


p = Person("Alex", 29, "Kyiv")
print(p)
print(p.name)
p.print_info()

class Developer(Person):
    pass

dev = Developer("Alex", 29, "Kharkiv")
dev.print_info()

class DeveloperWithLanguage(Person):
    # class attribute
    is_profitable = True

    def __init__(self, name, year, city, language):
        # object attribute or property
        super().__init__(name, year, city)
        # Person.__init__(self, name, year, city) - alternative way
        self.language = language

    def print_info(self):
        super().print_info()
        print(f"I'm a {self.language} developer")

dev_lang = DeveloperWithLanguage("Ivan", 35, "Odessa", "Python")
dev_lang.print_info()
print(DeveloperWithLanguage.is_profitable)
print(dev_lang.is_profitable)


# Example with Diamond inheritance
print("----------------------------")

#    A
#   / \
#  B   C
#   \ /
#    D

class A:
    x = "a"

class B:
    x = "b"

class C:
    x = "c"

#  Example 1
# class D(B, C):
#     x = "d"

#  Example 2
# class D(B, C):
#     pass

# Example 3
class D(C, B):
    pass

d = D()
print(d.x)

# MRO - Methos Resolution Order
print(D.__mro__)

# ---- Example with polymorphism
print("----------------------------")

class Animal:
    def __init__(self, nickname: str, age: int) -> None:
        self.nickname = nickname
        self.age = age

    def sound(self):
        pass

class Cat(Animal):
    def __init__(self, nickname: str, age: int, owner: str) -> None:
        super().__init__(nickname, age)
        self.owner = owner

    def sound(self) -> str:
        return f"{self.nickname} says Meow!"

class Dog(Animal):
    def __init__(self, nickname: str, age: int, owner: str) -> None:
        super().__init__(nickname, age)
        self.owner = owner

    def sound(self) -> str:
        return f"{self.nickname} says Woof!"

cat = Cat("Simon", 4, "Yurii")
dog = Dog("Alisa", 7, "Vlad")

for animal in [cat, dog]:
    print(animal.sound())
