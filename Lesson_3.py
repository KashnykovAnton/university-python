"""First Example"""
# import datetime

# now = datetime.datetime.now()
# print(now)

"""Second Example"""
# from datetime import datetime

# current_datetime = datetime.now()

# print(current_datetime.year)
# print(current_datetime.month)
# print(current_datetime.day)
# print(current_datetime.hour)
# print(current_datetime.minute)
# print(current_datetime.second)
# print(current_datetime.microsecond)
# print(current_datetime.tzinfo)

"""Third Example"""
# current_datetime = datetime.now()
# print(current_datetime.date()) # prints the date
# print(current_datetime.time()) # prints the time

"""Combining Date and Time"""
# import datetime 

# # Створення об'єктів date і time
# date_part = datetime.date(2023, 12, 14)
# time_part = datetime.time(12, 30, 15)

# # Комбінування дати і часу в один об'єкт datetime
# combined_datetime = datetime.datetime.combine(date_part, time_part)

# print(combined_datetime)  # Виведе "2023-12-14 12:30:15"

"""Specific date"""
# import datetime

# # Створення об'єкта datetime з конкретною датою
# specific_date = datetime.datetime(year=2020, month=1, day=7, hour=14, minute=20)
# short_specific_date = datetime.datetime(2020, 1, 7, 14, 20) # Те ж саме, що і вище

# print(specific_date)  # Виведе "2020-01-07 00:00:00"
# print(short_specific_date)  # Виведе "2020-01-07 00:00:00"

"""Week day"""
# from datetime import datetime

# # Створення об'єкта datetime
# now = datetime.now()

# # Отримання номера дня тижня
# day_of_week = now.weekday()

# # Поверне число від 0 (понеділок) до 6 (неділя)
# print(f"Сьогодні: {day_of_week}")  

"""Comparison of dates"""
# from datetime import datetime

# # Створення двох об'єктів datetime
# datetime1 = datetime(2023, 3, 14, 12, 0)
# datetime2 = datetime(2023, 3, 15, 12, 0)

# # Порівняння дат
# print(datetime1 == datetime2)  # False, тому що дати не однакові
# print(datetime1 != datetime2)  # True, тому що дати різні
# print(datetime1 < datetime2)   # True, тому що datetime1 передує datetime2
# print(datetime1 > datetime2)   # False, тому що datetime1 не наступає за datetime2

"""timedelta()"""
# from datetime import datetime
# from datetime import timedelta

# # Створення об'єкта datetime
# delta = timedelta(
#     days=50,
#     seconds=27,
#     microseconds=10,
#     milliseconds=29000,
#     minutes=5,
#     hours=8,
#     weeks=2
# )
# print(delta)

# # Створення двох об'єктів datetime
# seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)

# difference = seventh_day_2020 - seventh_day_2019
# print(difference)  # 365 days, 0:00:00
# print(difference.total_seconds())  # 31536000.0

# # Створення дати у майбутньому від поточної дати
# now = datetime.now()
# future_date = now + timedelta(days=10)  # Додаємо 10 днів до поточної дати
# print(future_date)

# # Створення дати у минулому від конкретної дати
# seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
# four_weeks_interval = timedelta(weeks=4)

# print(seventh_day_2020 + four_weeks_interval)  # 2020-02-04 14:00:00
# print(seventh_day_2020 - four_weeks_interval)  # 2019-12-10 14:00:00

"""toordinal()"""
# from datetime import datetime

# # Створення об'єкта datetime
# date = datetime(year=2023, month=12, day=18)
# current_date = datetime.now()

# # Отримання порядкового номера
# ordinal_number = date.toordinal()
# current_ordinal_number = current_date.toordinal()
# print(f"Порядковий номер дати {date} становить {ordinal_number}")
# print(f"Порядковий номер поточної дати {current_date} становить {current_ordinal_number}")

"""Timestamp"""
# from datetime import datetime

# # From datetime to timestamp  
# # Поточний час
# now = datetime.now()

# # Конвертація datetime в timestamp
# timestamp = datetime.timestamp(now)
# print(timestamp)  # Виведе timestamp поточного часу

# # From timestamp to datetime
# # Припустимо, є timestamp
# timestamp_mark = 1617183600

# # Конвертація timestamp назад у datetime
# dt_object = datetime.fromtimestamp(timestamp_mark)
# print(dt_object)  # Виведе відповідний datetime

"""Strftime()"""
"""
datetime_object.strftime(format)

Де datetime_object - це об'єкт datetime, а format - рядок формату, який визначає, як дата та час повинні бути представлені.

Кожен код у рядку формату починається з символу % і представляє певний компонент дати або часу. Ось деякі з найбільш використовуваних кодів:

    %Y - рік з чотирма цифрами (наприклад, 2023).
    %y - рік з двома цифрами (наприклад, 23).
    %m - місяць як номер (наприклад, 03 для березня).
    %d - день місяця як номер (наприклад, 14).
    %H - година (24-годинний формат) (наприклад, 15).
    %I - година (12-годинний формат) (наприклад, 03).
    %M - хвилини (наприклад, 05).
    %S - секунди (наприклад, 09).
    %A - повна назва дня тижня (наприклад, Tuesday).
    %a - скорочена назва дня тижня (наприклад, Tue).
    %B - повна назва місяця (наприклад, March).
    %b або %h - скорочена назва місяця (наприклад, Mar).
    %p - AM або PM для 12-годинного формату.
"""

# from datetime import datetime

# now = datetime.now()

# # Форматування дати і часу
# formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
# print(formatted_date) # Виведе "2023-03-14 12:00:00"

# # Форматування лише дати
# formatted_date_only = now.strftime("%A, %d %B %Y")
# print(formatted_date_only) # Виведе "Tuesday, 14 March 2023"

# # Форматування лише часу
# formatted_time_only = now.strftime("%I:%M %p")
# print(formatted_time_only) # Виведе "12:00 PM"

# # Форматування лише дати
# formatted_date_only = now.strftime("%d.%m.%Y")
# print(formatted_date_only) # Виведе "14.03.2023"

"""strptime()"""
"""
Синтаксис методу strptime виглядає наступним чином:

datetime_object = datetime.strptime(string, format)

де:

    string - рядок, який містить дату та/або час.
    format - рядок формату, який вказує, як розібрати string.

Коди форматування для strptime такі ж, як і для strftime. Наприклад, %Y представляє рік із чотирма цифрами, %m - місяць у вигляді двоцифрового числа тощо.
"""
# from datetime import datetime

# # Припустимо, у нас є дата у вигляді рядка
# date_string = "2023.03.14"

# # Перетворення рядка в об'єкт datetime
# datetime_object = datetime.strptime(date_string, "%Y.%m.%d")
# print(datetime_object)  # Виведе об'єкт datetime, що відповідає вказаній даті та часу

"""ISO 8601"""
# from datetime import datetime

# # Поточна дата та час
# now = datetime.now()
# iso_date_string = "2023-03-14T12:39:29.992996"

# # Конвертація у формат ISO 8601
# iso_format = now.isoformat()
# print(iso_format)

# # Конвертація з ISO формату
# date_from_iso = datetime.fromisoformat(iso_date_string)
# print(date_from_iso)

# # Використання isoweekday() для отримання дня тижня
# day_of_week = now.isoweekday()

# print(f"Сьогодні: {day_of_week}")  # Поверне число від 1 до 7, що відповідає дню тижня

# # Отримання ISO календаря
# iso_calendar = now.isocalendar()

# print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")

"""Time zones"""
# from datetime import datetime, timezone

# local_now = datetime.now()
# utc_now = datetime.now(timezone.utc)

# print(local_now)
# print(utc_now)  # Виведе поточний час в UTC

"""Time"""
"""Метод time.time() повертає поточний час у секундах з 1 січня 1970 року (epoch time)."""
import time

# current_time = time.time()
# print(f"Поточний час: {current_time}")

# --- time.sleep(seconds) ---
# Метод time.sleep() призначений для затримки виконання програми на певну кількість секунд.

# print("Початок паузи")
# time.sleep(5)
# print("Кінець паузи")

# --- time.ctime([seconds]) ---
# current_time = time.time()
# print(f"Поточний час: {current_time}")

# readable_time = time.ctime(current_time)
# print(f"Читабельний час: {readable_time}")

# --- time.localtime([seconds]) ---
# current_time = time.time()
# print(f"Поточний час: {current_time}")

# local_time = time.localtime(current_time)
# print(f"Місцевий час: {local_time}") # Виведе об'єкт time.struct_time

"""
Об'єкт time.struct_time в Python є іменованим кортежем, який використовується для представлення часу. Кожен елемент кортежу має особливе значення, що представляє певний компонент дати та часу:

    tm_year - рік
    tm_mon - місяць від 1 до 12
    tm_mday - день місяця від 1 до 31
    tm_hour - години від 0 до 23
    tm_min - хвилини від 0 до 59
    tm_sec - секунди від 0 до 59
    tm_wday - день тижня від 0 до 6
    tm_yday - день року від 1 до 366
    tm_isdst - прапорець літнього часу. 0 означає, що літній час не діє, -1 - інформація відсутня, 1 - літній час діє
"""

# # --- time.mktime(time_struct) ---
# # Записуємо час на початку виконання
# start_time = time.perf_counter()

# # Виконуємо якусь операцію
# for _ in range(1_000_000):
#     pass  # Просто проходить цикл мільйон разів

# # Записуємо час після виконання операції
# end_time = time.perf_counter()

# # Розраховуємо та виводимо час виконання
# execution_time = end_time - start_time
# print(f"Час виконання: {execution_time} секунд")

"""RANDOM"""
import random

# random_number = random.random()
# random_number_2 = random.randint(1, 100)
# print(random_number)
# print(random_number_2)

# --- Cимулювати випадкове відсоткове заповнення:
# fill_percentage = random.random() * 100
# print(f"Заповнення: {fill_percentage:.2f}%")

# --- Симуляція пострілу по мішені, але необхідно вибрати випадковий номер від 1 до 10, та лише непарні числа:
# target = random.randrange(1, 11, 2)
# print(f"Ціль: {target}")

# --- Перемішування колоди карт:
# cards = ["Туз", "Король", "Дама", "Валет", "10", "9", "8", "7", "6"]
# random.shuffle(cards)
# print(f"Перемішана колода: {cards}")

# --- Вибір випадкового фрукта:
# fruits = ['apple', 'banana', 'orange']
# print(random.choice(fruits))
"""
Синтаксис методу random.choices() наступний:

random.choices(population, weights=None, cum_weights=None, k=1)

    - population - послідовність список, з якої має бути зроблений вибір.
    - weights - опціональний список, який вказує ймовірності (ваги) кожного елемента в списку population. Ці ваги визначають, наскільки ймовірно, що конкретний елемент буде обраний. Довжина списку weights має бути дорівнювати довжині списку population.
    - cum_weights - теж опціональний список кумулятивних ваг. Якщо він вказаний, то список weights ігнорується. Кумулятивна вага кожного елемента визначається як сума його ваги плюс ваги всіх попередніх елементів.
    - k: Кількість елементів для вибору. За замовчуванням k=1"""

# Приклад з вагами
# colors = ['червоний', 'зелений', 'синій']
# weights = [10, 1, 1]
# chosen_color = random.choices(colors, weights, k=1)
# print(chosen_color)  

"""
Якщо виникає необхідність вибрати N елементів зі списку і вони при цьому не повторювалися треба використати метод random.sample(population, k). Він повертає список довжиною k з унікальними елементами, вибраними випадково з population.
"""
# participants = ['Анна', 'Богдан', 'Віктор', 'Галина', 'Дмитро', 'Олена', 'Женя', 'Зорян', 'Ігор', 'Йосип']
# team = random.sample(participants, 4)
# print(f"Команда: {team}")

# --- random.uniform(a, b) ---
# price = random.uniform(50, 100)
# print(f"Випадкова ціна: {price:.2f}")


"""MATH"""
"""
Константи:
    math.pi - константа ππ (приблизно 3.14159...);
    math.e - константа ee, основа натуральних логарифмів (приблизно 2.71828...);
    math.tau - константа ττ, дорівнює 2π2π (приблизно 6.28318...);
    math.inf - позначення нескінченності;
    math.nan - позначення 'Not a Number' (не число);

Функції округлення чисел:
    math.ceil(x) - виконує округлення дійсного числа x до найближчого більшого цілого числа;
    math.floor(x) - виконує округлення дійсного числа x до найближчого меншого цілого числа;
    math.trunc(x) - виконує обрізання дробової частини дійсного числа x, та повертає цілу частину числа;
    
Тригонометричні функції:
    math.sin(x) - синус x, де x в радіанах;
    math.cos(x) - косинус x;
    math.tan(x) - тангенс x;
    math.asin(x) - арксинус x;
    math.acos(x) - арккосинус x;
    math.atan(x) - арктангенс x;

Експоненційні та логарифмічні функції:
    math.exp(x) - число ee в ступені x;
    math.log(x[, base]) - Логарифм x за основою base. Якщо base не вказано, обчислюється натуральний логарифм;

Ступінь та корінь:
    math.pow(x, y) - x у ступені y;
    math.sqrt(x) - квадратний корінь з x;

Деякі інші функції:
    math.fabs(x) - модуль (абсолютне значення) x;
    math.factorial(x) - факторіал числа x;
    math.gcd(x, y) - найбільший спільний дільник для x та y;

"""

import math

number = 4.99
print(math.ceil(number))
print(math.floor(number))
print(math.trunc(number))

# Використання констант
print(math.pi)  # Виведе приблизне значення π

# Тригонометрія
angle = math.radians(60)  # Конвертація з градусів у радіани
print(math.sin(angle))  # Синус кута

# Корінь числа
print(math.sqrt(9))  # Квадратний корінь з 9

# Логарифми
print(math.log(10, 2))  # Логарифм 10 за основою 2

"""Функція math.isclose використовується для порівняння двох чисел з певною допустимою похибкою. Це корисно для порівняння дійсних чисел, де пряме порівняння може бути ненадійним."""

print(0.1 + 0.2 == 0.3)  # Це повертає False

r = math.isclose(0.1 + 0.2, 0.3)
print(r)  # Це поверне True 

