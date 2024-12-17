"""Іменовані кортежі"""

from collections import namedtuple

# --- Example 1
# Створення іменованого кортежу
# Point = namedtuple('Point', ['x', 'y'])
# p = Point(11, y=22)
# print(p)
# print(p.x, p.y)

# --- Example 2
# import collections

# # Створення іменованого кортежу Person
# Person = collections.namedtuple('Person', ['first_name', 'last_name', 'age', 'birth_place', 'post_index'])

# # Створення екземпляра Person
# person = Person('Mick', 'Nitch', 35, 'Boston', '01146')

# # Виведення різних атрибутів іменованого кортежу
# print(person.first_name)       
# print(person.post_index) 
# print(person.age)        
# print(person[3])         

# --- Example 3
# import collections

# Cat = collections.namedtuple('Cat', ['nickname', 'age', 'owner'])

# cat = Cat('Simon', 4, 'Krabat')

# print(f'This is a cat {cat[0]}, {cat[1]} age, his owner {cat[2]}') # Not good for understanding
# print(f'This is a cat {cat.nickname}, {cat.age} age, his owner {cat.owner}') # Good for understanding 

"""Counter"""
# --- solution with dict - less readable
# import pprint

# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7, 1, 1, 1, 3, 5]
# mark_counts = {}
# for mark in student_marks:
#     if mark in mark_counts:
#         mark_counts[mark] += 1
#     else:
#         mark_counts[mark] = 1

# pp = pprint.PrettyPrinter(indent=4)

# pp.pprint(mark_counts)

# person = {"name": "Bob", "age": 25, "city": "New York", "friends": ["Alice", "John"], "marks": mark_counts}
# pp.pprint(person)


# --- solution with Counter - more readable
# -- Example 1
import collections

# student_marks = [4, 2, 4, 6, 7, 4, 2, 3, 4, 5, 6, 6, 7 , 1, 1, 1, 3, 5]
# mark_counts = collections.Counter(student_marks)
# print(mark_counts)
# print(dict(mark_counts)) # convert to dict
# print(dir(collections.Counter()))

# --- Example 2
# import collections

# student_marks = [4, 2, 4, 6, 7, 4, 2 , 3, 4, 5, 6, 6, 7 , 1, 1, 1, 3, 5]
# mark_counts = collections.Counter(student_marks)

# print(mark_counts.most_common())
# print(mark_counts.most_common(1))
# print(mark_counts.most_common(2))

# --- Example 3
# from collections import Counter

# letter_count = Counter("banana")
# print(letter_count)

# # --- Example 4
# sentence = "the quick brown fox jumps over the lazy dog"
# words = sentence.split()
# word_count = Counter(words)

# for word, count in word_count.items():
#     print(f"{word}: {count}")


"""defaultdict"""
#  --- Example 1
# from collections import defaultdict

# # Створення defaultdict з list як фабрикою за замовчуванням
# d = defaultdict(list)

# # Додавання елементів до списку для кожного ключа
# d['a'].append(1)
# d['a'].append(2)
# d['b'].append(4)

# print(d)

# --- Example 2
# d = defaultdict(int)

# # Збільшення значення для кожного ключа
# d['a'] += 1
# d['b'] += 1
# d['a'] += 1

# print(d)

# --- Example 3 
# --- solution without defaultdict - not good
# words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
# grouped_words = {}

# for word in words:
#     char = word[0]
#     if char not in grouped_words:
#         grouped_words[char] = []
#     grouped_words[char].append(word)

# print(grouped_words)

# --- solution with defaultgict - better
# from collections import defaultdict

# words = ['apple', 'zoo', 'lion', 'lama', 'bear', 'bet', 'wolf', 'appendix']
# grouped_words = defaultdict(list)

# for word in words:
#     char = word[0]
#     grouped_words[char].append(word)

# print(dict(grouped_words))


"""Стек - LIFO - Last In, First Out"""
"""Існують основні операції стеку:

    Push - додавання елемента.
    Pop - вилучення елемента.
    Peek - перегляд верхнього елемента.
    Is Empty - перевірка стеку на порожнечу.
"""

# # Створення стеку
# def create_stack():
#     return []

# # Перевірка на порожнечу
# def is_empty(stack):
#     return len(stack) == 0

# # Додавання елементу
# def push(stack, item):
#     stack.append(item)

# # Вилучення елементу
# def pop(stack):
#     if not is_empty(stack):
#         return stack.pop()
#     else:
#         print("Стек порожній")

# # Перегляд верхнього елемента
# def peek(stack):
#     if not is_empty(stack):
#         return stack[-1]
#     else:
#         print("Стек порожній")

# stack = create_stack()
# push(stack, 'a')
# push(stack, 'b')
# push(stack, 'c')

# print(peek(stack))  # Виведе 'c'

# print(pop(stack))  # Виведе 'c'



"""Черга - (FIFO: First In, First Out)"""
"""Існують основні операції для черги:

    Enqueue - додавання елемента в кінець черги.
    Dequeue - видалення елемента з початку черги.
    Front/Peek - перегляд першого елемента черги без його видалення.
    Is Empty - перевірка, чи черга порожня.
    Size - визначення кількості елементів у черзі.
"""

# from collections import deque

# # Створення черги
# queue = deque()

# # Enqueue: Додавання елементів
# queue.append('a')
# queue.append('b')
# queue.append('c')

# print("Черга після додавання елементів:", list(queue))

# # Dequeue: Видалення елемента
# print("Видалений елемент:", queue.popleft())

# print("Черга після видалення елемента:", list(queue))

# # Peek: Перегляд першого елемента
# print("Перший елемент у черзі:", queue[0])

# # IsEmpty: Перевірка на порожнечу
# print("Чи черга порожня:", len(queue) == 0)

# # Size: Розмір черги
# print("Розмір черги:", len(queue))

"""Двостороння черга deque"""
"""Основні методи deque
    append(x) - додає елемент x в кінець черги.
    appendleft(x) - додає елемент x на початок черги.
    pop() - видаляє та повертає елемент з правого кінця черги. Якщо черга порожня, викидає виняток IndexError.
    popleft() - видаляє та повертає елемент з лівого кінця черги. Якщо черга порожня, викидає виняток IndexError.
"""

# from collections import deque

# # Створення пустої двосторонньої черги
# d = deque()

# # Додаємо елементи в чергу
# d.append('middle')  # Додаємо 'middle' в кінець черги
# d.append('last')    # Додаємо 'last' в кінець черги
# d.appendleft('first')  # Додаємо 'first' на початок черги

# # Виведення поточного стану черги
# print("Черга після додавання елементів:", list(d))

# # Видалення та виведення останнього елемента (з правого кінця)
# print("Видалений останній елемент:", d.pop())

# # Видалення та виведення першого елемента (з лівого кінця)
# print("Видалений перший елемент:", d.popleft())

# # Виведення поточного стану черги після видалення елементів
# print("Черга після видалення елементів:", list(d))


# Ще однією особливістю deque є можливість обмежити розмір Deque:
# from collections import deque

# d = deque(maxlen=5)
# for i in range(10):
#     d.append(i)

# print(d)

# --- EXAMPLE
# from collections import deque

# # Список завдань, де кожне завдання - це словник
# tasks = [
#     {"type": "fast", "name": "Помити посуд"},
#     {"type": "slow", "name": "Подивитись серіал"},
#     {"type": "fast", "name": "Вигуляти собаку"},
#     {"type": "slow", "name": "Почитати книгу"}
# ]

# # Ініціалізація черги завдань
# task_queue = deque()

# # Розподіл завдань у чергу відповідно до їх пріоритету
# for task in tasks:
#     if task["type"] == "fast":
#         task_queue.appendleft(task)  # Додавання на високий пріоритет
#         print(f"Додано швидке завдання: {task['name']}")
#     else:
#         task_queue.append(task)  # Додавання на низький пріоритет
#         print(f"Додано повільне завдання: {task['name']}")

# # Виконання завдань
# while task_queue:
#     task = task_queue.popleft()
#     print(f"Виконується завдання: {task['name']}")


"""Контроль точності обчислень decimal"""
# --- Example 1
# print(0.1 + 0.2 == 0.3)
# print(0.1 + 0.2)

# --- Example 2 - solution with decimal
# from decimal import Decimal

# print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
# print(Decimal("0.1") + Decimal("0.2"))

"""Точність обчислень з Decimal контролюється через контекст. Можна налаштувати загальну точність для всіх обчислень Decimal."""
# from decimal import Decimal, getcontext

# getcontext().prec = 6
# print(Decimal("1") / Decimal("7"))

# getcontext().prec = 8
# print(Decimal("1") / Decimal("7"))

"""Якщо ми потребуємо саме округлення чисел, нам необхідно використовувати метод quantize. Метод quantize використовується для встановлення точності числа Decimal, заснованої на іншому числі Decimal, яке використовується як шаблон."""
# from decimal import Decimal, ROUND_DOWN

# # Вихідне число Decimal
# number = Decimal('3.14159')

# # Встановлення точності до двох знаків після коми
# rounded_number = number.quantize(Decimal('0.00'), rounding=ROUND_DOWN)

# print(rounded_number)

# ROUND_FLOOR - округлення вниз
# ROUND_CEILING - округлення вгору
# ROUND_HALF_UP - округлення до найближчого
# ROUND_HALF_DOWN - округлення до найближчого, віддаляючи від нуля
# ROUND_HALF_EVEN - округлення до найближчого, вибираючи парне число
# ROUND_UP - округлення вгору
# ROUND_DOWN - округлення вниз
# ROUND_05UP - округлення до найближчого, збільшуючи 0.5

# --- !!! За замовчуванням округлення описується константою ROUND_HALF_EVEN !!! ---

# import decimal
# from decimal import Decimal
 
# number = Decimal("1.45")

# # Округлення за замовчуванням до одного десяткового знаку
# print("Округлення за замовчуванням ROUND_HALF_EVEN:", number.quantize(Decimal("0.0")))

# # Округлення вверх при нічиї (ROUND_HALF_UP)
# print("Округлення вгору ROUND_HALF_UP:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_HALF_UP))

# # Округлення вниз (ROUND_FLOOR)
# print("Округлення вниз ROUND_FLOOR:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_FLOOR))

# # Округлення вверх (ROUND_CEILING)
# print("Округлення вгору ROUND_CEILING:", number.quantize(Decimal("0.0"), rounding=decimal.ROUND_CEILING))

# # Округлення до трьох десяткових знаків за замовчуванням
# print("Округлення до трьох десяткових знаків:", Decimal("3.14159").quantize(Decimal("0.000")))


"""Генератори"""
"""Один із способів створити генератор у Python — це створити особливу функцію з декількома точками входу. Для цього використовується ключове слово yield.

Оператор yield поводиться схожим чином з return, повертає управління потоком виконання програмою з тіла функції. Але, на відміну від return, yield при наступному зверненні не розпочинає виконання функції з початку, а продовжує з місця зупинки функції.
"""

# def my_generator():
#     yield 1
#     yield 2
#     yield 3

# gen = my_generator()

# # Використання next()
# print(next(gen))  # Виведе 1
# print(next(gen))  # Виведе 2
# print(next(gen))  # Виведе 3

"""Після того, як генератор повернув усі свої значення, якщо ми виконаємо виклик next(gen), то виникне виняток StopIteration, оскільки більше немає значень для повернення. Цей виняток є сигналом того, що ітерація завершилася.

Щоб кожен раз не використовувати try except для контролю винятку StopIteration найчастіше генератори використовуються безпосередньо в циклах for ..., який буде це виконувати за нас:"""

# def count_down(start):
#     while start > 0:
#         yield start
#         start -= 1

# for number in count_down(5):
#     print(number)


# --- Example 2
def read_lines(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        for line in file:
            yield line.strip()

for line in read_lines("my_file.txt"):
    print(line)
# Перевага такого підходу в тому, що завдяки лінивій обробці, генератор читає рядки один за одним, не завантажуючи весь файл у пам'ять. Це особливо корисно при роботі з великими файлами.