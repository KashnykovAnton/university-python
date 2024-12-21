"""Основи ООП в Python. Класи та об'єкти."""
"""Класи — це структура мови програмування, яка дозволяє об'єднати в рамках однієї сутності змінні різних типів (поля, атрибути) та функції (методи)"""

# Example 1 - Class definition
class Person:
    pass  # Порожній блок для тіла класу

p = Person()

# Example 2
class User:
    name = 'Anonymous'
    age = 15

user1 = User()
print(user1.name)
print(user1.age)

user2 = User()
user2.name = "John"
user2.age = 90

print(user2.name)
print(user2.age)

# Атрибут класу – це змінна, яка визначена на рівні класу, а не екземпляра класу. Це означає, що вона спільна для всіх екземплярів цього класу. Атрибути класу використовуються для зберігання даних, які повинні бути однаковими для всіх об'єктів класу.
class MyClass:
    class_attribute = "I am a class attribute" 

# Поле класу (іноді називається "атрибут екземпляра") – це змінна, яка визначена на рівні окремого екземпляра класу. Кожен екземпляр класу має свій власний набір полів, які можуть приймати різні значення для різних екземплярів. Полем може бути будь-який об'єкт Python. Зазвичай це змінна, або контейнер (словник, список, рядок тощо). Поля класу використовуються для зберігання даних, що специфічні для кожного окремого об'єкта.
class MyClass:
    def __init__(self, value):
        self.instance_field = value  # Поле класу

obj1 = MyClass(5)
obj2 = MyClass(10)

# Метод класу — це функція, яка оперує з полями класу та/або аргументами, які передаються у метод. У будь-якого методу класу завжди повинен бути, принаймні, один аргумент self, це вимога синтаксису Python, оскільки інтерпретатор під час виклику методу обов'язково передасть першим аргументом сам об'єкт, а потім уже всі аргументи, які були передані під час виклику.

class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def say_name(self) -> None:
        print(f'Hi! I am {self.name} and I am {self.age} years old.')

    def set_age(self, age: int) -> None:
        self.age = age
    
    def set_name(self, name: str) -> None:
        self.name = name

bob = Person('Boris', 34)

bob.say_name()
bob.set_age(25)
bob.say_name()
bob.set_name('Bob')
bob.say_name()

# Різниця між полем і атрибутом класу
# У ООП поле і атрибут класу - це два терміни, які часто використовуються як синоніми. Однак між ними є тонка різниця.
# Змінна класу або атрибут – це змінна, яка зберігається в класі та доступ до них мають усі екземпляри цього класу. Змінна класу існує тільки одна, та будь-який з об'єктів, коли змінює змінну класу, змінює її для решти екземплярів цього ж класу.
# Змінна об'єкту або поле - це змінна, яка зберігається в об'єкті. Вона належать кожному окремому екземпляру класу. У цьому випадку кожен об'єкт має свою власну копію поля, тобто вона жодним чином не пов'язана з іншими такими ж полями в інших екземплярах.
class Person:
    count = 0

    def __init__(self, name: str):
        self.name = name
        Person.count += 1

    def how_many_persons(self):
        print(f"Кількість людей зараз {Person.count}")

first = Person('Boris')
first.how_many_persons()
second = Person('Alex')
first.how_many_persons()

# В цьому прикладі ми маємо доступ до змінної класу count
class Person:
    count = 0

    def __init__(self):
        pass

person = Person()
print(person.count)  # 0

# В цьому - вже ні
class Person:
    count = 0

    def __init__(self):
        self.count = 10

person = Person()
print(person.count)  # 10
print(Person.count)  # 0



# --- Example with Pokemon ---
class Pokemon:
    def __init__(self, name, type, health):
        self.name = name
        self.type = type
        self.health = health

    def attack(self, other_pokemon):
        print(f"{self.name} attacks {other_pokemon.name}!")

    def dodge(self):
        print(f"{self.name} dodged the attack!")

    def evolve(self, new_form):
        print(f"{self.name} is evolving into {new_form}!")
        self.name = new_form

# Створення об'єкта Pikachu
pikachu = Pokemon("Pikachu", "Electric", 100)

# Використання методів
pikachu.attack(Pokemon("Charmander", "Fire", 100))
pikachu.dodge()
pikachu.evolve("Raichu")


"""Концепції ООП"""
"""ООП має чотири основні концепції, які відрізняють його від інших методологій програмування:
    Абстракція (Abstraction) - вибіркове незнання - свідоме приховування деяких деталей реалізації, щоб зосередитися на важливих аспектах.
    Інкапсуляція
    Наслідування
    Поліморфізм"""

# --- Інкапсуляція (Encapsulation) - це механізм, який об'єднує дані та методи, які працюють з цими даними, в класі та обмежує доступ до них ззовні. Це означає, що клас приховує внутрішню реалізацію та деталі роботи об'єкта від користувача.
# Загалом інкапсуляція в ООП реалізується через використання публічних (public), захищених (protected) і приватних (private) атрибутів та методів.
    # Public - елемент доступний з будь-якого місця в програмі.
    # Protected - елемент доступний з класу, в якому він оголошений, а також з класів-похідних.
    # Private - елемент доступний лише з класу, в якому він оголошений.

# Example 1 - Public
class Person:
    def __init__(self, name: str, age: int):
        self.name = name # Публічне поле
        self.age = age # Публічне поле

    def greeting(self) -> str:
        return f"Hi {self.name}"

p = Person("Boris", 34)

# Example 2 - Protected
class Person:
    def __init__(self, name: str, age: int, is_active: bool):
        self.name = name # Публічне поле
        self.age = age # Публічне поле
        self._is_active = is_active # Захищене поле (protected)

    def greeting(self):
        return f"Hi {self.name}"

p = Person("Boris", 34, True)
print(p.name, p.age, p._is_active) # Bad practice to access to protected field directly "p._is_active" - but it's possible
print(p.greeting())

# Example 2 - Protected - avoid direct access to protected field:
class Person:
    def __init__(self, name: str, age: int, is_active: bool):
        self.name = name
        self.age = age
        self._is_active = is_active

    def greeting(self):
        return f"Hi {self.name}"
    
    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active

p = Person("Boris", 34, True)
print(p.name, p.age, p.is_active())
print(p.greeting())
print(p.is_active())
p.set_active(False)
print(p.is_active())

# Example 3 - Private
class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name # Публічне поле
        self.age = age # Публічне поле
        self._is_active = is_active # Захищене поле (protected)
        self.__is_admin = is_admin # Приватне поле (private)

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active

p = Person("Boris", 34, True, False)
# print(p.__is_admin) # Will return an error, because it's private field
print(p._Person__is_admin) # We can see private field directly "p._Person__is_admin"

# Example 3 - Private - avoid direct access to private field:
class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = is_active
        self.__is_admin = is_admin

    def greeting(self):
        return f"Hi {self.name}"

    def is_active(self):
        return self._is_active

    def set_active(self, active: bool):
        self._is_active = active

    def get_is_admin(self):
        return self.__is_admin

    def set_is_admin(self, is_admin: bool):
        # Тут можна додати будь-яку логіку перевірки або обробки
        self.__is_admin = is_admin

        
p = Person("Boris", 34, True, False)
print(p.get_is_admin())
p.set_is_admin(True)
print(p.get_is_admin())




# --- Наслідування (Inheritance) - це механізм ООП, який дозволяє одному класу переймати властивості та методи іншого класу. У Python це робиться шляхом оголошення класу, який "наслідується" від іншого класу.
# Базовий або батьківський клас (superclass) це клас, від якого наслідуються властивості та методи.
# Похідний або дочірній клас (subclass) це клас, який наслідує властивості та методи від базового класу.


class Animal: # Базовий клас (superclass)
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass

class Cat(Animal): # Похідний клас (subclass)
    def make_sound(self) -> str:
        return "Meow"

class Dog(Animal): # Похідний клас (subclass)
    def make_sound(self) -> str:
        return "Woof"

class Cow(Animal): # Похідний клас (subclass)
    def make_sound(self):
        return "Moo"

my_cat = Cat("Simon", 4)
my_dog = Dog("Rex", 5)
my_cow = Cow("Bessie", 3)

print(my_cat.make_sound())  # Виведе "Meow"
print(my_dog.make_sound())  # Виведе "Woof"
print(my_cow.make_sound())  # Виведе "Moo"

# Example with additional field - breed and method - chase_tail
# class Dog(Animal):
# def __init__(self, nickname: str, age: int, breed: str):
#         super().__init__(nickname, age)  # Викликаємо конструктор базового класу
#         self.breed = breed  # Додаємо нову властивість

#     def make_sound(self):
#         return "Woof"
    
#     def chase_tail(self) -> str:
#         return f"{self.name} is chasing its tail!"

# my_dog = Dog("Rex", 5, "Golden Retriever")
# print(my_dog.make_sound())  # Виведе "Woof"
# print(my_dog.chase_tail())  # Виведе "Rex is chasing its tail!"




# --- Багаторівневе наслідування та Method Resolution Order (MRO)
# Багаторівневе наслідування - це коли клас наслідує від іншого класу, який вже є похідним класом. Це створює "ланцюжок" наслідування, де можливості передаються через декілька рівнів.
class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass

class Bird(Animal):
    def make_sound(self):
        return "Chirp"

class Parrot(Bird):
    def can_fly(self):
        return True

class TalkingParrot(Parrot):
    def say_phrase(self, phrase):
        return f"The parrot says: '{phrase}'"

my_parrot = TalkingParrot("Alice", 2)
print(my_parrot.make_sound())
print(my_parrot.can_fly())
print(my_parrot.say_phrase("Hello, World!"))

print(TalkingParrot.mro()) 

# Example for MRO
class A:
    name = "Я клас A"

class B:
    name = "Я клас B"
    property = "Я знаходжусь в класі B"

class C(A, B):
    property = "Я знаходжусь в класі C"

c = C()
print(c.name) # Виведе "Я клас A"
print(c.property) # Виведе "Я знаходжусь в класі C"

# OR chnage order of parent classes
class C(B, A):
    property = "Я знаходжусь в класі C"

c = C()
print(c.name) # Виведе "Я клас B"
print(c.property) # Виведе "Я знаходжусь в класі C"




# --- Поліморфізм (Polymorphism) та качина типізація
# Поліморфізм - це один із ключових концептів ООП, який дозволяє об'єктам мати різні форми або поведінку, базуючись на їх типах.
# У контексті ООП, це відноситься до здатності різних класів використовувати методи з однаковою назвою, але з різною реалізацією. Це дозволяє використовувати один інтерфейс для різних типів даних.

class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass

class Cat(Animal):
    def make_sound(self):
        return "Meow"

class Dog(Animal):
    def make_sound(self):
        return "Woof"

def animal_sounds(animals):
    for animal in animals:
        print(animal.make_sound())

animals = [Cat("Simon", 4), Dog("Rex", 5)]
animal_sounds(animals)

# Отже поліморфізм дозволяє обробляти об'єкти різних класів, які є похідними від одного базового класу, через спільний інтерфейс (тобто через однакові методи). 
# Таким чином, поліморфізм дозволяє функції animal_sounds взаємодіяти з об'єктами Cat та Dog як з об'єктами Animal, використовуючи їхні спільні інтерфейси, не зважаючи на різницю в їх внутрішній реалізації. Це робить код більш гнучким і він легше адаптується до змін, оскільки ми можемо додавати нові класи, які наслідують від Animal, без необхідності змінювати функцію animal_sounds.

# !!! Качина типізація (Duck Typing) - це концепція в програмуванні, яка відіграє важливу роль в динамічно типізованих мовах, таких як Python. Назва походить від англійського вислову "Якщо це ходить як качка і крякає як качка, то це, ймовірно, качка".
class Duck:
    def quack(self):
        print("Quack, quack!")

class Person:
    def quack(self):
        print("I'm Quacking Like a Duck!")

def make_it_quack(duck):
    duck.quack()

duck = Duck()
person = Person()

make_it_quack(duck)
make_it_quack(person)

# У Python можна використовувати статичну типізацію для анотації типів і одночасно покладатися на качину типізацію для поліморфізму та гнучкої поведінки об'єктів.
from typing import Protocol

class Speaker(Protocol):
    def speak(self) -> str:
        pass

class Dog:
    def speak(self) -> str:
        return "Woof"

class Cat:
    def speak(self) -> str:
        return "Meow"

class Robot:
    def speak(self) -> str:
        return "Beep boop"

def make_it_speak(speaker: Speaker) -> None:
    print(speaker.speak())

dog = Dog()
cat = Cat()
robot = Robot()

make_it_speak(dog)  # Виведе: Woof
make_it_speak(cat)  # Виведе: Meow
make_it_speak(robot)  # Виведе: Beep boop


"""Розширене ООП в Python"""
# --- UserDict — це клас, що міститься в модулі collections і слугує обгорткою навколо словника. Він дозволяє легше створювати власні класи словників, модифікуючи або додаючи нову поведінку до стандартних методів словника.

#  Simple example
from collections import UserDict

class MyDictionary(UserDict):
    # Приклад додавання нового методу
    def add_key(self, key, value):
        self.data[key] = value

# Створення екземпляра власного класу
my_dict = MyDictionary({'a': 1, 'b': 2})
my_dict.add_key('c', 3)
print(my_dict) # {'a': 1, 'b': 2, 'c': 3}


# Example - more complicated
from collections import UserDict

contacts = [
    {
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Chaim Lewis",
        "email": "dui.in@egetlacus.ca",
        "phone": "(294) 840-6685",
        "favorite": False,
    },
    {
        "name": "Kennedy Lane",
        "email": "mattis.Cras@nonenimMauris.net",
        "phone": "(542) 451-7038",
        "favorite": True,
    }
]

class Customer(UserDict):
    def phone_info(self):
        return f"{self.get('name')}: {self.get('phone')}"

    def email_info(self):
        return f"{self.get('name')}: {self.get('email')}"

if __name__ == "__main__":
    customers = [Customer(el) for el in contacts]

    print("---------------------------")

    for customer in customers:
        print(customer.phone_info())

    print("---------------------------")

    for customer in customers:
        print(customer.email_info())


# --- UserList - це клас, який дозволяє створювати власні версії списків з додатковими функціями. Ви можете додавати нові методи або змінювати ті, що вже існують, щоб вони працювали по-іншому. Це корисно, коли вам потрібен список, який робить щось спеціальне, чого не робить звичайний список Python.

# Simple example
from collections import UserList

class MyList(UserList):
    # Додавання спеціалізованої поведінки. Наприклад, метод для додавання елемента, якщо він ще не існує
    def add_if_not_exists(self, item):
        if item not in self.data:
            self.data.append(item)

# Створення екземпляру MyList
my_list = MyList([1, 2, 3])
print("Оригінальний список:", my_list)

# Додавання елементу, якщо він не існує
my_list.add_if_not_exists(3)  # Не додасться, бо вже існує
my_list.add_if_not_exists(4)  # Додасться, бо ще не існує
print("Оновлений список:", my_list)

# Example - more complicated
from collections import UserList

class CountableList(UserList):
    def sum(self):
        return sum(map(lambda x: int(x), self.data))

countable = CountableList([1, '2', 3, '4'])
countable.append('5')
print(countable.sum()) # 15

# --- UserString - дозволяє створювати класи, які наслідують поведінку звичайного рядка, з можливістю додавання нових методів або зміни стандартної поведінки рядків. Це корисно, коли вам потрібно працювати з рядками спеціалізованим чином, який не підтримується стандартними рядками Python.

# Simple example
from collections import UserString

# Створення класу, який розширює UserString
class MyString(UserString):
    # Додавання методу, який перевіряє, чи рядок є паліндромом
    def is_palindrome(self):
        return self.data == self.data[::-1]

# Створення екземпляру MyString
my_string = MyString("radar")
print("Рядок:", my_string)
print("Чи є паліндромом?", my_string.is_palindrome())

# Створення іншого екземпляру MyString
another_string = MyString("hello")
print("Рядок:", another_string)
print("Чи є паліндромом?", another_string.is_palindrome())

# Example one more
from collections import UserString

class TruncatedString(UserString):
    MAX_LEN = 7

    def truncate(self):
        self.data = self.data[:self.MAX_LEN]

ts = TruncatedString('hello world!')
ts.truncate()
print(ts) # hello w




# --- Класи даних в Python - dataclass
# Базовий приклад синтаксису @dataclass виглядає наступним чином:
# from dataclasses import dataclass

# @dataclass
# class ExampleClass:
#     attribute1: type
#     attribute2: type = default_value

# Example with old definition
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

# Example with @dataclass
from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int = 18 # 18 - default value

# Example with @dataclass and Rectangle class
from dataclasses import dataclass

@dataclass
class Rectangle:
    width: int
    height: int

    def area(self) -> int:
        return self.width * self.height

rect1 = Rectangle(10, 5)
rect2 = Rectangle(7, 3)
rect3 = Rectangle(8, 6)

print(f"Площа прямокутника 1: {rect1.area()}")
print(f"Площа прямокутника 2: {rect2.area()}")
print(f"Площа прямокутника 3: {rect3.area()}")


# --- Перелічуваний тип даних - Enumeration / Enum
# Це спосіб визначення набору іменованих констант у мовах програмування, що дозволяє використовувати більш зрозумілі імена для цих констант замість простих числових значень. Enum визначає символічні імена для набору пов'язаних значень, полегшуючи читання та розуміння коду.

# Simple example
from enum import Enum

class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

today = Day.MONDAY
print(today)  # Виведе: Day.MONDAY

if today == Day.MONDAY:
    print("Сьогодні понеділок.")
else:
    print("Сьогодні не понеділок.")

print(today.name)  
print(today.value)  

day_from_value = Day(2)
print(day_from_value.name)  # Виведе: Day.TUESDAY

# More complicated exmaple
from enum import Enum, auto
from dataclasses import dataclass


class OrderStatus(Enum):
    NEW = auto()
    PROCESSING = auto()
    SHIPPED = auto()
    DELIVERED = auto()

@dataclass
class Order:
    def __init__(self, name: str, status: OrderStatus):
        self.name = name
        self.status = status

    def update_status(self, new_status: OrderStatus):
        self.status = new_status
        print(f"Замовлення '{self.name}' оновлено до статусу {self.status.name}.")

    def display_status(self):
        print(f"Статус замовлення '{self.name}': {self.status.name}.")

order1 = Order("Ноутбук", OrderStatus.NEW)
order2 = Order("Книга", OrderStatus.NEW)

order1.display_status()
order2.display_status()

order1.update_status(OrderStatus.PROCESSING)
order2.update_status(OrderStatus.SHIPPED)

order1.display_status()
order2.display_status()


# --- Асоціація, композиція та агрегація в ООП
# Асоціація пропонує альтернативу наслідуванню, яка може уникнути деяких його недоліків. Асоціація в ООП - це концепція, яка описує відносини між класами через їх об'єкти. У цьому контексті, клас може включати в себе інший клас як одне зі своїх полів, що описується словом "має".

# Асоціація поділяється на два основних типи: композиція та агрегація, кожен з яких має свої особливості та застосування.

# 1) Aгрегація - це тип відношення між об'єктами, яке також представляє відносини "ціле" до "частини", але в цьому випадку "частини" можуть існувати незалежно від "цілого". Це означає, що якщо "ціле" буде знищено, "частини" можуть продовжувати існувати самостійно. Агрегація вказує на більш слабку залежність між об'єктами і часто використовується, коли об'єкти можуть входити до складу різних груп або колекцій. 

class Owner:
    def __init__(self, name: str, phone: str):
        self.name = name
        self.phone = phone

    def info(self):
        return f"{self.name}: {self.phone}"

class Cat:
    def __init__(self, nickname: str, age: int, owner: Owner):
        self.nickname = nickname
        self.age = age
        self.owner = owner

    def get_info(self):
        return f"Cat Name: {self.nickname}, Age: {self.age}"

    def sound(self):
        return "Meow"

owner = Owner("Boris", "+380503002010")
cat = Cat("Simon", 4, owner)
print(cat.owner.info()) # Boris: +380503002010
print(cat.get_info()) # Cat Name: Simon, Age: 4

# ☝ Агрегація дозволяє "частині" існувати незалежно від "цілого". У нашому прикладі, це означає, що господар може існувати окремо від улюбленця. Екземпляр господаря створюється незалежно і лише потім асоціюється з твариною, передаючись в конструктор вихованця як параметр.

# 2) Композиція - це тип відношення між об'єктами, де один об'єкт є частиною іншого. У відношенні композиції "частина" не може існувати без "цілого". Це означає, що якщо "ціле" буде знищено або видалено, то "частина" також буде знищена або видалена.
class Task:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def display_info(self):
        print(f"Задача: {self.name}, Опис: {self.description}")

class Project:
    def __init__(self, name: str):
        self.name = name
        self.tasks: list[Task] = []

    def add_task(self, name: str, description: str):
        self.tasks.append(Task(name, description))

    def remove_task(self, name: str):
        self.tasks = [task for task in self.tasks if task.name != name]

    def display_project_info(self):
        print(f"Проект: {self.name}")
        for task in self.tasks:
            task.display_info()

# Створення проекту
my_project = Project("Веб-розробка")

# Додавання задач
my_project.add_task("Дизайн інтерфейсу", "Створити макет головної сторінки.")
my_project.add_task("Розробка API", "Реалізувати ендпоінти для користувачів.")

# Відображення інформації про проект
my_project.display_project_info()

# Видалення задачі
my_project.remove_task("Розробка API")

# Перевірка видалення задачі
my_project.display_project_info()

# ☝ Композиція є ідеальним вибором для моделювання відносин, де існує сильна залежність між об'єктами, і "частини" не можуть існувати самостійно без "цілого". Вона забезпечує чітку структуру володіння та керування об'єктами, підтримуючи цілісність та консистенцію системи.



# --- Власні винятки
# Base example
class MyCustomError(Exception):
    """Базовий клас для власних винятків"""
    pass


# Example 1
# Визначення власного класу винятку
class AgeVerificationError(Exception):
    def __init__(self, message="Вік не задовольняє мінімальній вимозі"):
        self.message = message
        super().__init__(self.message)

# Функція для перевірки віку
def verify_age(age: int):
    if age < 18:
        raise AgeVerificationError("Вік особи менший за 18 років")

if __name__ == "__main__":
    # Обробка винятку
    try:
        verify_age(16)  # Змініть вік для різних результатів
    except AgeVerificationError as e:
        print(f"Виняток: {e}")
    else:
        print("Вік перевірено, особа доросла.")


# Example 2
class NameTooShortError(Exception):
    pass

class NameStartsFromLowError(Exception):
    pass

def enter_name():
    name = input("Enter name: ")
    if len(name) < 3:
        raise NameTooShortError("Name is too short, need more than 2 symbols")
    if not name[0].isupper():
        raise NameStartsFromLowError("Name should start from capital letter")
    return name

if __name__ == "__main__":
    try:
        name = enter_name()
        print(f"Hello, {name}")
    except (NameTooShortError, NameStartsFromLowError) as e:
        print(e)
