"""FIND"""
s = "Hi there!"

start = 0
end = 7

print(s.find("er", start, end)) # 5
print(s.find("q")) # -1

"""INDEX"""
# print(s.index("q")) # ValueError: substring not found

"""RFIND"""
s = 'Some words'

print(s.find("o"))
print(s.rfind('o'))

"""RINDEX"""
print(s.index("o"))
print(s.rindex('o'))

"""split()"""
"""Синтаксис методу split()
str.split(separator=None, maxsplit=-1)
де:
    separator - роздільник, за яким слід розділяти рядок. Якщо не вказано, рядок розділяється за будь-яким пробілом.
    maxsplit - максимальна кількість розділень. Значення -1 означає "без обмежень"."""

# Приклад 1. Розділення рядка за пробілами
text = "hello world"
result = text.split()
print(result)  # Виведе: ['hello', 'world']

# Приклад 2. Розділення рядка за символом
text = "apple,banana,cherry"
result = text.split(',')
print(result)  # Виведе: ['apple', 'banana', 'cherry']

"""join()"""
"""Синтаксис методу join()
string.join(iterable)
де:
    string - рядок роздільник, який буде вставлений між елементами послідовності.
    iterable - послідовність, список або кортеж рядків, які потрібно об'єднати."""

# Приклад 1. Об'єднання рядків
list_of_strings = ['Hello', 'world']
result = ' '.join(list_of_strings)
print(result)  # Виведе: 'Hello world'

# Приклад 2. Об'єднання символів
elements = ['earth', 'air', 'fire', 'water']
result = ', '.join(elements)
print(result)  # Виведе: 'earth, air, fire, water'

"""strip()"""
clean = '   spacious   '.strip()
print(clean) # spacious

"""
"лівий", lstrip, видаляє тільки пробіли на початку рядка;
та "правий", rstrip, видаляє тільки пробіли в кінці рядка.
"""

"""replace()"""
"""Метод replace() має наступний синтаксис
str.replace(old, new, count=-1)
де:
    old - підрядок, який потрібно замінити.
    new - підрядок, на який потрібно замінити.
    count - лічильник максимальної кількості замін. Якщо не вказано або вказано -1, замінюються всі входження."""

# Приклад 1. Заміна підрядка
text = "Hello world"
new_text = text.replace("world", "Python")
print(new_text) 

# Приклад 2. Заміна обмеженої кількості разів
text = "one fish, two fish, red fish, blue fish"
new_text = text.replace("fish", "bird", 2)
print(new_text)  

# Приклад 3. Видалення підрядка
text = "Hello, world!"
new_text = text.replace(" world", "")
print(new_text)

"""removeprefix()"""
print('TestHook'.removeprefix('Test')) # Hook
print('TestHook'.removeprefix('Hook')) # TestHook

"""removesuffix()"""
print('TestHook'.removesuffix('Test'))
print('TestHook'.removesuffix('Hook'))

"""isdigit(), isalpha(), isspace()"""
print("123".isdigit()) # True
print("Number123".isdigit()) # False
print("hello".isalpha()) # True
print(" ".isspace()) # True

"""translate()"""
# Приклад 1. Заміна символів
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

str = "This is string example"
print(str.translate(trantab)) # Th3s 3s str3ng 2x1mpl2

# Приклад 2. Видалення символів
intab = "aeiou"
trantab = str.maketrans('', '', intab)

str = "This is string example"
print(str.translate(trantab)) # Ths s strng xmpl


"""regular expressions"""
import re

# Приклад 1. Пошук підрядка
text = "Вивчення Python може бути веселим."
pattern = "Python"
match = re.search(pattern, text)

if match:
    print("Знайдено:", match.group()) # Python
else:
    print("Не знайдено.") 

# Приклад 2. Пошук підрядка з використанням шаблону
text = "Вивчення Python може бути веселим."
pattern = r"в\w*м"
match = re.search(pattern, text, re.IGNORECASE)

if match:
    print("Знайдено:", match.group()) # веселим

# Приклад 3. Пошук email-адреси
text = "Моя електронна адреса: example@example.com"
pattern = r"\w+@\w+\.\w+"
match = re.search(pattern, text)

if match:
    print("Електронна адреса:", match.group())

"""re.findall()"""
"""Синтаксис методу:
import re
matches = re.findall(pattern, string)
    pattern - регулярний вираз, який ви шукаєте.
    string - рядок, у якому потрібно знайти відповідності."""

import re

text = "Рік 2023 був складнішим, ніж 2022"
pattern = r"\d+"
matches = re.findall(pattern, text)

print(matches) # ['2023', '2022']

"""re.sub()"""
"""Синтаксис:
import re

modified_string = re.sub(pattern, repl, string)
    pattern - регулярний вираз, який вказує на частину рядка, яку потрібно замінити.
    repl - рядок, на який буде замінено збіги.
    string - рядок, в якому відбувається заміна."""

import re

# Приклад 1. Заміна пробілів на підкреслення
file_name = "Мій документ Python.txt"
pattern = r"\s"
replacement = "_"
formatted_name = re.sub(pattern, replacement, file_name)

print(formatted_name)  

# Приклад 2. Форматування номерів телефонів
phone = """
        Михайло Куліш: 050-171-1634
        Вікторія Кущ: 063-134-1729
        Оксана Гавриленко: 068-234-5612
        """
pattern = r"(\d{3})-(\d{3})-(\d{4})"
replacement = r"(\1) \2-\3"
formatted_phone = re.sub(pattern, replacement, phone)

print(formatted_phone)

"""re.split()"""
"""Синтаксис:
import re
list_of_elements = re.split(pattern, string)
    pattern - регулярний вираз, який використовується як роздільник.
    string - рядок, який потрібно розділити."""

import re

# Приклад 1. Розділення рядка за пробілами
text = "Python - це проста, але потужна мова програмування."
pattern = r"\s+"
words = re.split(pattern, text)

print(words)  # Виведе список слів у рядку

# Приклад 2. Розділення рядка за символами !!! звичайний метод split() таке вже зробити не зможе !!!
text = "apple#banana!mango@orange;kiwi"
pattern = r"[#@;!]"
fruits = re.split(pattern, text)

print(fruits)
