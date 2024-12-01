"""Умовні оператори, цикли"""


# --- Умовний оператор if ---
"""if <умова>:
    <тіло if-блоку>
else:
    <тіло else-блоку>
"""

# ----- Приклад 1
# num = 15  # приклад значення для num

# if num > 10:
#     print("num більше за 10")
# else:
#     print("num не більше за 10")

# ----- Приклад 2
# x = int(input('Введіть число: '))

# if x % 2 == 0:
#     print("Число є парним.")
# else:
#     print("Число є непарним.")


# --- Oператор контролю виконання if ... elif ... else ---
"""if <умова 1>:
    <тіло if-блоку>
elif <умова 2>:
    <тіло elif-блоку>
else:
    <тіло else-блоку>
"""

# ----- Приклад 3
# a = input('Введіть число: ')
# a = int(a)
# if a > 0:
#     print('Число додатне')
# elif a < 0:
#     print("Число від'ємне")
# else:
#     print('Це число - нуль')

# ----- Приклад 4
# a = input('Введіть число')
# a = int(a)

# if a == 1:
#     print('Число дорівнює 1')
# elif a > 0:
#     print('Число додатне')
# else:
#     print("a <= 0")


"""Логічні вирази"""
# Правило перше - число 0 приводиться до False (ціле, дійсне або комплексне).
# money = 0
# if money:
#     print(f"You have {money} on your bank account")
# else:
#     print("You have no money and no debts")

# Правило друге - значення None приводиться до False.
# result = None
# if result:
#     print(result)
# else:
#     print("Result is None, do something")

# Правило третє - порожній рядок, список, кортеж, множина, словник приводяться до False.
# user_name = input("Enter your name: ")

# if user_name:
#     print(f"Hello {user_name}")
# else:
#     print("Hi Anonym!")

# Правило останнє - все інше приводиться до True

"""Оператор is"""
# a = [1, 2, 3]
# b = a
# c = [1, 2, 3]

# print(a is b)  # True
# print(a is c)  # False

# # Однак основне його застосування - це перевірка, чи змінна є None.
# if my_var is None:
#     # Робимо щось, якщо 'my_var' є 'None'
# # !!! if a is None: - правильна перевірка на None


"""Булева алгебра"""
# name = "Taras"
# age = 22
# has_driver_licence = True

# if name and age >= 18 and has_driver_licence:
#     print(f"User {name} can rent a car")

# ----- Оператор "and"
# a = True and False  # False

# ----- Оператор "or"
# b = True or False  # True

# ----- Оператор "not"
# a = not 2 < 0  # True

# ----- завдання "FizzBuzz”
# Задаємо конкретне число
# num = int(input())
# Перевіряємо кратність
# if num % 3 == 0 and num % 5 == 0:
#     print("FizzBuzz")
# elif num % 3 == 0:
#     print("Fizz")
# elif num % 5 == 0:
#     print("Buzz")
# else:
#     print(num)


"""Тернарні операції"""

#  ----- Приклад 1
# is_nice = True
# state = "nice" if is_nice else "not nice"
# print(state)

# # ----- Приклад з if ... else:
# is_nice = True
# if is_nice:
#     state = "nice"
# else:
#     state = "not nice"

# ----- Приклад 2
# some_data = None
# msg = some_data or "Не було повернено даних"
# print(msg)

# # ----- Приклад з if ... else:
# some_data = None
# if some_data:
#     msg = some_data
# else:
#     msg = "Не було повернено даних"


"""Оператор match"""

# Структура оператора match:
# match змінна:
#     case шаблон1:
#         # виконати код для шаблону 1
#     case шаблон2:
#         # виконати код для шаблону 2
#     case _:
#         # виконати код, якщо не знайдено відповідностей

# ----- Приклад 1
# fruit = "apple"

# match fruit:
#     case "apple":
#         print("This is an apple.")
#     case "banana":
#         print("This is a banana.")
#     case "orange":
#         print("This is an orange.")
#     case _:
#         print("Unknown fruit.")

# ----- Приклад 2
# point = (1, 0)

# match point:
#     case (0, 0):
#         print("Точка в центрі координат")  
#     case (0, y):
#         print(f"Точка лежить на осі Y: y={y}")  
#     case (x, 0):
#         print(f"Точка лежить на осі X: x={x}") 
#     case (x, y):
#         print(f"Точка має координати:  x={x}, y={y}") 
#     case _:
#         print("Це не точка")

# ----- Приклад 3
# pets = ["dog", "fish", "cat"]

# match pets:
#     case ["dog", "cat", _]:
#         # Випадок, коли є і собака, і кіт
#         print("There's a dog and a cat.")
#     case ["dog", _, _]:
#         # Випадок, коли є тільки собака
#         print("There's a dog.")
#     case _:
#         # Випадок для інших комбінацій
#         print("No dogs.")

"""Цикли"""

"""--- Цикл for ---"""
# Цикл for в Python використовується для ітерації по елементах будь-якої послідовності (наприклад, списку, кортежу, рядка) або інших ітерованих об'єктів;
# for element in sequence:
    # виконувати дії з element

# ----- Приклад 1
# fruit = 'apple'
# for char in fruit:
#     print(char)

# ----- Приклад 2
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# for char in alphabet:
#     print(char, end=" ")

# ----- Приклад 3
# odd_numbers = [1, 3, 5, 7, 9]
# for i in odd_numbers:
#     print(i ** 2)

# ----- Приклад 4
# user_input = input("Введіть рядок: ")

# total_chars = len(user_input)  # загальна кількість символів у рядку
# space_count = 0  # кількість пробілів

# for char in user_input:
#     if char == " ":
#         space_count += 1

# print(f"Загальна кількість символів у рядку: {total_chars}")
# print(f"Кількість пробілів у рядку: {space_count}")

# ----- Приклад 5
# for i in range(1, 10):
#     if i % 2 == 0:
#         print(f”{i} є парним числом.“)
#     else:
#         print(f”{i} є непарним числом.“)
#  # range(start, end, step) - створює послідовність чисел від start до end - 1 з кроком step


"""--- Цикл while ---"""
# Цикл while виконує блок коду, поки задана умова є істинною (True). Як тільки умова стає неправдивою (False), цикл закінчується.
# while condition:
    # виконувати дії, поки condition є True

# ----- Приклад 1
# k = 0
# while k < 10:
#     k = k + 1
#     print(k)

"""«Нескінченні цикли» та break"""
# ----- Приклад 1
# a = 0
# while True:
#     print(a)
#     if a >= 20:
#         break
#     a = a + 1

# ----- Приклад 2
# while True:
#     user_input = input("Enter something: ")
#     print(user_input)
#     if user_input == "exit":
#         break

"""Завершення ітерації за допомогою continue"""
# ----- Приклад 1
# a = 0
# while a < 6:
#     a = a + 1
#     if not a % 2:
#         continue
#     print(a)


"""Розширення можливостей циклу for"""
# --- Функція Range ---
"""Функція range важлива для створення послідовностей чисел, які ви можете використовувати у циклах. Вона надзвичайно корисна, коли вам потрібно виконати дію певну кількість разів або ітерувати через послідовність чисел."""
# range(start, stop, step)
""" range(stop): Створює послідовність чисел від 0 до stop - 1.
    range(start, stop): Генерує числа від start до stop - 1.
    range(start, stop, step): Створює числа від start до stop - 1, з кроком step."""

# ----- Приклад 1 (stop)
# for i in range(5):
#     print(i)

# ----- Приклад 2 (start, stop)
# for i in range(2, 10):
#     print(i)

# ----- Приклад 3 (start, stop, step)
# for i in range(0, 10, 2):
#     print(i)

# --- Функція Enumerate ---
"""Коли вам потрібно отримати доступ не тільки до значення з ітерованої колекції, але до її індексу, тут функція enumerate стає незамінним помічником. Ця функція дозволяє вам легко отримувати доступ до індексу кожного елементу під час ітерації."""
# enumerate(iterable, start=0)
""" iterable: послідовність, яку ви хочете перебрати.
    start: індекс, з якого починається нумерація."""

# ----- Приклад 1
# names = ['Alice', 'Bob', 'Charlie', 'Dilan']
# for i, name in enumerate(names):
#     print(f"Index: {i}, Name: {name}")

# ----- Приклад 2
# names = ['Alice', 'Bob', 'Charlie', 'Dilan']
# for i, name in enumerate(names, 3):
#     print(f"Index: {i}, Name: {name}")

# --- Функція Zip ---
"""Функція zip використовується для одночасної ітерації по кількох колекціях. Якщо вам потрібно комбінувати дані з різних джерел або виконувати операції, які залежать від декількох пов'язаних колекцій, zip дозволяє це зробити легко та елегантно."""
# zip(iterable1, iterable2, ...)
""" iterable1, iterable2, ...: колекції, які ви хочете об'єднати."""

# ----- Приклад 1
# names = ['Alice', 'Bob', 'Charlie', 'Dilan']
# ages = [25, 30, 35, 40]
# for name, age in zip(names, ages):
#     print(f"Name: {name}, Age: {age}")

# ----- Приклад 2 (різні довжини списків)
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c', 'd', 'e']

# for number, letter in zip(list1, list2):
#     print(number, letter)

"""Цикли та словники"""
# ----- Приклад 1
# numbers = {
#     1: "one",
#     2: "two",
#     3: "three"
# }

# for key in numbers:
#     print(key)

# # Або .keys() - виводить ключі словника
# for key in numbers.keys():
#     print(key)

# # .values() - виводить значення словника
# for value in numbers.values():
#     print(value)

# # .items() - виводить пари ключ-значення
# for key, value in numbers.items():
#     print(f"Key: {key}, Value: {value}")

"""Механізм обробки винятків (try ... except)"""

# ----- Приклад 1
# val = 'a'
# try:
#     val = int(val)
# except ValueError:
#     print(f"val {val} is not a number")
# else:
#     print(f"val > 0: {val > 0}")
# finally:
#     print("This will be printed anyway")

# ----- Приклад 2
# age = input("How old are you? ")
# try:
#     age = int(age)
#     if age >= 18:
#         print("You are adult.")
#     else:
#         print("You are infant")
# except ValueError:
#     print(f"{age} is not a number")

"""Функції, область видимості змінних (LEGB)"""
# --- Створення та виклик функцій ---
# def say_hello():
# 		# тіло функції
#     print('Привіт, Світ!')

# # Кінець функції say_hello()

# # виклик функції
# say_hello()

# # ще один виклик функції
# say_hello()

# --- Аргументи функції ---
"""Зверніть увагу на термінологію: імена, вказані при оголошенні функції, називаються параметрами, тоді як значення, які ви передаєте у функцію при її виклику, – аргументами."""
# def print_max(a, b):
#     if a > b:
#         print(a, 'максимально')
#     elif a == b:
#         print(a, 'дорівнює', b)
#     else:
#         print(b, 'максимально')

# print_max(3, 4)  # пряма передача значень

# x = 5
# y = 7
# print_max(x, y)  # передача змінних у якості аргументів

# --- Типізація параметрів функції ---
# def print_max(a: int, b: int):
#     if a > b:
#         print(a, 'максимально')
#     elif a == b:
#         print(a, 'дорівнює', b)
#     else:
#         print(b, 'максимально')

# print_max(3, 4)  # пряма передача значень

# x = 5
# y = 7
# print_max(x, y)  # передача змінних у якості аргументів

# --- Повернення результату (return) ---
# ----- Приклад 1 (int)
# def add_numbers(num1: int, num2: int) -> int:
#     sum = num1 + num2
#     return sum

# x = input("Enter first number: ")
# y = input("Enter second number: ")

# result = add_numbers(int(x), int(y))
# print(result) 

# ----- Приклад 2 (str)
# def greet(name: str) -> str:
#     return f"Привіт, {name}!"

# greeting = greet("Олексій")
# print(greeting)

# ----- Приклад 3 (bool)
# def is_even(num: int) -> bool:
#     return num % 2 == 0

# val = int(input("Enter a number: "))

# check_even = is_even(val)
# print("Is even:", check_even)

"""Принципи змінності об'єктів у Python"""

"""НЕЗМІННІ типи в Python — це ті, що не можуть бути змінені після їх створення. Це включає типи, як-от цілі числа int, дійсні числа float, рядки str, кортежі tuple. типи в Python — це ті, що не можуть бути змінені після їх створення. Це включає типи, як-от цілі числа int, дійсні числа float, рядки str, кортежі tuple."""

"""ЗМІННІ типи, як списки list, словники dict, множини set, можуть змінюватися. Коли змінний об'єкт передається у функцію, передається посилання на цей об'єкт, і зміни, зроблені всередині функції, відображаються на оригінальному об'єкті."""

# ----- Приклад 1 (не змінні типи)
# def modify_string(original: str) -> str:
#     original = "змінено"
#     return original

# str_var = "оригінал"
# print(modify_string(str_var))  # виведе: змінено
# print(str_var)                # виведе: оригінал

# ----- Приклад 2 (змінні типи)
# def modify_list(lst: list) -> None:
#     lst.append(4)

# my_list = [1, 2, 3]
# modify_list(my_list)
# print(my_list)  # виведе: [1, 2, 3, 4]

# ----- Приклад 3 (copy())
# def modify_list(lst: list) -> None:
#     lst = lst.copy()
#     lst.append(4)

# my_list = [1, 2, 3]
# modify_list(my_list)
# print(my_list)  # виведе: [1, 2, 3]




# --------------- EXAMPLES with functions -------------

# ----- Example 1
# def real_cost(price: int, discount: float =0) -> float:
#     return price - price * discont / 100

# result = real_cost(100, 10)
# print(result)

# ----- Example 2
# def concat_string(*args):
#     result = ""
#     for str in args:
#         result += str
#     return result

# string = concat_string("Hello", " ", "world")
# string2 = concat_string("Python", " ", "is", " ", "awesome")

# print(string)
# print(string2)

# ----- Example 3
# def greet(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# greet(name="Alice", age=25)
# greet(name="Bob", age=30, city="New York")

# ----- Example 4
# def example_function(*args, **kwargs):
#     print("Позиційні аргументи:", args)
#     print(type(args))
#     print("Ключові аргументи:", kwargs)
#     print(type(kwargs))

# example_function(1, 2, 3, name="Alice", age=25)

"""Розпакування списків та словників"""
# my_list = [1, 2, 3]
# a, b, c = my_list
# d, _, e = my_list
# f, *rest = my_list

# # ----- Example 5
# def greet(name, age):
#     print(f"Hello {name}, you are {age} years old.")

# person_info = {"name": "Alice", "age": 25}
# greet(**person_info)

"""Рекурсія"""
# def factorial(n):
#     print("Виклик функції factorial з n = ", n)
#     if n == 1:
#         print("Базовий випадок, n = 1, повернення 1")
#         return 1
#     else:
#         result = n * factorial(n-1)
#         print("Повернення результату для n = ", n, ": ", result)
#         return result

# print(factorial(5))

# x = "string"
# print(len(x))

# def func(*args):
#     print(len(args))

# func(1, 2, 3, 4, 5)

# obj = {"a": 1, "b": 2, "c": 3}
# print(len(obj))
# arr = obj.keys()
# print(len(arr))

"""--- !!! ---"""
"""Tasks from lection"""
# # Task 1
# winners = ["Ukraine", "Spain", "Italy", "France", "Germany", "Ukraine", "Italy", "Spain", "Ukraine"]
# stats = {}

# for winner in winners:
#     if winner in stats:
#         stats[winner] += 1
#     else:
#         stats[winner] = 1

# print(stats)

# # Task 2
# #camelCase, PascalCase to snake_case

# # camelCase
# string = "geekForGeeks"
# result = ""

# for char in string:
#     if char.isupper():
#         result += "_" + char.lower()
#     else:
#         result += char

# print(result)

# # PascalCase
# string = "GeekForGeeks"
# result = ""

# for char in string:
#     if char.isupper():
#         result += "_" + char.lower()
#     else:
#         result += char

# # res = result[1:] # first approach
# res = result.removeprefix("_") # second approach

# print(res)

# # Task 3
# Create menu

# menu = """
# 1. Add new contact
# 2. Show all contacts
# 3. Search contact
# 4. Exit
# """

# print(menu)

# if ... else approach
# while True:
#     try:
#         choice = int(input("Enter your choice: "))
#         if choice > 4 or choice < 1:
#             raise Exception("Please enter a number from 1 to 4")
#         if choice == 1:
#             print("You chose 1 - Add new contact")
#         elif choice == 2:
#             print("You chose 2 - Show all contacts")
#         elif choice == 3:
#             print("You chose 3 - Search contact")
#         elif choice == 4:
#             break
#     except ValueError:
#         print("Please enter a number")
#         continue
#     except Exception as e:
#         print(e)
#         continue

# match approach
# while True:
#     try:
#         choice = int(input("Enter your choice: "))
#         match choice:
#             case 1:
#                 print("You chose 1 - Add new contact")
#             case 2:
#                 print("You chose 2 - Show all contacts")
#             case 3:
#                 print("You chose 3 - Search contact")
#             case 4:
#                 break
#             case _:
#                 raise Exception("Please enter a number from 1 to 4")
#     except ValueError:
#         print("Please enter a number")
#         continue
#     except Exception as e:
#         print(e)
#         continue





