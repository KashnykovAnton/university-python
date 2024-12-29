# Agregation - better to use
class Animal:
    def __init__(self, nickname, age, owner):
        self.__nickname = nickname
        self.__age = age
        self.__owner = owner

class Owner:
    def __init__(self, name, phone):
        self.__name = name
        self.__phone = phone


andrii = Owner("Andrii", "1234567890")

cat = Animal("Tom", 3, andrii)


# Composition
class Animal:
    def __init__(self, nickname, age, owner_name, owner_phone):
        self.__nickname = nickname
        self.__age = age
        self.__owner = Owner(owner_name, owner_phone)

class Owner:
    def __init__(self, name, phone):
        self.__name = name
        self.__phone = phone

cat = Animal("Tom", 3, "Andrii", "1234567890")

# Singleton pattern

# Example when two examples of the class have different memory addresses
class DatabaseConnection:
    def __init__(self, password):
        self.__password = password


d1 = DatabaseConnection("123456")
d2 = DatabaseConnection("123456")
print(d1, d2)

# Example when two examples of the class have the same memory address
class DatabaseConnection:
    __instance = None

    def __new__(cls, password):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, password):
        self.__password = password

d1 = DatabaseConnection("123456")
d2 = DatabaseConnection("123456")
print(d1, d2)

# Abstract class - Polymorphism
from abc import ABC, abstractmethod

class Developer(ABC):
    @abstractmethod # decorator for abstract method, should be at least one abstract method in the class
    def write_code(self):
        pass

# developer = Developer() # TypeError: Can't instantiate abstract class Developer with abstract methods write_code

class PythonDeveloper(Developer):
    def write_code(self):
        return "Python developer writes code"

python_dev = PythonDeveloper()
print(python_dev.write_code())