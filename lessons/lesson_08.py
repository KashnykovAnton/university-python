"""Елементи функціонального програмування"""
# Перше, це присвоїмо функцію змінній.
def my_function():
    print("Hello, world!")

f = my_function
f()

# --- Функції можуть бути аргументами інших функцій. 
from typing import Callable

def add(a: int, b: int) -> int:
    return a + b

def multiply(a: int, b: int) -> int:
    return a * b

def apply_operation(a: int, b: int, operation: Callable[[int, int], int]) -> int:
    return operation(a, b)

# Використання
result_add = apply_operation(5, 3, add)
result_multiply = apply_operation(5, 3, multiply)

print(result_add, result_multiply)

# --- Функції як об'єкт першого класу можуть повертати інші функції.
from typing import Callable

def power(exponent: int) -> Callable[[int], int]:
    def inner(base: int) -> int:
        return base ** exponent
    return inner

# Використання
square = power(2)
cube = power(3)

print(square(4)) 
print(cube(4))

# --- Зберігання функцій у структурах даних
from typing import Callable, Dict

# Визначення функцій
def add(a: int, b: int) -> int:
    return a + b

def multiply(a: int, b: int) -> int:
    return a * b

def power(exponent: int) -> Callable[[int], int]:
    def inner(base: int) -> int:
        return base ** exponent
    return inner

# Використання power для створення функцій square та cube
square = power(2)
cube = power(3)

# Словник операцій
operations: Dict[str, Callable] = {
    'add': add,
    'multiply': multiply,
    'square': square,
    'cube': cube
}

# Використання операцій
result_add = operations['add'](10, 20)  # 30
result_square = operations['square'](5)  # 25

print(result_add)  
print(result_square)  


"""Замикання та каррування"""
# --- Closure - це функція, яка зберігає посилання на змінні з області видимості, в якій вона була створена.
# Example 1 - Simple closure
def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function

# Створення замикання
my_func = outer_function("Hello, world!")
my_func()

# Example 2
from typing import Callable

def counter() -> Callable[[], int]:
    count = 0

    def increment() -> int:
        # використовуємо nonlocal, щоб змінити змінну в замиканні
        nonlocal count  
        count += 1
        return count

    return increment

# Створення лічильника
count_calls = counter()

# Виклики лічильника
print(count_calls())  # Виведе 1
print(count_calls())  # Виведе 2
print(count_calls())  # Виведе 3

# --- Currying - це процес перетворення функції з декількома аргументами на послідовність функцій з одним аргументом.
# -- Example 1 - without currying
def add(a, b):
    return a + b

# -- Example 2 - with currying
def add(a):
    def add_b(b):
        return a + b
    return add_b

# Використання:
add_5 = add(5)
result = add_5(10)
print(result)

# -- Example 3 - withou currying - more complicated function
def apply_discount(price: float, discount_percentage: int) -> float:
    return price * (1 - discount_percentage / 100)

# Використання
discounted_price = apply_discount(500, 10)  # Знижка 10% на ціну 500
print(discounted_price)

discounted_price = apply_discount(500, 20)  # Знижка 20% на ціну 500
print(discounted_price)

# -- Example 4 - with currying - more complicated function
from typing import Callable

def discount(discount_percentage: int) -> Callable[[float], float]:
    def apply_discount(price: float) -> float:
        return price * (1 - discount_percentage / 100)
    return apply_discount

# Каррінг в дії
ten_percent_discount = discount(10)
twenty_percent_discount = discount(20)

# Застосування знижок
discounted_price = ten_percent_discount(500)  # 450.0
print(discounted_price)

discounted_price = twenty_percent_discount(500)  # 400.0
print(discounted_price)

# -- OR, with dictionary:

from typing import Callable, Dict

def discount(discount_percentage: int) -> Callable[[float], float]:
    def apply_discount(price: float) -> float:
        return price * (1 - discount_percentage / 100)
    return apply_discount

# Створення словника з функціями знижок
discount_functions: Dict[str, Callable] = {
    "10%": discount(10),
    "20%": discount(20),
    "30%": discount(30)
}

# Використання функції зі словника
price = 500
discount_type = "20%"

discounted_price = discount_functions[discount_type](price)
print(f"Ціна зі знижкою {discount_type}: {discounted_price}")


"""Декоратори"""
# Example - without decorator
def complicated(x: int, y: int) -> int:
    return x + y

def logger(func):
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result

    return inner

complicated = logger(complicated)
print(complicated(2, 3))

# Example - with decorator
def logger(func):
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result

    return inner

@logger
def complicated(x: int, y: int) -> int:
    return x + y

print(complicated(2, 3))

"""Дуже важливо при створенні декораторів використовувати модуль functools, це необхідно для збереження метаданих оригінальної функції, яку ми декоруємо. Функція functools.wraps допомагає в цьому, зберігаючи інформацію про оригінальну функцію, як-от ім'я функції та документацію."""

from functools import wraps

def logger(func):
    @wraps(func)
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result

    return inner

@logger
def complicated(x: int, y: int) -> int:
    return x + y

print(complicated(2, 3))
print(complicated.__name__)


"""Comprehensions"""
"""Comprehensions в Python - це спосіб компактного створення колекцій на основі існуючих колекцій. Python підтримує кілька видів comprehensions: 
- для списків (list comprehensions), 
- множин (set comprehensions) та 
- словників (dictionary comprehensions). 
Вони дозволяють писати вирази для створення нових колекцій з меншою кількістю коду, ніж при використанні циклів."""
# Example with comprehensions
sq = []
for i in range(1, 6):
    sq.append(i**2)

print(sq) # [1, 4, 9, 16, 25]

# --- List comprehensions використовуються для створення нових списків та мають наступний синтаксис:
[new_item for item in iterable if condition]

# Example 1
sq = [x**2 for x in range(1, 6)] # [1, 4, 9, 16, 25]
print(sq)

# Example 2
even_squares = [x**2 for x in range(1, 10) if x % 2 == 0]
print(even_squares) # [4, 16, 36, 64]

# Example 3
words = ["apple", "banana", "cherry"]
upper_words = [word.upper() for word in words]
print(upper_words) # ['APPLE', 'BANANA', 'CHERRY']


# --- Set comprehensions використовуються аналогічно list comprehensions, але для створення множин.
{new_item for item in iterable if condition}

# Example 1
numbers = [1, 4, 1, 3, 2, 5, 2, 6]
sq = {i ** 2 for i in numbers}
print(sq) # {1, 4, 9, 16, 25, 36}

# Example 2
odd_squares = {x**2 for x in range(1, 10) if x % 2 != 0}
print(odd_squares) # {1, 9, 25, 49, 81}

# Example 3
words = ["apple", "banana", "cherry"]
upper_words = {word.upper() for word in words}
print(upper_words) # {'BANANA', 'CHERRY', 'APPLE'}

# --- Dictionary comprehensions використовуються для створення нових словників. 
# Для словників синтаксис comprehension трохи відрізняється, оскільки потрібно явно вказати ключ та значення
{key: value for item in iterable if condition}

# Example 1
sq = {x: x**2 for x in range(1, 10)}
print(sq) # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# Example 2
sq_dict = {x: x**2 for x in range(1, 10) if x > 5}
print(sq_dict) # {6: 36, 7: 49, 8: 64, 9: 81}

# Example 3
words = ["apple", "banana", "cherry"]
word_lengths = {word: len(word) for word in words}
print(word_lengths) # {'apple': 5, 'banana': 6, 'cherry': 6}


"""Лямбда-функції"""
"""Буває, що нам потрібна функція, суть якої можна викликати, передавши їй аргументи, але сама функція дуже проста і її всю можна описати одним виразом. У таких ситуаціях немає особливого сенсу створювати функцію, використовуючи стандартний синтаксис і захаращувати простір імен.
Спеціально для таких випадків у Python є лямбда-функції, відомі також як анонімні функції, які є важливою частиною Python і використовуються для створення маленьких, однорядкових функцій."""

lambda arguments: expression
"""Тут lambda — це ключове слово, що вказує на початок лямбда-функції. arguments — це список аргументів, які приймає функція, а expression — це вираз, який буде виконано та його результат повернуто."""

# Example 1 - not good pattern
add = lambda x, y: x + y
print(add(5, 3))  # Виведе 8

# Example 2 - good pattern
print((lambda x, y: x + y)(5, 3))  # Виведе 8

# Лямбда-функції часто використовуються як аргументи для функцій вищого порядку, таких як map(), filter() або sorted(). 
# Наприклад зворотне сортування списку для sorted():
nums = [1, 2, 3, 4, 5]
nums_sorted = sorted(nums, key=lambda x: -x)
print(nums_sorted) # [5, 4, 3, 2, 1]


# --- Функція map() використовується для виконання функції на кожному елементі ітерабельного об'єкта.
"""Синтаксис:
map(function, iterable, ...)
    function - функція, яку треба застосувати до кожного елемента в iterable.
    iterable - об'єкт ітерації (список, кортеж тощо), елементи якого будуть оброблятися function."""

# Example 1
numbers = [1, 2, 3, 4, 5]

for i in map(lambda x: x ** 2, numbers):
    print(i) # 1 4 9 16 25

#  OR for list:
numbers = [1, 2, 3, 4, 5]

squared_nums = list(map(lambda x: x ** 2, numbers))
print(squared_nums) # [1, 4, 9, 16, 25]

# OR for several lists:
nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
sum_nums = map(lambda x, y: x + y, nums1, nums2)

print(list(sum_nums)) # [5, 7, 9]

# --- Функція filter() використовується для відфільтрування елементів ітерабельного об'єкта на основі умови, вказаної в функції.
"""Синтаксис filter():
filter(function, iterable)
    function - функція, яка визначає, чи слід включати елемент у результат. Ця функція повинна приймати один аргумент і повертати булеве значення True або False.
    iterable - об'єкт ітерації (наприклад, список, кортеж), елементи якого будуть перевірятися функцією function."""

# Example 1
even_nums = filter(lambda x: x % 2 == 0, range(1, 11))

print(list(even_nums)) # [2, 4, 6, 8, 10]

# Example 2 - witout lambda
def is_positive(x):
    return x > 0

nums = [-2, -1, 0, 1, 2]
positive_nums = filter(is_positive, nums)

print(list(positive_nums)) # [1, 2]

# Example 3
some_str = 'Видавництво А-БА-БА-ГА-ЛА-МА-ГА'

new_str = ''.join(list(filter(lambda x: x.islower(), some_str)))
print(new_str) # вдвнцво-б-б-г-м-г

# --- Функція any() повертає True, якщо хоча б один елемент ітерабельного об'єкта є True, і False, якщо всі елементи є False.
# Example 1
nums = [0, False, 5, 0]
result = any(nums)  
print(result)

# Example 2
nums = [1, 3, 5, 7, 9]
result = any(x % 2 == 0 for x in nums)  
print(result)

# --- Функція all() повертає True, якщо всі елементи ітерабельного об'єкта є True, і False, якщо хоча б один елемент є False.
# Example 1
nums = [1, 2, 3, 4]
result = all(nums)  
print(result)

# Example 2
nums = [1, 2, 3, 4]
is_all_even = all(x % 2 == 0 for x in nums) 
print(is_all_even)

# Example 3
words = ["Hello", "World", "Python"]
is_all_title_case = all(word.istitle() for word in words)
print(is_all_title_case)


