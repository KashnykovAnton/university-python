from collections import UserDict
from colorama import Fore, init
from datetime import datetime, timedelta


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

class Birthday(Field):
    def __init__(self, value):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError(Fore.CYAN + "Invalid date format. Use DD.MM.YYYY")

class Record:
    def __init__(self, name):
        try:
            self.name = Name(name)
        except ValueError as e:
            print(Fore.RED + f"An error occurred while adding name: {str(e)}")
            return
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        try:
            existing_phone = list(filter(lambda p: p.value == phone, self.phones))
            if existing_phone:
                return print(Fore.CYAN + f"Phone number {phone} already exists.")
            self.phones.append(Phone(phone))
            print(Fore.GREEN + f"Phone number {phone} added successfully.")
        except ValueError as e:
            print(Fore.RED + f"An error occurred while adding phone: {e}")

    def remove_phone(self, phone):
        try:
            original_length = len(self.phones)
            self.phones = list(filter(lambda p: p.value != phone, self.phones))
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
            if filtered_phones:
                print(Fore.GREEN + f"Phone number {phone} found.")
                return filtered_phones[0]
            return print(Fore.CYAN + f"Phone number {phone} not found.")
        except ValueError as e:
            print(Fore.RED + f"An error occurred while finding phone: {e}")
    
    def add_birthday(self, birthday):
        try:
            if self.birthday is not None:
                self.birthday = Birthday(birthday)
                print(Fore.YELLOW + f"Birthday updated to {birthday} successfully.")
            else:
                self.birthday = Birthday(birthday)
                print(Fore.GREEN + f"Birthday {birthday} added successfully.")
        except ValueError as e:
            print(Fore.RED + f"An error occurred while adding birthday: {e}")

    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        return Fore.GREEN + f"Contact name: {self.name.value}, phones: {phones}, birthday: {self.birthday.value}"
    
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
        if name in self.data:
            del self.data[name]
            return print(Fore.GREEN + f"Record for '{name}' has been successfully deleted.")
        return print(Fore.RED + f"Cannot delete: No record found for '{name}'.")

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        upcoming_birthdays = []

        for name, record in self.data.items():
            if record.birthday:
                birthday_this_year = record.birthday.value.replace(year=today.year)
                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(year=today.year + 1)

                difference = (birthday_this_year - today).days
                if difference <= 7:
                    weekday = birthday_this_year.weekday()
                    if weekday == 5:  # If Saturday
                        birthday_this_year += timedelta(days=2)
                    elif weekday == 6:  # If Sunday
                        birthday_this_year += timedelta(days=1)

                    upcoming_birthdays.append({
                        "name": name,
                        "congratulation_date": birthday_this_year.strftime("%Y.%m.%d")
                    })

        return upcoming_birthdays

# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890") 
john_record.add_phone("5555555555")
john_record.add_phone("98765432100") # Виведення: Phone number 98765432100 must be exactly 10 digits.
john_record.add_birthday("02.01.1990")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення запису для Bob
bob_record = Record("Bob")
bob_record.add_phone("7776665550") 
bob_record.add_birthday("31.12.1995")

# Додавання запису John до адресної книги
book.add_record(bob_record)

# Створення запису для Ann
ann_record = Record("Ann")
ann_record.add_phone("9998887770") 
ann_record.add_birthday("15.01.1993")
ann_record.add_birthday("17.01.1993")



# Додавання запису John до адресної книги
book.add_record(ann_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
jane_record.add_phone("9876543210") # Виведення: Phone number 9876543210 already exists.
jane_record.add_birthday("15.12.1985")
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

upcoming = book.get_upcoming_birthdays()
print("Список привітань на цьому тижні:", upcoming)