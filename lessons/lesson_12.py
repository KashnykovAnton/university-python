"""Управління порядком серіалізації та копіювання об'єктів"""
"""Не всі об'єкти Python можна серіалізувати. Наприклад, не можна серіалізувати файловий дескриптор або системний ресурс. Тоді, що робити, коли є клас, об'єкт який треба запакувати, використовуючи pickle, але у нього є атрибути, що не серіалізуються? У такій ситуації можна скористатися магічними методами, які управляють серіалізацією та десеріалізацією за допомогою pickle.

Методи __getstate__ і __setstate__ в Python дозволяють нам контролювати, як об'єкт повинен бути серіалізований та десеріалізований модулем pickle."""

import pickle

class Robot:
    def __init__(self, name, battery_life):
        self.name = name
        self.battery_life = battery_life
        # Цей атрибут ми не збираємось серіалізувати
        self.is_active = False  

    def __getstate__(self):
        state = self.__dict__          #!!!!! self.__dict__ - це спеціальний атрибут об'єкта, що містить словник з усіма атрибутами, які належать до цього об'єкта
        # Видаляємо is_active з серіалізованого стану
        del state['is_active']
        return state

    def __setstate__(self, state):
        # Відновлюємо об'єкт при десеріалізації
        self.__dict__.update(state)
        # Задаємо значення is_active за замовчуванням
        self.is_active = False  

# Створення об'єкта Robot
robot = Robot("Robo1", 100)

# Серіалізація об'єкта
serialized_robot = pickle.dumps(robot)

# Десеріалізація об'єкта
deserialized_robot = pickle.loads(serialized_robot)

print(deserialized_robot.__dict__)



# --- One more Example - more clear
class Example:
    def __init__(self, name, age):
        self.name = name
        self.age = age

obj = Example("Gupalo Vasyl", 30)
print(obj.__dict__) # {'name': 'Gupalo Vasyl', 'age': 30}

# Ми можемо динамічно додавати, видаляти або змінювати атрибути:
obj.__dict__['city'] = 'Poltava'  # Додавання нового атрибута
print(obj.city)  # Виведення: Poltava

del obj.__dict__['age']  # Видалення атрибута age
print(obj.__dict__)  # Виведення: {'name': 'Gupalo Vasyl', 'city': 'Poltava'}



# ---- Example with file
# При намаганні серіалізувати екземпляр класу Reader за допомогою pickle, виникає помилка, оскільки файловий дескриптор self.fh не може бути серіалізованим. Вона виникає тому, що файлові дескриптори не підлягають серіалізації pickle через їх залежність від зовнішніх системних ресурсів, які pickle не може зберегти та відновити.
# Щоб уникнути цієї помилки, ми можемо використати магічні методи __getstate__ і __setstate__ для управління серіалізації та десеріалізацією об'єкта Reader:

# import pickle

# class Reader:
#     def __init__(self, filename):
#         self.filename = filename
#         self.fh = open(self.filename, "r", encoding="utf-8")

#     def close(self):
#         self.fh.close()

#     def read(self):
#         data = self.fh.read()
#         return data

#     def __getstate__(self):
#         attributes = {**self.__dict__, "fh": None}
#         return attributes

#     def __setstate__(self, state):
#         # Відновлюємо стан об'єкта
#         self.__dict__ = state
#         self.fh = open(state["filename"], "r", encoding="utf-8")

# if __name__ == "__main__":
#     reader = Reader("data.txt")
#     data = reader.read()
#     print(data)
#     reader.close()

#     # Приклад серіалізації об'єкта Reader
#     with open("reader.pkl", "wb") as f:
#         pickle.dump(reader, f)

#     # Приклад десеріалізації об'єкта Reader
#     with open("reader.pkl", "rb") as f:
#         loaded_reader = pickle.load(f)
#         print(loaded_reader.read())
#         loaded_reader.close()



"""Створення копій об'єктів в Python"""
"""Створення копій об'єктів у Python може виявитися нетривіальним завданням, залежно від того, чи потрібна вам поверхнева (shallow) або глибока (deep) копія, а також від складності структури даних об'єкта."""
# --- Example with object copy problem
my_list = [1, 2, 3]
copy_list = my_list
copy_list.append(4)
print(my_list)
# Виходить, що copy_list — це просто ще одне ім'я для того самого списку my_list і, змінюючи copy_list, ми змінюємо й my_list. Це неочевидно і може збивати з пантелику.

# --- Example with solving object copy problem
my_list = [1, 2, 3]

def square_list(x: list):
    return [el**2 for el in x]

new_list = square_list(my_list)
print(new_list)
print(my_list)

# --- Для списків та словників можна скористатися явним копіюванням:
my_list = [1, 2, 3]
copy_list = my_list[:]
copy_list.append(4)
print(my_list, copy_list)

my_dict = {1: "a"}
copy_dict = {**my_dict}
copy_dict["new_key"] = "new_value"
print(my_dict, copy_dict)



"""Створення поверхневих копій об'єктів Python"""
"""Щоб створити "поверхневу" копію об'єкта, у пакеті copy є функція copy. Ця функція створює новий об'єкт такого самого типу і потім створює посилання на увесь вміст старого об'єкта в новий. Такий механізм досить хороший для роботи з об'єктами, де вже на першому рівні вкладеності немає змінних об'єктів, і він працює досить швидко."""
import copy

my_list = [1, 2, {"name": "Gupalo Vasyl"}]
copy_list = copy.copy(my_list)
copy_list.append(4)
print(my_list) # [1, 2, {'name': 'Gupalo Vasyl'}]
print(copy_list) # [1, 2, {'name': 'Gupalo Vasyl'}, 4]

# --- One more example
import copy

my_list = [1, 2, {"name": "Gupalo Vasyl"}]
copy_list = copy.copy(my_list)
copy_list[2]["age"] = 30
print(my_list) # [1, 2, {'name': 'Gupalo Vasyl', 'age': 30}]
print(copy_list) # [1, 2, {'name': 'Gupalo Vasyl', 'age': 30}]

# ☝ Поверхнева копія створює новий об'єкт, але не копіює вкладені об'єкти. Замість цього, вона копіює лише посилання на вкладені об'єкти. Це означає, що якщо ви змінюєте вкладені об'єкти в оригіналі, ці зміни також відобразяться у поверхневій копії.



"""Створення глибоких копій об'єктів Python"""
"""Глибока копія створює новий об'єкт та рекурсивно копіює всі вкладені об'єкти. В результаті, ви отримуєте повністю незалежну копію оригінального об'єкта.
Для створення глибокої копії використовуйте метод deepcopy() модуля copy. Ця функція рекурсивно створює нові об'єкти."""

import copy

my_list = [1, 2, {"name": "Gupalo Vasyl"}]
copy_list = copy.deepcopy(my_list)
copy_list[2]["age"] = 30
print(my_list) # [1, 2, {'name': 'Gupalo Vasyl'}]
print(copy_list) # [1, 2, {'name': 'Gupalo Vasyl', 'age': 30}]


"""Управління порядком копіювання об'єктів Python"""
"""Щоб створити об'єкт, який буде коректно оброблятися функціями copy та deepcopy, заданий клас повинен реалізувати два магічних методи: __copy__ та __deepcopy__ для поверхневого та глибокого копіювання відповідно."""

# --- Example SIMPLE
import copy

class MyClass:
    def __init__(self, value):
        self.value = value

    def __copy__(self):
        print("Викликано __copy__")
        return MyClass(self.value)

    def __deepcopy__(self, memo=None):
        print("Викликано __deepcopy__")
        return MyClass(copy.deepcopy(self.value, memo))

# Поверхневе копіювання
obj = MyClass(5)
obj_copy = copy.copy(obj)
obj_copy.value = 10

# Глибоке копіювання
obj_deepcopy = copy.deepcopy(obj)
obj_deepcopy.value = 20
print(obj.value, obj_copy.value, obj_deepcopy.value)

# --- Example with more complex object
import copy

class SimpleObject:
    def __init__(self, greeting: str):
        self.greeting = greeting

class ComplexObject:
    def __init__(self, value: int, nested_obj: SimpleObject):
        self.value = value
        self.nested_obj = nested_obj

    def __copy__(self):
        print("Викликано __copy__ для ComplexObject")
        # Поверхневе копіювання не копіює вкладені об'єкти глибоко
        return ComplexObject(self.value, self.nested_obj)

    def __deepcopy__(self, memo=None):
        print("Викликано __deepcopy__ для ComplexObject")
        # Глибоке копіювання копіює вкладені об'єкти
        return ComplexObject(
            copy.deepcopy(self.value, memo), copy.deepcopy(self.nested_obj, memo)
        )

nested_obj = SimpleObject("Привіт")
complex_obj = ComplexObject(5, nested_obj)

# Створюємо копію та глибоку копію
complex_obj_copy = copy.copy(complex_obj)
complex_obj_deepcopy = copy.deepcopy(complex_obj)

# Змінюємо значення вкладеного об'єкту nested_obj
nested_obj.greeting = "Hello"

# Дивимось зміни у об'єктах
print(f"Copy object: {complex_obj_copy.nested_obj.greeting}")
print(f"Deepcopy object: {complex_obj_deepcopy.nested_obj.greeting}")


# !!!! lib for serialization - pydantic !!!
