"""Робота з модулями та створення віртуального оточення"""

# --- Iport and use package ---
# import math
# sin_pi = math.sin(math.pi)

# ----------------------------

# from math import pi, sin
# sin_pi = sin(pi)

# ----------------------------
# # mymodule.py
# def say_hello(name):
#     return f"Hello, {name}!"

# # main.py
# import mymodule
# print(mymodule.say_hello("World"))
# # OR
# # main.py
# from mymodule import say_hello
# print(say_hello("World"))
# # OR
# # main.py
# from mymodule import say_hello as greeting
# print(greeting("World"))

# --- Функція dir() ---
# Виводить список імен, які визначені в поточному модулі

# --- Службова змінна __name__ ---
# Визначає, чи є поточний модуль головним

# --- Модуль sys. Обробка аргументів командного рядка ---
"""    
sys.argv - список аргументів командного рядка, переданих скрипту Python. Елемент argv[0] є ім'ям скрипту, а інші елементи – це додаткові аргументи командного рядка.
sys.exit() - функція виходу з Python. Ви можете передати числовий аргумент, що стане статусом виходу програми. Прийнято, що аргумент 0 означає успішне завершення, а ненульові значення вказують на помилку.
sys.path - список рядків, який визначає шлях пошуку інтерпретатора для модулів. Ви можете модифікувати цей список, щоб додати власні шляхи для пошуку модулів.
sys.version - рядок, що містить інформацію про версію Python, яка використовується.
sys.platform - рядок, що вказує на ім'я платформи, на якій виконується Python (наприклад, 'linux' для Linux, 'win32' для Windows).
sys.modules - словник, який містить завантажені модулі. Ключі – це назви модулів, а значення – це об'єкти модулів.
"""
import sys
print(sys.argv)
print(sys.version)
print(sys.platform)

# --- Модуль os. Робота з операційною системою ---
import os
print(sys.modules["os"])
print(sys.modules.keys())
print(sys.builtin_module_names)

# sys.path
print(sys.path)

# sys.argv
for arg in sys.argv:
    print(arg)

# python echo.py test --user -hello some text 
#  !!! Example 01 in folders


# --- Створення пакетів та модулів ---
"""Основне правило — це називати пакети та модулі так само, як і змінні Python (тільки літери, цифри та _, ім'я не починається з цифри)"""


# --- Файл __init.py__ ---
"""У версіях Python до 3.3 в пакетах обов'язково потрібно було розмістити допоміжний файл __init__.py. Якщо цього не зробити, то Python не сприймав директорію як пакет та імпортувати з такої директорії нічого не міг. Зараз в цьому немає потреби, але часто такі файли створюються для зворотної сумісності зі старими версіями."""
"""Зазвичай __init__.py — порожній і нічого не робить. """
#  !!! Example 02 in folders



"""Пакетний менеджер pip та створення віртуального оточення"""
"""Встановлення додаткових пакетів в Python здійснюється менеджерами пакетів. Стандартний (але не єдиний) менеджер пакетів Python — це pip. Пакетний менеджер pip є інструментом, який дозволяє вам встановлювати, оновлювати та видаляти бібліотеки та інструменти, що використовуються в програмуванні на Python. Це ключовий інструмент у світі Python, який робить керування зовнішніми бібліотеками та їхніми залежностями значно простішим."""
# python3 -m pip list

# Для встановлення останньої версії пакету, на прикладі пакету requests:
# pip install requests

# Для встановлення конкретної версії пакету requests:
# pip install requests==2.28.2

# Встановлення версії пакету requests новішого за 2.28.2:
# pip install requests>=2.28.2

# Встановлення версії пакету requests давнішого за 2.28.2:
# pip install requests<=2.28.2

# Видалення пакету requests:
# pip uninstall requests

# Список встановлених пакетів з версіями:
# pip freeze
# !!! This command shows exactly list of packages that are necessary for the project to run. Important to save this list in a file requirements.txt



# --- Створення віртуального оточення ---
"""Віртуальне оточення - це ізольоване середовище для Python проєктів. Використовуючи віртуальне оточення, можна встановлювати бібліотеки та їхні залежності в межах цього середовища, не впливаючи на глобальне середовище Python або на інші віртуальні оточення."""

# STEP 1: Create virtual environment
"""Щоб створити нове віртуальне оточення, виконайте наступні кроки:

    Відкрийте термінал або командний рядок.
    Перейдіть до директорії, де ви хочете створити свій Python проєкт.
    Виконайте наступну команду для створення віртуального оточення:

    python3 -m venv .venv 
    OR
    python3 -m venv .env
"""

# STEP 2: Activate virtual environment
"""Щоб почати використовувати Python з віртуального оточення, виконайте активацію віртуального оточення. Для активації віртуального оточення, використовуйте одну з наступних команд, в залежності від вашої системи та командного інтерпретатора:

    source .venv/bin/activate

Після активації командний рядок зміниться, відображаючи назву віртуального оточення, це показує, що воно активне.
"""

# STEP 3: Deactivate virtual environment
"""
Щоб повернутися до системного Python, виконайте в консолі:
    
    deactivate
"""

# STEP 4: Delete virtual environment
"""
Щоб видалити віртуальне оточення, достатньо фізично видалити директорію .venv з усім її вмістом в директорії проєкту."""

# Example 04 in folders

# --- Create requirements.txt ---
# pip freeze > requirements.txt
# !!! This command creates a file requirements.txt with a list of all packages that are necessary for the project to run.

# Щоб встановити пакети, перелічені у requirements.txt, використовуйте команду:
# pip install -r requirements.txt




"""Структура проєкту"""

"""Принцип KISS
Принцип KISS (Keep It Simple, Stupid) — це концепція в дизайні та програмуванні, яка підкреслює важливість простоти у розробці. Основна ідея полягає в тому, щоб утримуватись від зайвої складності та зробити рішення якомога більш простими та зрозумілими."""
# Without KISS
def is_even(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False


# With KISS
def is_even(number: int) -> bool:
    return number % 2 == 0

"""
Принцип DRY

Принцип DRY (Don't Repeat Yourself) закликає розробників уникати повторення однакових частин коду у різних частинах програми. Основна мета - зробити код більш ефективним, легким для розуміння та підтримки. Повторення коду може призвести до помилок, оскільки при зміні логіки доведеться вносити зміни у кожне місце, де цей код використовується."""

# Without DRY
# Розрахунок площі 
length1, width1 = 5, 10
area1 = length1 * width1

length2, width2 = 7, 12
area2 = length2 * width2

# With DRY
def calculate_area(length: float, width: float) -> float:
    return length * width

area1 = calculate_area(5, 10)
area2 = calculate_area(7, 12)


"""For creating package that will be upload to the PyPi"""
"""Main examople - package https://pypi.org/project/moskali/"""
# --- Step 1 ---
# install packages:
pip3 install setuptools
pip3 install wheel
pip3 install twine

# --- Step 2 ---
# Create setup.py file
# from setuptools import setup, find_packages

# --- Step 3 ---
# run setup.py file from the terminal:
python3 setup.py sdist bdist_wheel

# after it will be created two folders: dist and build
# dist - contains the package that will be uploaded to the PyPi
# build - contains the package that will be uploaded to the Py
# in dist folder there will be two files: .tar.gz and .whl

# --- Step 4 ---
# Upload package to the PyPi
twine upload dist/* # uploading to the PyPi
twine upload --repository testpypi dist/* # uploading to the test PyPi

# --- Step 5 ---
# If I want to install package locally:
python3 -m pip install -e . # run this command in the folder where setup.py is located
