"""Серіалізація об'єктів в Python"""
"""Серіалізація об'єктів в Python — це процес перетворення структури даних або об'єкта в потік байтів для зберігання або передачі. """
"""Python надає декілька модулів для серіалізації, найпопулярнішими з яких є pickle і json.

    - вбудований пакет pickle дозволяє працювати з вбудованими типами (словники, списки, кортежі, рядки, множини та ін.) і навіть з нескладними класами;
    - формат JSON підтримується Python і з невеликими обмеженнями дозволяє працювати з рядками, числами, списками, кортежами та словниками."""

# ----- Серіалізація об'єктів Python за допомогою pickle -----
# --- Упакування у byte-рядки та розпакування із byte-рядків
import pickle

# Об'єкт для серіалізації
my_data = {"key": "value", "num": 42}

# Серіалізація об'єкта в байтовий рядок
serialized_data = pickle.dumps(my_data)
# Виведе байтовий рядок
print(serialized_data)  

# Десеріалізація об'єкта з байтового рядка
deserialized_data = pickle.loads(serialized_data)
# Виведе вихідний об'єкт Python
print(deserialized_data)


# --- Упакування у файл та розпакування з файлу
import pickle

# Об'єкт для серіалізації
my_data = {"key": "value", "num": 100}

# Серіалізація об'єкта в файл
with open("data.pickle", "wb") as file:
    pickle.dump(my_data, file)


# Десеріалізація об'єкта з файлу
with open('data.pickle', 'rb') as file:
    deserialized_data = pickle.load(file)

# Виведе вихідний об'єкт Python
print(deserialized_data)

# --- Робота з класами користувача
import pickle

class Human:
    def __init__(self, name):
        self.name = name

bob = Human("Bob")

# Серіалізація об'єкта класу Human
with open("instance.pickle", "wb") as file:
    pickle.dump(bob, file)

# Десеріалізація об'єкта класу Human
with open("instance.pickle", "rb") as file:
    loaded_instance = pickle.load(file)

print(loaded_instance.name)

# ----- Серіалізація об'єктів Python за допомогою JSON -----
# --- Упакування у byte-рядок та розпакування із byte-рядків
import json

some_data = {
    "key": "value",
    2: [1, 2, 3],
    "my_tuple": (5, 6),
    "my_dict": {"key": "value"},
}

json_string = json.dumps(some_data)
print(json_string)
unpacked_some_data = json.loads(json_string)
print(unpacked_some_data)

# --- Упакування у файл та розпакування з файлу
import json

# Python об'єкт (словник)
data = {"name": "Gupalo Vasyl", "age": 30, "isStudent": True}

# Серіалізація у файл
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f)

# Десеріалізація з файлу
with open("data.json", "r", encoding="utf-8") as f:
    data_from_file = json.load(f)
    print(data_from_file)

# --- Проблеми серіалізації об'єктів Python з ASCII-символами
import json

# Python об'єкт (словник)
data = {"name": "Гупало Василь", "age": 30, "isStudent": True}

# Серіалізація у файл
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)



# ----- Робота з таблицями CSV у Python -----
# --- Для читання даних з CSV файлу можна використовувати функцію csv.reader, що повертає об'єкт, який ітерує по рядках файлу.
import csv

# Відкриваємо CSV файл
with open("data.csv", newline="", encoding="utf-8") as csvfile:
    # Створюємо об'єкт reader
    reader = csv.reader(csvfile, delimiter=",")
    # Проходимося по кожному рядку у файлі
    for row in reader:
        print(", ".join(row))

# --- Для запису даних у CSV файл можна використати функцію csv.writer. Вона дозволяє легко записувати рядки даних у файл.
# За допомогою writer.writerows(rows) можна записати кілька рядків одразу. Якщо потрібно записати один рядок, можна використати writer.writerow(row).
import csv

# Дані для запису
rows = [
    ["name", "age", "specialty"],
    ["Василь Гупало", 30, "Математика"],
    ["Марія Петренко", 22, "Фізика"],
    ["Олександр Коваленко", 20, "Інформатика"],
]

# Відкриваємо файл для запису
with open("data.csv", "w", newline="", encoding="utf-8") as csvfile:
    # Створюємо об'єкт writer
    writer = csv.writer(csvfile, delimiter=",")
    # Записуємо рядки даних
    writer.writerows(rows)

# --- Використання DictReader і DictWriter полегшує доступ до полів за їхніми назвами та автоматизує процес запису заголовків стовпців.
import csv

# Запис у CSV файл зі словників
with open("students.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["name", "age", "specialty"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({"name": "Олег Олегов", "age": 23, "specialty": "Історія"})
    writer.writerow({"name": "Анна Сергіївна", "age": 22, "specialty": "Біологія"})

# Читання з CSV файлу в словники
with open("students.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row["name"], row["age"], row["specialty"])


# --- Example two
import csv

FILENAME = "users.csv"

users = [
    {"name": "Микола", "age": 22, "gender": "male"},
    {"name": "Марія", "age": 22, "gender": "female"},
    {"name": "Назар", "age": 22, "gender": "male"},
]

with open(FILENAME, "w", encoding="utf-8", newline="") as f:
    columns = users[0].keys()
    writer = csv.DictWriter(f, delimiter=",", fieldnames=columns)
    writer.writeheader()
    for row in users:
        writer.writerow(row)

with open(FILENAME, "r", encoding="utf-8", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        print(row)





"""Autochecks"""
# Task 1
"""
Є список, кожен елемент якого є словником з контактами користувача наступного виду:

    {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}

Словник містить ім'я користувача name, його email, телефонний номер phone та властивість favorite - обраний контакт чи ні.

Розробіть дві функції для серіалізації та десеріалізації списку контактів за допомогою пакета pickle та зберігання отриманих даних у бінарному файлі.

Перша функція write_contacts_to_file приймає два параметри: filename - ім'я файлу, contacts - список контактів. Вона зберігає вказаний список у файл, використовуючи метод dump пакету pickle.

Друга функція read_contacts_from_file читає та повертає зазначений список contacts з файлу filename, використовуючи метод load пакету pickle.
"""
# Solution
import pickle


def write_contacts_to_file(filename, contacts):
    with open(filename, 'wb') as file:
        pickle.dump(contacts, file)
    print(f"Contacts have been successfully written to {filename}.")

def read_contacts_from_file(filename):
    with open(filename, 'rb') as file:
        contacts = pickle.load(file)
    print(f"Contacts have been successfully read from {filename}.")
    return contacts


# Task 2
"""
Є список, кожен елемент якого є словником з контактами користувача наступного виду:

{
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}

Словник містить ім'я користувача name, його email, телефонний номер phone та властивість favorite - обраний контакт чи ні.

Розробіть дві функції для серіалізації та десеріалізації списку контактів за допомогою пакету json та зберігання отриманих даних у текстовому файлі.

Перша функція write_contacts_to_file приймає два параметри: filename - ім'я файлу, contacts - список контактів. Вона зберігає вказаний список у файл, використовуючи метод dump пакету json.

Структура json файлу має бути такою:

{
  "contacts": [
    {
      "name": "Allen Raymond",
      "email": "nulla.ante@vestibul.co.uk",
      "phone": "(992) 914-3792",
      "favorite": false
    },
    ...
  ]
}

Тобто список контактів повинен зберігатися за ключем "contacts", а не просто зберегти список у файл.

Друга функція read_contacts_from_file читає та повертає зазначений список contacts з файлу filename, збереженого раніше функцією write_contacts_to_file, використовуючи метод load пакету json.
"""

# Solution
import json


def write_contacts_to_file(filename, contacts):
    data = {"contacts": contacts}
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    print(f"Contacts have been successfully written to {filename}.")
        


def read_contacts_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    print(f"Contacts have been successfully read from {filename}.")
    return data.get("contacts", [])


# Task 3
"""
Є список, кожен елемент якого є словником з контактами користувача наступного виду:

    {
    "name": "Allen Raymond",
    "email": "nulla.ante@vestibul.co.uk",
    "phone": "(992) 914-3792",
    "favorite": False,
}

Словник містить ім'я користувача name, його email, телефонний номер phone та властивість favorite - обраний контакт чи ні.

Розробіть дві функції для серіалізації та десеріалізації списку контактів за допомогою пакету csv та зберігання отриманих даних у текстовому файлі.

Перша функція write_contacts_to_file приймає два параметри: filename - ім'я файлу, contacts - список контактів. Вона зберігає вказаний список у файлі формату csv.

Структура csv файлу має бути такою:

name,email,phone,favorite
Allen Raymond,nulla.ante@vestibul.co.uk,(992) 914-3792,False
Chaim Lewis,dui.in@egetlacus.ca,(294) 840-6685,False
Kennedy Lane,mattis.Cras@nonenimMauris.net,(542) 451-7038,True
Wylie Pope,est@utquamvel.net,(692) 802-2949,False
Cyrus Jackson,nibh@semsempererat.com,(501) 472-5218,True

Зверніть увагу, першим рядком у файлі йдуть заголовки – це назви ключів.

Друга функція read_contacts_from_file читає, виконує перетворення даних та повертає вказаний список contacts із файлу filename, збереженого раніше функцією write_contacts_to_file.

Примітка: При читанні файлу csv ми отримуємо властивість словника favorite у вигляді рядка, тобто. наприклад favorite='False' . Необхідно його привести до логічного виразу назад, щоб стало favorite=False.
"""

# Solution
import csv

def write_contacts_to_file(filename, contacts):
    with open(filename, "w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "email", "phone", "favorite"])
        writer.writeheader()
        writer.writerows(contacts)
    print(f"Contacts have been successfully written to {filename}.")

def read_contacts_from_file(filename):
    contacts = []
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["favorite"] = row["favorite"].lower() == "true"
            contacts.append(row)
    print(f"Contacts have been successfully read from {filename}.")
    return contacts

# Task 4
"""
Приклад створення екземпляра класу:

    Person(
    "Allen Raymond",
    "nulla.ante@vestibul.co.uk",
    "(992) 914-3792",
    False,
)

Розробіть клас Contacts. Він повинен ініціалізувати через конструктор дві властивості: filename - ім'я файлу для пакування об'єкта класу Contacts, contacts - список контактів, екземплярів класу Person.

Приклад створення екземпляра класу:

contacts = [
    Person(
        "Allen Raymond",
        "nulla.ante@vestibul.co.uk",
        "(992) 914-3792",
        False,
    ),
    Person(
        "Chaim Lewis",
        "dui.in@egetlacus.ca",
        "(294) 840-6685",
        False,
    ),
]

persons = Contacts("user_class.dat", contacts)

Розробіть два методи для серіалізації та десеріалізації екземпляра класу Contacts за допомогою пакету pickle та зберігання даних у бінарному файлі.

Перший метод save_to_file зберігає екземпляр класу Contacts у файл, використовуючи метод dump пакету pickle. Ім'я файлу зберігається в атрибуті filename.

Другий метод read_from_file читає та повертає екземпляр класу Contacts з файлу filename, використовуючи метод load пакету pickle.

Приклад роботи:

persons = Contacts("user_class.dat", contacts)
persons.save_to_file()
person_from_file = persons.read_from_file()
print(persons == person_from_file)  # False
print(persons.contacts[0] == person_from_file.contacts[0])  # False
print(persons.contacts[0].name == person_from_file.contacts[0].name)  # True
print(persons.contacts[0].email == person_from_file.contacts[0].email)  # True
print(persons.contacts[0].phone == person_from_file.contacts[0].phone)  # True
"""

# Solution
import pickle


class Person:
    def __init__(self, name: str, email: str, phone: str, favorite: bool):
        self.name = name
        self.email = email
        self.phone = phone
        self.favorite = favorite

    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        return (
            self.name == other.name and
            self.email == other.email and
            self.phone == other.phone and
            self.favorite == other.favorite
        )
        

class Contacts:
    def __init__(self, filename: str, contacts: list[Person] = None):
        if contacts is None:
            contacts = []
        self.filename = filename
        self.contacts = contacts

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            return pickle.load(file)