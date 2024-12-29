"""Використання спеціальних методів для керування об'єктами"""
"""Магічні методи"""
# Важливо пам'ятати, що імена всіх магічних методів в Python дотримуються строгої номенклатури: вони складаються з літер нижнього регістру та символів підкреслення, починаючись і закінчуючись подвійним символом підкреслення (__). Наприклад, __init__.

# --- __init__ ---
# Example with custom method in __init__:   
class Human:
    def __init__(self, name: str, age: int = 0):
        self.name = name
        self.age = age
        # Виклик методу під час ініціалізації
        self.is_adult = self.__check_adulthood()  
        
        # Приклад логування
        print(f"Створено Human: {self.name}, Вік: {self.age}, Дорослий: {self.is_adult}")

    def say_hello(self) -> str:
        return f'Hello! I am {self.name}'

    def __check_adulthood(self) -> bool:
        return self.age >= 18

bill = Human('Bill')
print(bill.say_hello())
print(f"Вік: {bill.age}, Дорослий: {bill.is_adult}")

jill = Human('Jill', 20)
print(jill.say_hello())
print(f"Вік: {jill.age}, Дорослий: {jill.is_adult}")

# Методи __str__ та __repr__  - використовуються для представлення об'єктів у вигляді рядків
print("-----------------------------------")
# Метод __repr__ призначений для створення офіційного рядкового представлення об'єкта. 
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

point = Point(2, 3)
print(repr(point))  # Виводить: Point(x=2, y=3)

# Метод __str__ призначений для повернення рядкового представлення об'єкта, яке має бути читабельним і зрозумілим для людини. 
class Human:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Human named {self.name} who is {self.age} years old"
    
    def __repr__(self):
        return f"Human({self.name}, {self.age})"

human = Human("Alice", 30)
print(human)

# !!!! Main difference between __str__ and __repr__: 
# if in console you write print(object) - it will call __str__ method # print(human)
# if you write object - it will call __repr__ method # human


# Методи __getitem__ та __setitem__ 
# Методи __getitem__ та __setitem__ в Python використовуються для налаштування доступу до елементів об'єкта за допомогою індексації або ключів, подібно до роботи зі списками чи словниками.

# Метод __getitem__ визначає, як об'єкт класу повинен вести себе при доступі до його елементів за допомогою індексу або ключа. Він приймає ключ або індекс як аргумент і повинен повертати значення, асоційоване з цим ключем або індексом.


# Метод __setitem__ визначає, як об'єкт повинен поводити себе при присвоєнні значення елементу за певним індексом або ключем. Він приймає два аргументи: ключ (або індекс) та значення, яке потрібно асоціювати з цим ключем.

class SimpleDict:
    def __init__(self):
        self.__data = {}

    def __getitem__(self, key):
        return self.__data.get(key, "Key not found")

    def __setitem__(self, key, value):
        self.__data[key] = value

# Використання класу
simple_dict = SimpleDict()
simple_dict['name'] = 'Boris'
print(simple_dict['name'])  
print(simple_dict['age'])  

#  Example with temperature
class BoundedList:
    def __init__(self, min_value: int, max_value: int):
        self.min_value = min_value
        self.max_value = max_value
        self.__data = []

    def __getitem__(self, index: int):
        return self.__data[index]

    def __setitem__(self, index: int, value: int):
        if not (self.min_value <= value <= self.max_value):
            raise ValueError(f"Value {value} must be between {self.min_value} and {self.max_value}")
        if index >= len(self.__data):
            # Додати новий елемент, якщо індекс виходить за межі
            self.__data.append(value)
        else:
            # Замінити існуючий елемент
            self.__data[index] = value

    def __repr__(self):
        return f"BoundedList({self.max_value}, {self.min_value})"

    def __str__(self):
        return str(self.__data)

if __name__ == '__main__':
    temperatures = BoundedList(18, 26)

    for i, el in enumerate([20, 22, 25, 27]):
        try:
            temperatures[i] = el
        except ValueError as e:
            print(e)

    print(temperatures)

    # --- Перевизначення математичних операторів ---
    #     __add__(self, other) для оператора +
    # __sub__(self, other) для оператора -
    # __mul__(self, other) для оператора *
    # __truediv__(self, other) для оператора /
    # __floordiv__(self, other) для оператора цілочисельного ділення //
    # __mod__(self, other) для оператора залишку від ділення %
    # __pow__(self, other) для оператора * піднесення до степеня

#  Example
from collections import UserDict

class MyDict(UserDict):
    def __add__(self, other):
        temp_dict = self.data.copy()
        temp_dict.update(other)
        return MyDict(temp_dict)

    def __sub__(self, other):
        temp_dict = self.data.copy()
        for key in other:
            if key in temp_dict:
                temp_dict.pop(key)
        return MyDict(temp_dict)

if __name__ == '__main__':
    d1 = MyDict({1: 'a', 2: 'b'})
    d2 = MyDict({3: 'c', 4: 'd'})

    d3 = d1 + d2
    print(d3)

    d4 = d3 - d2
    print(d4)

    # Example 2
    class ComplexNumber:
        def __init__(self, real, imag):
            self.real = real
            self.imag = imag

        def __add__(self, other):
            return ComplexNumber(self.real + other.real, self.imag + other.imag)

        def __sub__(self, other):
            return ComplexNumber(self.real - other.real, self.imag - other.imag)

        def __mul__(self, other):
            real_part = self.real * other.real - self.imag * other.imag
            imag_part = self.real * other.imag + self.imag * other.real
            return ComplexNumber(real_part, imag_part)

        def __str__(self):
            return f"{self.real} + {self.imag}i"

if __name__ == "__main__":
    num1 = ComplexNumber(1, 2)
    num2 = ComplexNumber(3, 4)
    print(f"Сума: {num1 + num2}")
    print(f"Різниця: {num1 - num2}")
    print(f"Добуток: {num1 * num2}")


# --- Перевизначення операцій порівняння ---
    # __eq__(self, other) — визначає поведінку під час перевірки на відповідність (==).
    # __ne__(self, other) — визначає поведінку під час перевірки на невідповідність. !=.
    # __lt__(self, other) — визначає поведінку під час перевірки на менше <.
    # __gt__(self, other) — визначає поведінку під час перевірки на більше >.
    # __le__(self, other) — визначає поведінку під час перевірки на менше-дорівнює <=.
    # __ge__(self, other) — визначає поведінку під час перевірки на більше-дорівнює >=.


# Example
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() == other.area()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() < other.area()

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __gt__(self, other):
        if not isinstance(other, Rectangle):
            return NotImplemented
        return self.area() > other.area()

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)

if __name__ == "__main__":
    rect1 = Rectangle(5, 10)
    rect2 = Rectangle(3, 20)
    rect3 = Rectangle(5, 10)
    print(f"Площа прямокутників: {rect1.area()}, {rect2.area()}, {rect3.area()}")
    print(rect1 == rect3)  # True: площі рівні
    print(rect1 != rect2)  # True: площі не рівні
    print(rect1 < rect2)  # True: площа rect1  менша, ніж у rect2
    print(rect1 <= rect3)  # True: площі рівні, тому rect1 <= rect3
    print(rect1 > rect2)  # False: площа rect1 менша, ніж у rect2
    print(rect1 >= rect3)  # True: площі рівні, тому rect1 >= rect3


#  Example 2
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x < other.x and self.y < other.y

    def __gt__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x > other.x and self.y > other.y

    def __le__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x <= other.x and self.y <= other.y

    def __ge__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return self.x >= other.x and self.y >= other.y

if __name__ == "__main__":
    print(Point(0, 0) == Point(0, 0))  # True
    print(Point(0, 0) != Point(0, 0))  # False
    print(Point(0, 0) < Point(1, 0))  # False
    print(Point(0, 0) > Point(0, 1))  # False
    print(Point(0, 2) >= Point(0, 1))  # True
    print(Point(0, 0) <= Point(0, 0))  # True

"""Управління атрибутами та методами в класах Гетери і сетери"""
class Person:
    def __init__(self, age):
        self.__age = age  # Пряме присвоєння значення атрибуту в конструкторі

    @property
    def age(self):
        return self.__age  # Геттер повертає значення приватного поля

    @age.setter
    def age(self, value):
        if value < 0:
            # Валідація вхідного значення
            raise ValueError("Вік не може бути від'ємним")  
        # Присвоєння валідного значення приватному полю
        self.__age = value  

if __name__ == "__main__":
    person = Person(10)
    print(person.age)
    # person.age = -5
    person.age = 5

# Example 2 - good pattern
class Person:
    def __init__(self, age):
        # Спочатку встановлюємо __age як None
        self.__age = None
        # Використовуємо сеттер для встановлення віку, що дозволяє валідацію вхідного значення
        self.age = age

    @property
    def age(self):
        # Геттер повертає значення приватного поля
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            # Валідація вхідного значення
            raise ValueError("Вік не може бути від'ємним")
        # Присвоєння валідного значення приватному полю
        self.__age = value

if __name__ == "__main__":
    person = Person(10)
    # person = Person(-10)
    print(person.age)

#  Example with incupsulation
class Person:
    def __init__(self, name: str, age: int, is_active: bool, is_admin: bool):
        self.name = name
        self.age = age
        self._is_active = None
        self.__is_admin = None
        self._is_active = is_active
        self.__is_admin = is_admin

    @property
    def is_active(self):
        return self._is_active

    @is_active.setter
    def is_active(self, value: bool):
        # Тут можна додати будь-яку логіку перевірки або обробки
        self._is_active = value

    @property
    def is_admin(self):
        return self.__is_admin

    @is_admin.setter
    def is_admin(self, value: bool):
        # Тут можна додати будь-яку логіку перевірки або обробки
        self.__is_admin = value

    def greeting(self):
        return f"Hi {self.name}"

if __name__ == "__main__":
    p = Person("Boris", 34, True, False)
    print(p.is_admin)  # Використовуємо геттер
    p.is_admin = True  # Використовуємо сеттер
    print(p.is_admin)

"""Статичні та класові методи"""
# Статичні методи використовують декоратор @staticmethod і є методами, які не мають доступу до екземпляру класу тобто змінної self, з якого вони були викликані. 

class Geometry:
    PI = 3.14159

    @staticmethod
    def area_of_circle(radius):
        return Geometry.PI * radius ** 2

# Example 2
class Animal:
    def __init__(self, nickname, age):
        self.nickname = nickname
        self.age = age

    @staticmethod
    def has_owner():
        return False


dog = Animal("Rex", 3)
print(dog.has_owner())  # False
print(Animal.has_owner())  # False - можна викликати без створення екземпляра класу

# Example 3
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def add(self):
        return self.a + self.b

    @staticmethod
    def multiply(a, b):
        return a * b

calculate = Calculator(5, 3)
print(calculate.add())  # 8

print(Calculator.multiply(5, 3))  # 15 - можна викликати без створення екземпляра класу
print(calculate.multiply(5, 3))  # 15 - можна викликати через екземпляр класу


# Класові методи використовують декоратор @classmethod і, на відміну від статичних методів, мають доступ до самого класу через параметр cls, який автоматично передається Python.

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    @classmethod
    def from_string(cls, employee_info):
        name, position = employee_info.split(',')
        return cls(name, position)


"""Функтори, Ітератори та Управління контекстом в Python"""

"""Функтори в Python — це об'єкти класів, які можуть бути викликані як функції. Це досягається за допомогою реалізації спеціального магічного методу __call__ для класу. Коли ви додаєте метод __call__ до класу, екземпляри цього класу можуть бути викликані як звичайні функції."""
print("-----------------------------------")
class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, other):
        return self.factor * other

# Створення екземпляра функтора
double = Multiplier(2)
triple = Multiplier(3)

# Виклик функтора
print(double(5))  # Виведе: 10
print(triple(3))  # Виведе: 9

# Розглянемо функтор зі станом
class Counter:
    def __init__(self):
        self.count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1

counter = Counter()
counter()
counter()
print(f"Викликано {counter.count} разів")


# Example 2
class SmartCalculator:
    def __init__(self, operation='add'):
        self.operation = operation

    def __call__(self, a, b):
        if self.operation == 'add':
            return a + b
        elif self.operation == 'subtract':
            return a - b
        else:
            raise ValueError("Невідома операція")

add = SmartCalculator('add')
print(add(5, 3))  # 8

subtract = SmartCalculator('subtract')
print(subtract(10, 7))  # 3


"""Ітератор в Python — це об'єкт, який дозволяє нам послідовно перебирати елементи будь-якого об'єкта ітерації (наприклад, списку, кортежу, словника) без потреби використання індексів. Він реалізує методи __iter__() та __next__() та дозволяє перебирати елементи послідовності, не завантажуючи всю послідовність у пам'ять."""
print("-----------------------------------")

class CountDown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current == 0:
            raise StopIteration
        self.current -= 1
        return self.current

if __name__ == '__main__':
    counter = CountDown(5)
    for count in counter:
        print(count)


"""Генератор - це спрощений спосіб створення ітераторів. Функція стає генератором, коли містить вираз yield. Генератор автоматично реалізує методи __iter__() та __next__()."""
def count_down(start):
    current = start
    current -= 1
    while current >= 0:
        yield current
        current -= 1

# Використання генератора
for count in count_down(5):
    print(count)

# Example 2
from random import randint

class RandIterator:
    def __init__(self, start, end, quantity):
        self.start = start
        self.end = end
        self.quantity = quantity
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count > self.quantity:
            raise StopIteration
        else:
            return randint(self.start, self.end)

if __name__ == '__main__':
    my_random_list = RandIterator(1, 20, 5)

    for rn in my_random_list:
        print(rn, end=' ')

# OR solution with yeild
from random import randint

def rand_generator(start, end, quantity):
    count = 0
    while count < quantity:
        yield randint(start, end)
        count += 1

if __name__ == '__main__':
    for rn in rand_generator(1, 20, 5):
        print(rn, end=' ')

"""Передача значень у генератор"""
"""Оператор yield має більш рідкісне застосування, він може повертати значення так само, як і виклик функції. Це дозволяє передавати значення в генератор за допомогою виклику методу send."""

def my_generator():
    received = yield "Ready"
    yield f"Received: {received}"

gen = my_generator()
print(next(gen))  
print(gen.send("Hello"))  

# Коли генератору більше не потрібно виробляти значення, його можна закрити за допомогою методу close(). При цьому в генераторі викликається виключення GeneratorExit, яке можна перехопити для виконання якихось дій перед закриттям генератора.

def my_generator():
    try:
        yield "Working"
    except GeneratorExit:
        print("Generator is being closed")

gen = my_generator()
print(next(gen))  # Отримуємо "Working"
gen.close()  # Викликаємо закриття генератора

# Example with square numbers
def square_numbers():
    try:
        while True:  # Безкінечний цикл для прийому чисел
            number = yield  # Отримання числа через send()
            square = number ** 2  # Піднесення до квадрата
            yield square  # Повернення результату
    except GeneratorExit:
        print("Generator closed")

# Створення і старт генератора
gen = square_numbers()

# Ініціалізація генератора
next(gen)  # Або gen.send(None), щоб стартувати

# Відправлення числа в генератор і отримання результату
result = gen.send(10)  # Повинно повернути 100
print(f"Square of 10: {result}")

# Перехід до наступного очікування
next(gen)

# Відправлення іншого числа
result = gen.send(5)  # Повинно повернути 25
print(f"Square of 5: {result}")

# Закриття генератора
gen.close()

# Example with filter lines:
def filter_lines(keyword):
    print(f"Looking for {keyword}")
    try:
        while True:  # Нескінченний цикл, де генератор чекає на вхідні дані
            line = yield  # Отримання рядка через send()
            if keyword in line:  # Перевірка на наявність ключового слова
                yield f"Line accepted: {line}"
            else:
                yield None
    except GeneratorExit:
        print("Generator closed")

if __name__ == "__main__":
    # Створення і старт генератора
    gen = filter_lines("hello")
    next(gen)  # Потрібно для старту генератора
    messages = ["this is a test", "hello world", "another hello world line", "hello again", "goodbye"]
    hello_messages = []
    # Відправлення даних у генератор
    for message in messages:
        result = gen.send(message)  # Відправляємо повідомлення в генератор
        if result:  # Додаємо результат тільки якщо він не None
            hello_messages.append(result)
        next(gen)  # Продовжуємо до наступного yield: інструкція line = yield

    # Закриття генератора
    gen.close()
    print(hello_messages)


"""Створення власних менеджерів контексту"""
print("-----------------------------------")

# Example 1
from contextlib import contextmanager

@contextmanager
def my_context_manager():
    # Ініціалізація ресурсу
    print("Enter the block")
    try:
        yield  # Місце виконання блоку `with`
    except Exception as e:
        # Обробка виключень
        print(f"Error detected: {e}")
        # Можна ре-підняти виключення або вирішити його тут
        raise
    finally:
        # Звільнення ресурсу
        print("Exit the block")

# Використання
with my_context_manager():
    print("Inside the block")
    raise Exception("Something went wrong")


# Example 2
class FileManager:
    def __init__(self, filename, mode='w', encoding='utf-8'):
        self.file = None
        self.opened = False
        self.filename = filename
        self.mode = mode
        self.encoding = encoding

    def __enter__(self):
        self.file = open(self.filename, self.mode, encoding=self.encoding)
        self.opened = True
        print("Відкриваємо файл", self.filename)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Завершення блоку with")
        if self.opened:
            print("Закриваємо файл", self.filename)
            self.file.close()
        self.opened = False


if __name__ == '__main__':
    with FileManager('new_file.txt') as f:
        f.write('Hello world!\n')
        f.write('The end\n')


class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y

    def __call__(self, value=None):
        if value:
            self.coordinates.x = self.coordinates.x * value
            self.coordinates.y = self.coordinates.y * value
        return self.coordinates.x, self.coordinates.y

    def __add__(self, vector):
        x = self.coordinates.x + vector.coordinates.x
        y = self.coordinates.y + vector.coordinates.y
        return Vector(Point(x, y))

    def __sub__(self, vector):
        x = self.coordinates.x - vector.coordinates.x
        y = self.coordinates.y - vector.coordinates.y
        return Vector(Point(x, y))

    def __mul__(self, vector):
        return (
                self.coordinates.x * vector.coordinates.x
                + self.coordinates.y * vector.coordinates.y
        )

    def len(self):
        return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5

    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"
    
    def __eq__(self, vector):
        return len(self) == len(vector)
        
    def __ne__(self, vector):
        return self.x != vector.x or self.y != vector.y

    def __lt__(self, vector):
        return self.x < vector.x and self.y < vector.y

    def __gt__(self, vector):
        return self.x > vector.x and self.y > vector.y

    def __le__(self, vector):
        return self.x <= vector.x and self.y <= vector.y

    def __ge__(self, vector):
        return self.x >= vector.x and self.y >= vector.y