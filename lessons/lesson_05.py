"""Open and close files."""


# fh = open('test.txt')
# fh.close()


"""
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

Параметри:
    file - шлях до файлу у вигляді рядка. Це може бути повний шлях або шлях відносно поточного каталогу виконання.
    mode (необов'язковий) - режим, в якому буде відкрито файл. Ось основні режими які ми будемо використовувати:
    'r' - читання (за замовчуванням). Файл має існувати.
    'w' - запис. Створює новий файл або перезаписує, що вже існує.
    'a' - додавання. Дописує в кінець файлу, не перезаписуючи його.
    'b' - бінарний режим (може бути використаний разом з іншими, наприклад 'rb' або 'wb').
    '+' - оновлення (читання та запис).
    buffering (необов'язковий) - визначає буферизацію: 0 для вимкненої, 1 для включеної буферизації рядків, більше 1 для вказання розміру буфера у байтах.
    encoding (необов'язковий) - ім'я кодування, яке буде використовуватися для кодування або декодування файлу.
    errors (необов'язковий) - вказує, як обробляти помилки кодування.
    newline (необов'язковий) - контролює, як обробляються нові рядки.
    closefd (необов'язковий) - має бути True (за замовчуванням); якщо вказано False, файловий дескриптор не буде закритий.
    opener (необов'язковий) - визначає спеціальну функцію для відкриття файлу.
"""

# Відкрити файл для запису або створити новий, якщо його немає, або перезаписати файл - 'w'
# fh = open('test.txt', 'w')
# symbols_written = fh.write('hello!')
# print(symbols_written) # 6
# fh.close()


# Метод read, який дозволяє прочитати деяку кількість символів із файлу - read()
# fh = open('test.txt', 'w+')
# fh.write('hello!')
# fh.seek(0)

# first_two_symbols = fh.read(2)
# print(first_two_symbols)  # 'he'

# fh.close()


# Метод readlines, який дозволяє прочитати всі рядки файлу у вигляді списку - readlines()
# fh = open('test.txt', 'w')
# fh.write('first line\nsecond line\nthird line')
# fh.close()

# fh = open('test.txt', 'r')
# while True:
#     line = fh.readline()
#     if not line:
#         break
#     print(line)

# fh.close()


# Аналогічний метод readlines, який читає увесь файл повністю, але повертає список рядків, де елемент списку — це один рядок з файлу
# fh = open("test.txt", "w")
# fh.write("first line\nsecond line\nthird line")
# fh.close()

# fh = open("test.txt", "r")
# lines = [el.strip() for el in fh.readlines()]
# print(lines)

# fh.close()


# Метод seek, дає можливість управляти положенням курсора (вказівника)
# fh = open('test.txt', 'w+')
# fh.write('hello!')

# fh.seek(1)
# second = fh.read(1)
# print(second)  # 'e'

# fh.close()

# Метод tell, повертає позицію (номер) символу з початку файлу, де зараз знаходиться курсор.
# fh = open("test.txt", "w+")
# fh.write("hello!")

# position = fh.tell()
# print(position)  # 6

# fh.seek(1)
# position = fh.tell()
# print(position)  # 1

# fh.read(2)
# position = fh.tell()
# print(position)  # 3

# fh.close()

"""
Менеджер контексту

Застосунок може виконати багато операцій між відкриттям та закриттям файлу. В будь-якому місці може статися помилка та застосунок завершиться аварійно, не повернувши файловий дескриптор системі. Така поведінка, як вже згадувалося, небажана і може призводити до втрати даних.

Щоб уникнути цього, можна взяти блок коду, в якому відбувається робота з файлом, у блок try ... except:
"""

# CLASSIC approach:
# fh = open('text.txt', 'w')
# try:
#     # Виконання операцій з файлом
#     fh.write('Some data')
# finally:
#     # Закриття файлу в блоку finally гарантує, що файл закриється навіть у разі помилки
#     fh.close()

# Using CONTEXT manager:
# with open('text.txt', 'w') as fh:
#     # Виконання операцій з файлом
#     fh.write('Some data')
# # Файл автоматично закриється після виходу з блоку with


"""Робота з не текстовими файлами у Python"""
"""Якщо ж потрібно працювати не з текстовими файлами, то можна вказати режим відкриття файлів як b, скорочено від bytes. У такому режимі ви отримаєте файловий об'єкт для роботи з файлом в режимі байт-рядків."""
"""Щоб працювати з послідовністю байтів у Python є вбудовані типи даних байт-рядків
    bytes - незмінний тип, що використовують для представлення байтів.
    bytearray - змінний тип, що дозволяє модифікувати байти після їх створення."""

# with open('raw_data.bin', 'wb') as fh:
#     fh.write(b'Hello world!')

# Для перетворення рядка у байт-рядок можна скористатися методом рядків encode.
# byte_str = 'some text'.encode()
# print(byte_str)
"""Синтаксис:
str.encode(encoding="utf-8", errors="strict")
    encoding - вказує метод кодування. По замовчуванню використовується 'utf-8', який підтримує велику кількість символів з різних мов.
    errors - вказує, як обробляти помилки кодування. Наприклад, 'strict' для викидання виключення у випадку помилки, 'ignore' для ігнорування помилок або 'replace' для заміни неможливих для кодування символів на певний замінник (?).
"""



""""
Порівняння рядків
Принцип порівняння рядків, з перетворенням їх у єдиний регістр, використовується для забезпечення нерозрізнення регістру при порівнянні. Це особливо корисно, коли порівняння повинно бути незалежним від того, чи введено рядок у верхньому, нижньому чи змішаному регістрі.
"""

# string1 = "Hello World"
# string2 = "hello world"
# if string1.lower() == string2.lower():
#     print("Рядки однакові")
# else:
#     print("Рядки різні")

# casefold() - метод, який повертає рядок, перетворений у нижній регістр, при цьому враховуючи спеціальні символи для різних мов (Німецька).
# text = "Python Programming"
# print(text.casefold()) # python programming

# german_word = 'straße'  # В нижньому регістрі
# search_word = 'STRASSE'  # В верхньому регістрі

# # Порівняння за допомогою lower()
# lower_comparison = german_word.lower() == search_word.lower()

# # Порівняння за допомогою casefold()
# casefold_comparison = german_word.casefold() == search_word.casefold()

# print(f"Порівняння з lower(): {lower_comparison}")
# print(f"Порівняння з casefold(): {casefold_comparison}")


"""Робота з архівами"""
"""
Модуль shutil в Python - це модуль стандартної бібліотеки, який надає ряд функцій для роботи з файлами і колекціями файлів. Цей модуль може бути використаний для копіювання, переміщення, перейменування та видалення файлів і директорій, забезпечуючи високорівневі операції для обробки файлової системи, які є більш зручними, ніж використання базових функцій модуля os.
"""

# shutil.make_archive() - створення архіва
"""Синтаксис методу:
shutil.make_archive(base_name, format, root_dir=None, base_dir=None)

Параметри:
    base_name - шлях до файлу, де потрібно зберегти архів, без розширення.
    format - формат архіву, наприклад 'zip', 'tar', 'gztar', 'bztar' або 'xztar'.
    root_dir - директорія, з якої буде створено архів. Якщо не вказано, використовується поточна директорія.
    base_dir - директорія всередині архіву, з якої почнеться архівація.
"""

# import shutil
# # Створення ZIP-архіву з вмістом директорії 'my_folder'
# shutil.make_archive('example', 'zip', root_dir='my_folder')
# # Створення TAR.GZ архіву
# shutil.make_archive('example', 'gztar', root_dir='my_folder')

# shutil.unpack_archive()
"""Синтаксис
shutil.unpack_archive(filename, extract_dir=None, format=None)

Параметри

    filename - шлях до архівного файлу, який потрібно розпакувати.
    extract_dir - директорія, куди буде розпаковано вміст архіву. Якщо не вказано, використовується поточна директорія.
    format - формат архіву наприклад, zip, tar, gztar, bztar, або xztar. Якщо параметр не вказано, Python намагається визначити формат автоматично.
"""
# import shutil
# # Розпакування ZIP-архіву в певну директорію
# shutil.unpack_archive('example.zip', 'destination_folder')

"""
Основи модуля pathlib

Модуль pathlib в Python є сучасним інструментом для роботи з файловою системою, що надає об'єктно-орієнтований інтерфейс для роботи з шляхами. Він прийшов на заміну застарілому модулю os, роботу з яким ще можна зустріти в старих прикладах коду.

pathlib - це модуль у Python, який надає класи для обробки файлових шляхів у об'єктно-орієнтованому стилі. Два основних класи у цьому модулі - це Path та PurePath.
"""

# from pathlib import PurePath

# p = PurePath("/usr/bin/simple.jpg")
# print("Name:", p.name) # Name: simple.jpg
# print("Suffix:", p.suffix) # Suffix: .jpg
# print("Parent:", p.parent) # Parent: \usr\bin

# #  -----------------------------------------

# from pathlib import Path

# p = Path("example.txt")
# p.write_text("Hello, world!")
# print(p.read_text()) # Hello, world!
# print("Exists:", p.exists()) # Exists: True

"""Створення Шляхів"""
# from pathlib import Path

# # Для Unix/Linux
# path_unix = Path("/usr/bin/python3")

# # Для Windows
# path_windows = Path("C:/Users/Username/Documents/file.txt")

# # Example
# # Початковий шлях
# base_path = Path("/usr/bin")

# # Додавання додаткових частин до шляху
# full_path = base_path / "subdir" / "script.py"

# print(full_path)  # Виведе: /usr/bin/subdir/script.py



"""Відносні та абсолютні шляхи"""
# from pathlib import Path

# # Перетворення відносного шляху в абсолютний
# relative_path = Path("documents/example.txt")
# absolute_path = relative_path.absolute()
# print(absolute_path)



# --- relative_to() ---
# from pathlib import Path

# # Перетворення відносного шляху в абсолютний
# relative_path = Path("documents/example.txt")
# absolute_path = relative_path.absolute()

# current_working_directory = Path("E:\WebDir\Works\Python\python-help-solution\example_for_new_core\l04")
# relative_path = absolute_path.relative_to(current_working_directory)
# print(relative_path)



# --- with_name() ---
# from pathlib import Path

# # Початковий шлях до файлу
# original_path = Path("documents/example.txt")
# # Зміна імені файлу
# new_path = original_path.with_name("report.txt")
# print(new_path) # documents\report.txt



# --- with_suffix() ---
# from pathlib import Path

# # Початковий шлях до файлу
# original_path = Path("documents/example.txt")
# # Зміна імені файлу
# new_path = original_path.with_suffix(".md")
# print(new_path) # documents\example.md

"""Але треба розуміти, що методи with_name і with_suffix в класі Path модуля pathlib в Python не змінюють фізичне ім'я файлу на диску. Замість цього, вони використовуються для створення нового об'єкта Path, який відображає змінений шлях."""

# from pathlib import Path

# original_path = Path("documents/example.txt")
# # Створює новий об'єкт Path з іншим ім'ям файлу
# new_path = original_path.with_name("report.txt")
# print(original_path) # documents\example.txt
# print(new_path) # documents\report.txt



# --- rename() ----
# from pathlib import Path

# original_path = Path("documents/example.txt")
# # Створює новий об'єкт Path з іншим ім'ям файлу
# new_path = original_path.with_name("report.txt")
# original_path.rename(new_path)



"""Читання та запис файлів"""
"""Методи read_text() та write_text() використовуються для читання та запису текстових файлів."""
"""Синтаксис методу read_text()

Path.read_text(encoding=None, errors=None)
Параметри:
    encoding - необов'язковий, ім'я кодування, яке використовується для декодування файлу. Якщо не вказано, використовується кодування за замовчуванням.
    errors - необов'язково, інструкція, як обробляти помилки декодування.

Синтаксис методу write_text()
Path.write_text(data, encoding=None, errors=None)
    data - рядок, який необхідно записати в файл.
    encoding - необов'язковий, ім'я кодування, яке використовується для декодування файлу. Якщо не вказано, використовується кодування за замовчуванням.
    errors - необов'язково, інструкція, як обробляти помилки декодування.


Як бачимо параметр errors, в обох методах, визначає, як мають бути оброблені ці помилки.
    errors='strict'. Це значення за замовчуванням. Якщо виникає помилка декодування, буде викинуто виключення UnicodeDecodeError.
    errors='ignore'. Якщо ми хочемо ігнорувати помилки декодування. Частини тексту, що не можуть бути декодовані, будуть просто пропущені.
    errors='replace'. Якщо пропускати ми не хочемо, то замінимо неможливі для декодування символи на спеціальний символ заміни, згідно документації символ '?'.    
"""
"""Методи read_bytes() та write_bytes() використовуються для читання та запису бінарних файлів."""


# # Приклад запису тексту у файл
# from pathlib import Path

# # Створення об'єкту Path для файлу
# file_path = Path("example.txt")

# # Запис тексту у файл
# file_path.write_text("Привіт світ!", encoding="utf-8")

# # Приклад читання тексту з файлу
# from pathlib import Path

# # Створення об'єкту Path для файлу
# file_path = Path("example.txt")

# # Читання тексту з файлу
# text = file_path.read_text(encoding="utf-8")
# print(text)





"""Робота з директоріями"""

# Метод iterdir() використовується для отримання переліку всіх файлів та піддиректорій у вказаній директорії. 
from pathlib import Path
# Створення об'єкту Path для директорії
directory = Path("./picture")
# Виведення переліку всіх файлів та піддиректорій
for path in directory.iterdir():
    print(path)


'''Для створення нової директорії використовується метод mkdir().

Path.mkdir(mode=0o777, parents=False, exist_ok=False)
Параметри:
    mode - права доступу до директорії, використовуються для Linux і не актуальні для Windows.
    parents - якщо має значення True, створить всі батьківські директорії, які відсутні.
    exist_ok - якщо має значення True, помилка не буде викинута, якщо директорія вже існує.
'''

from pathlib import Path
directory = Path('/my_directory/new_folder')
directory.mkdir(parents=True, exist_ok=True)


"""Для видалення директорії використовується метод rmdir(). Він видаляє директорію, але директорія повинна бути порожньою.

from pathlib import Path
directory = Path('/my_directory/new_folder')
directory.rmdir()
Модуль pathlib також надає декілька методів для перевірки існування та типу файлових об'єктів:
    метод exists() перевіряє, чи існує файл або директорія.
    метод is_dir() перевіряє, чи є об'єкт директорією.
    метод is_file() перевіряє, чи є об'єкт файлом.
"""

from pathlib import Path

path = Path("./picture")

# Перевірка існування
if path.exists():
    print(f"{path} існує") # picture існує

# Перевірка, чи це директорія
if path.is_dir():
    print(f"{path} є директорією") # picture є директорією

# Перевірка, чи це файл
if path.is_file():
    print(f"{path} є файлом")




"""Переміщення та копіювання файлів"""
"""Модуль pathlib чудово інтегрується з модулем shutil для виконання операцій копіювання та переміщення файлів. 
Для копіювання файлів використовується функція shutil.copy() або shutil.copy2()."""

import shutil
from pathlib import Path

# Вихідний і цільовий файли
source = Path('/path/to/source/file.txt')
destination = Path('/path/to/destination/file.txt')

# Копіювання файла
shutil.copy(source, destination)



"""Для переміщення файлів використовується функція shutil.move()."""
import shutil
from pathlib import Path

# Вихідний і цільовий шляхи
source = Path('/path/to/source/file.txt')
destination = Path('/path/to/destination/file.txt')

# Переміщення файла
shutil.move(source, destination)



"""Метод stat() повертає інформацію про файл, включаючи його розмір."""
from pathlib import Path

file_path = Path("./picture/bot-icon.png")

# Отримання розміру файла
size = file_path.stat().st_size
print(f"Розмір файла: {size} байтів") # Розмір файла: 2876 байтів

# Час створення та модифікації
creation_time = file_path.stat().st_ctime
modification_time = file_path.stat().st_mtime
print(f"Час створення: {time.ctime(creation_time)}") # Час створення: Fri Dec 29 04:43:16 2023
print(f"Час модифікації: {time.ctime(modification_time)}") # Час модифікації: Thu May 17 19:59:44 2018



"""Для видалення файлу використовується метод unlink(). """
from pathlib import Path

# Створення об'єкту Path для файлу
file_path = Path('/path/to/file.txt')

# Перевірка, чи файл існує, перш ніж видаляти
if file_path.exists():
    file_path.unlink()
    print(f'Файл {file_path} було видалено')
else:
    print(f'Файл {file_path} не існує')


# Можна також видалити файл без попередньої перевірки його існування, використовуючи параметр missing_ok.
from pathlib import Path
file_path = Path('/path/to/file.txt')
file_path.unlink(missing_ok=True)
