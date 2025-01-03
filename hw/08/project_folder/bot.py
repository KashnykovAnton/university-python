from colorama import Fore, init
from datetime import datetime
from collections import UserDict
from .address_book import AddressBook
from .record import Record
from .fields import *

init(autoreset=True)

class Bot:
    def __init__(self):
        self.address_book = AddressBook()

    def input_error(func):
        def inner(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except (KeyError, ValueError, IndexError) as e:
                return Fore.RED + f"Error: {str(e)}"
        return inner

    def parse_input(self, user_input):
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, args

    @input_error
    def add_contact(self, args):
        name, phone = args
        contact_phone = Phone(phone)
        record = self.address_book.find(name)
        if isinstance(record, str):
            print(record)
            record = None
        message = "updated"
        if record is None:
            record = Record(name)
            self.address_book.add_record(record)
            message = "added"
        if contact_phone:
            record.add_phone(contact_phone)    
        return Fore.GREEN + f"Contact {name} {message} successfully."

    @input_error
    def change_contact(self, args):
        name, old_phone, new_phone = args
        record = self.address_book.find(name)
        if isinstance(record, str):
            print(record)
            record = None
        if record:
            return record.edit_phone(old_phone, new_phone)
        return Fore.RED + "Contact not found."

    @input_error
    def show_phone(self, args):
        name = args[0]
        record = self.address_book.find(name)
        if isinstance(record, str):
            print(record)
            record = None
        if record:
            return record.show_phones()
        return Fore.RED + "Contact not found."

    def show_all(self, args=None):
        if self.address_book:
            result = Fore.CYAN + "All contacts:\n"
            for record in self.address_book.values():
                result += Fore.YELLOW + str(record) + "\n"
            return result.strip()
        return Fore.RED + "No contacts found."

    @input_error
    def add_birthday(self, args):
        name, birthday = args
        contact_birthday = Birthday(birthday)
        record = self.address_book.find(name)
        if isinstance(record, str):
            print(record)
            record = None
        if record:
            return record.add_birthday(contact_birthday)
        return Fore.RED + "Contact not found."

    @input_error
    def show_contact_birthday(self, args):
        name = args[0]
        record = self.address_book.find(name)
        if isinstance(record, str):
            print(record)
            record = None
        if record:
            return record.show_birthday()
        return Fore.RED + "Contact not found."

    @input_error
    def show_birthdays(self, args):
        upcoming_birthdays = self.address_book.get_upcoming_birthdays()
        if upcoming_birthdays:
            result = Fore.CYAN + "Upcoming birthdays:\n"
            for item in upcoming_birthdays:
                result += Fore.YELLOW + f"{item['name']}: {item['congratulation_date']}\n"
            return result.strip()
        return Fore.RED + "No upcoming birthdays."
    
    @input_error
    def remove_contact(self, args):
        name = args[0]
        return self.address_book.delete(name)
    
    @input_error
    def remove_phone(self, args):
        name, phone = args
        record = self.address_book.find(name)
        if isinstance(record, str):
            print(record)
            record = None
        if record:
            return record.remove_phone(phone)
        return Fore.RED + "Contact not found."

    def run(self):
        print(Fore.GREEN + "Welcome to the assistant bot!")
        while True:
            user_input = input(Fore.BLUE + "Enter a command: ")
            command, args = self.parse_input(user_input)

            if command in ["close", "exit"]:
                print(Fore.GREEN + "Good bye!")
                break
            elif command == "hello":
                print(Fore.GREEN + "How can I help you?")
            elif command == "add":
                print(self.add_contact(args))
            elif command == "change":
                print(self.change_contact(args))
            elif command == "phone":
                print(self.show_phone(args))
            elif command == "remove-phone":
                print(self.remove_phone(args))
            elif command == "all":
                print(self.show_all())
            elif command == "add-birthday":
                print(self.add_birthday(args))
            elif command == "show-birthday":
                print(self.show_contact_birthday(args))
            elif command == "birthdays":
                print(self.show_birthdays(args))
            elif command == "remove":
                print(self.remove_contact(args))
            else:
                print(Fore.RED + "Invalid command.")
