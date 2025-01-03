from colorama import Fore
from datetime import datetime
from .fields import *

class Record:
    def __init__(self, name):
        try:
            self.name = Name(name)
        except ValueError as e:
            return Fore.RED + f"An error occurred while adding name: {str(e)}"
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        try:
            existing_phone = list(filter(lambda p: p.value == phone, self.phones))
            if existing_phone:
                return Fore.CYAN + f"Phone number {phone} already exists."
            self.phones.append(phone)
            print(Fore.GREEN + f"Phone number {phone} added successfully.")
        except ValueError as e:
            return Fore.RED + f"An error occurred while adding phone: {e}"

    def remove_phone(self, phone):
        try:
            original_length = len(self.phones)
            self.phones = list(filter(lambda p: p.value != phone, self.phones))
            if len(self.phones) < original_length:
                return Fore.GREEN + f"Phone number {phone} was successfully removed."
            return Fore.CYAN + f"Phone number {phone} not found."
        except ValueError as e:
            return Fore.RED + f"An error occurred while removing phone: {e}"

    def edit_phone(self, old_phone, new_phone):
        try:
            if old_phone == new_phone:
                return Fore.YELLOW + "New phone number should be different from the old one."
            
            if new_phone in [p.value for p in self.phones]:
                return Fore.YELLOW + "New phone number is already in the list."
            
            for idx, phone in enumerate(self.phones):
                if phone.value == old_phone:
                    self.phones[idx] = Phone(new_phone)
                    return Fore.GREEN + f"Phone number {old_phone} successfully changed to {new_phone}."
            
            return Fore.RED + f"Phone number {old_phone} not found."
        except ValueError as e:
            return Fore.RED + f"An error occurred while editing phone: {e}"

    def show_phones(self):
        try:
            phones = "; ".join(p.value for p in self.phones)
            return Fore.GREEN + f"Contact name: {self.name.value}, phones: {phones}"
        except ValueError as e:
            return Fore.RED + f"An error occurred while finding phone: {e}"
    
    def add_birthday(self, birthday):
        try:
            if self.birthday is not None:
                self.birthday = birthday
                return Fore.YELLOW + f"Birthday updated to {birthday} successfully."
            else:
                self.birthday = birthday
                return Fore.GREEN + f"Birthday {birthday} added successfully."
        except ValueError as e:
            return Fore.RED + f"An error occurred while adding birthday: {e}"
    
    def show_birthday(self):
        try:
            birthday = self.birthday.value if self.birthday else "not set"
            return Fore.GREEN + f"Contact name: {self.name.value}, birthday: {birthday}"
        except ValueError as e:
            return Fore.RED + f"An error occurred while finding phone: {e}"

    def __str__(self):
        phones = "; ".join(p.value for p in self.phones)
        birthday = self.birthday.value if self.birthday else "not set"
        return Fore.GREEN + f"Contact name: {self.name.value}, phones: {phones}, birthday: {birthday}"
    