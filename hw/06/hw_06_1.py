from collections import UserDict
from colorama import Fore, init

init(autoreset=True)

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        if not value or not value.strip():
            raise ValueError(Fore.CYAN + "Name cannot be empty.")


class Phone(Field):
    def __init__(self, value):
        super().__init__(value)
        if not value.isdigit() or len(value) != 10:
            raise ValueError(Fore.CYAN + "Phone number must be exactly 10 digits.")


class Record:
    def __init__(self, name):
        try:
            self.name = Name(name)
        except ValueError as e:
            print(Fore.RED + f"An error occurred while adding name: {str(e)}")
            return
        self.phones = []

    def add_phone(self, phone):
        try:
            existing_phone = list(filter(lambda p: p.value == phone, self.phones))
            # existing_phone = [p for p in self.phones if p.value == phone] # alternative solution with list comprehension
            if existing_phone:
                return print(Fore.CYAN + f"Phone number {phone} already exists.")
            self.phones.append(Phone(phone))  # This will raise an exception if invalid
            print(Fore.GREEN + f"Phone number {phone} added successfully.")
        except ValueError as e:
            print(Fore.RED + f"An error occurred while adding phone: {e}")

    def remove_phone(self, phone):
        try:
            original_length = len(self.phones)
            self.phones = list(filter(lambda p: p.value != phone, self.phones))
            # self.phones = [p for p in self.phones if p.value != phone] # alternative solution with list comprehension
            if len(self.phones) < original_length:
                return print(Fore.GREEN + f"Phone number {phone} was successfully removed.")
            return print(Fore.CYAN + f"Phone number {phone} not found.")
        except ValueError as e:
            print(Fore.RED + f"An error occurred while removing phone: {e}")

    def edit_phone(self, old_phone, new_phone):
        try: 
            if old_phone == new_phone:
                return print(Fore.YELLOW + "New phone number should be different from the old one.")
            
            if new_phone in [p.value for p in self.phones]:
                return print(Fore.YELLOW + "New phone number is already in the list.")
            
            for idx, phone in enumerate(self.phones):
                if phone.value == old_phone:
                    self.phones[idx] = Phone(new_phone)
                    return print(Fore.GREEN + f"Phone number {old_phone} successfully changed to {new_phone}.")
            
            return print(Fore.RED + f"Phone number {old_phone} not found.")
        except ValueError as e:
            print(Fore.RED + f"An error occurred while editing phone: {e}")

    def find_phone(self, phone):
        try:
            filtered_phones = list(filter(lambda p: p.value == phone, self.phones))
            # filtered_phones = [p for p in self.phones if p.value == phone] # alternative solution with list comprehension
            if filtered_phones:
                print(Fore.GREEN + f"Phone number {phone} found.")
                return filtered_phones[0]
            return print(Fore.CYAN + f"Phone number {phone} not found.")
        except ValueError as e:
            print(Fore.RED + f"An error occurred while finding phone: {e}")

    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        return Fore.GREEN + f"Contact name: {self.name.value}, phones: {phones}"
    
class AddressBook(UserDict):
    def add_record(self, record):
        if record.name.value in self.data:
            return print(Fore.RED + f"Record with name '{record.name.value}' already exists.")
        self.data[record.name.value] = record
        return print(Fore.GREEN + f"Record for '{record.name.value}' has been successfully added.")

    def find(self, name):
        record = self.data.get(name)
        if record:
            print(Fore.GREEN + f"Record for '{name}' found.")
            return record
        return print(Fore.RED + f"No record found for '{name}'.")

    def delete(self, name):
        try:
            if name in self.data:
                del self.data[name]
                return print(Fore.GREEN + f"Record for '{name}' has been successfully deleted.")
            return print(Fore.RED + f"Cannot delete: No record found for '{name}'.")
        except KeyError as e:
            print(Fore.RED + f"An error occurred while deleting record: {e}")


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890") 
john_record.add_phone("5555555555")
john_record.add_phone("98765432100") # Виведення: Phone number 98765432100 must be exactly 10 digits.


# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
jane_record.add_phone("9876543210") # Виведення: Phone number 9876543210 already exists.
book.add_record(jane_record)

# Спроба створити ше один запис з ім'ям Jane
jane_two_record = Record("Jane")
jane_two_record.add_phone("9876543210")
book.add_record(jane_two_record) # Виведення: Record with name 'Jane' already exists.

# Спроба створити запис з некорректним ім'ям
jane_two_record = Record("    ") # Виведення: Name cannot be empty.

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john_wrong = book.find("John1") # Виведення: No record found for 'John1'.
john = book.find("John")
john.edit_phone("1234567890", "1112223333")
john.edit_phone("5555555555", "5555555555") # Виведення: New phone number should be different from the old one.
john.edit_phone("5555555555", "1112223333") # Виведення: New phone number is already in the list.
john.edit_phone("7776665554", "9998887776") # Виведення: Phone number 7776665554 not found.

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555
found_phone = john.find_phone("7776665554") # Виведення: Phone number 7776665554 not found.

# Видалення запису Jane
book.delete("Jane")

# Виведення всіх записів у книзі після видалення
for name, record in book.data.items():
    print(record)