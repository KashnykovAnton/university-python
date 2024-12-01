print("Hello world!")
# print(len("hello"))
# name = ["John", "Doe", "Bob", "Alice"]
# for i in name: print(i)
# float = 1.123456
# print(float)
# int = 7
# print(int)
# print(len(name))
# name = "John"
# print(name)
# print("Hello " + name)
# def greet(): return "Hello"
# print(greet(), "Bob")

# # Змініть вхідні дані на ціле число
# age = int(input("How old are you now? "))
# print(age)
# print("How old will you be next year?")
# print(age + 1)

# my_lucky_number = 7
# guess = int(input("Guess my lucky number! I think it is: "))
# while my_lucky_number != guess:
#      guess = int(input("Oops! Not it. Try again: "))
# print("Congrats! You guessed it.")

# max_number = max(100,2,3,4,5)
# print(max_number)

# txt = "Hello, welcome to my world."
# x = txt.find("welcome")
# print(x) 

# cars = ['Ford', 'BMW', 'Volvo']
# cars.sort()
# print(cars)

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# x = car.keys()
# print(x) 

# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
# x = thistuple.count(5)
# y = thistuple.index(8)
# print(x) 
# print(y)

# name = input("Enter your name: ")
# phrase = f"This is {name}"
# print(phrase)

# side = int(input("Enter the side of the square: "))
# area = side * side
# print(f"The area of the square is {area}")

# TYPES
# a = 3
# b = a
# print(id(a), id(b))
# a = 11
# print(id(a), id(b))
# print(a)
# print(b)
# print(type(a))
# c = 3.00
# print(type(c))
# d = True
# print(type(d))
# c = None
# print(type(c))

# LISTS
# my_list = list()
# my_list.append("Bob")
# print(my_list)
# my_list.append("Alice")
# print(my_list)
# my_list.remove("Bob")
# print(my_list)
# my_list.insert(0, "Bob")
# print(my_list)
# my_list.append("John")
# print(my_list)
# # my_list.pop()
# # print(my_list)
# # my_list.pop(0)
# # print(my_list)
# my_list[0] = "Dilan"
# print(my_list)
# name = my_list.pop()
# print(name)
# my_numbers = [1, 2, 3]
# my_list.extend(my_numbers)
# print(my_list)
# my_index = my_list.index(2)
# print(my_index)
# print(len(my_list))
# fruits_list = ["banana", "apple", "orange", "cherry", "melon", "kiwi", "mango", "strawberry"]
# fruits_list.sort()
# print(fruits_list)
# sorted_fruits_list = sorted(fruits_list, key=len, reverse=True)
# print(sorted_fruits_list)
# fruits_list.reverse()
# print(fruits_list)


# DICTINARIES
# my_dict = {}
# my_dict["name"] = "Bob"
# my_dict["age"] = 25
# print(my_dict)
# my_dict["friends"] = ["Alice", "John"]
# # del my_dict["name"]
# print("name" in my_dict)
# print("student" in my_dict)
# age = my_dict.get("age")
# print(age)
# print(my_dict)
# my_dict.update({"student": True, "age": 23})
# print(my_dict)
# gender = my_dict.get("gender", "unknown")
# print(gender)

# SETS
# my_set = set({1,2,3,4,5,6})
# my_set.add(5)
# my_set.remove(6)
# # my_set.remove(8) # KeyError
# my_set.discard(8)
# my_set.discard(5)
# print(my_set)

# example_list = [1,2,3,1,2,3]
# example_set = set(example_list)
# print(example_set)
# updated_list = list(example_set)
# print(updated_list)

# OPERATIONS WITH SETS
# a = {1,2,3}
# # a = [1,2,3] # TypeError
# b = {3,4,5}
# print(a.union(b))
# print(a | b) # the same as a.union(b)
# print(a.intersection(b))
# print(a & b) # the same as a.intersection(b)
# print(a.difference(b))
# print(a - b) # the same as a.difference(b)
# print(a.symmetric_difference(b))
# print(a ^ b) # the same as a.symmetric_difference(b)
# print(a.issubset(b))
# print(a.issuperset(b))
# print(a.isdisjoint(b))

# my_frozenset_a = frozenset([1, 2, 3, 4, 5])
# my_frozenset_b = frozenset([4, 5, 6, 7, 8])
# # my_frozenset.add(6) # AttributeError
# print(my_frozenset_a | my_frozenset_b)
# print(my_frozenset_a & my_frozenset_b)
# print(my_frozenset_a - my_frozenset_b)
# print(my_frozenset_a ^ my_frozenset_b)

# TUPLES
# my_tuple = tuple()
# my_tuple = ("Bob", "Alice")
# my_number_tuple = (1, 2, 3)
# my_mixed_tuple = (1, "Alice", True) 
# print(my_tuple) 
# print(my_number_tuple)
# print(my_mixed_tuple)
# tuple_with_one_element = ("Bob",) # tuple - with one element
# print(tuple_with_one_element)
# defenition_tuple = ("Bob") # not a tuple!!!!
# print(defenition_tuple)
# tuple_with_no_brackets = "Bob", "Alice" # tuple - without brackets
# print(tuple_with_no_brackets)

# STRINGS
# my_string = "Hello, World!"
# print(my_string[0])
# print(my_string[8])
# # my_string[1] = "a" # TypeError
# my_string.upper() # not change the original string !!! nothing happens
# print(my_string)
# print(my_string.upper())
# print(my_string.lower())
# print(my_string.startswith("Hello"))
# my_file = "file.txt"
# print(my_file.endswith("txt")) # Usefull for checking file extensions
# print(my_string.replace("H", "J"))

# new_string = "lorem ipsum dolor sit amet"
# new_string.capitalize()
# print(new_string) # nothing happens
# print(new_string.capitalize())
# print(new_string.title())

# print("123".isdigit())
# print("hello".isalpha())
# print(" ".isspace())

# # Просте форматування рядка
# name = 'John'
# print('Hello, {}!'.format(name))

# # Форматування з декількома аргументами
# age = 25
# print('Hello, {}. You are {} years old.'.format(name, age))

# # Використання іменованих аргументів
# print('Hello, {name}. You are {age} years old.'.format(name='Jane', age=30))

# # Використання індексів для вказівки порядку аргументів
# print('Hello, {1}. You are {0} years old.'.format(age, name))

# # SLICES 
# # [початок:кінець:крок]
# s = "Hello, World!"
# first_five = s[:5]
# print(first_five)  # Виведе 'Hello'
# last_five = s[-5:]
# print(last_five)  # Виведе 'orld!'

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# odd_numbers = numbers[0:10:2]
# odd_numbers_another_syntax = numbers[::2] # the same as above !!!
# print(odd_numbers)
# print(odd_numbers_another_syntax)
# even_numbers = numbers[1:10:2]
# even_numbers_another_syntax = numbers[1::2] # the same as above !!!
# print(even_numbers)
# print(even_numbers_another_syntax)
# copy_of_numbers = numbers[:] # copy of the list 
# print(copy_of_numbers)
# print(numbers == copy_of_numbers)

# fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# reverse_fruits = fruits[::-1] # reverse the list
# print(reverse_fruits)

# string = "Hello, World!"
# reverse_string = string[::-1] # reverse the string
# print(reverse_string)