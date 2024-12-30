from colorama import Fore, init
from datetime import datetime, timedelta

init(autoreset=True)

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return Fore.RED + "Contact not found. Please check the name."
        except ValueError:
            return Fore.RED + "Give me name and phone please." + Fore.GREEN + "\nUsage: <command> <name> <phone>"
        except IndexError:
            return Fore.RED + "Invalid number of arguments." + Fore.GREEN + "\nUsage: <command> <name>"
    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name in contacts:
        return Fore.RED + "Contact already exists. Use 'change' to update the number."
    contacts[name] = {"phone": phone, "birthday": None}
    return Fore.YELLOW + "Contact added."

@input_error
def change_contact(args, contacts):        
    name, phone = args
    if name in contacts:
        contacts[name]["phone"] = phone
        return Fore.YELLOW + "Contact updated."
    else:
        return Fore.RED + "Contact not found. Use 'add' to create a new contact."

@input_error
def show_phone(args, contacts):
    name = args[0]
    if name in contacts:
        return Fore.YELLOW + f"{name}: {contacts[name]}"
    else:
        return Fore.RED + "Contact not found."

@input_error
def show_all(contacts):
    if contacts:
        result = Fore.CYAN + "All contacts:\n"
        for name, phone in contacts.items():
            result += Fore.YELLOW + f"{name}: {phone}\n"
        return result.strip()
    else:
        return Fore.RED + "No contacts found."

@input_error
def add_birthday(args, contacts):
    name, birthday = args
    if name in contacts:
        try:
            birthday_date = datetime.strptime(birthday, "%d.%m.%Y").date()
            contacts[name]["birthday"] = birthday_date
            return Fore.YELLOW + f"Birthday for {name} added: {birthday_date.strftime('%d.%m.%Y')}"
        except ValueError:
            return Fore.RED + "Invalid date format. Use DD.MM.YYYY."
    else:
        return Fore.RED + "Contact not found. Add the contact first."

@input_error
def show_birthday(args, contacts):
    name = args[0]
    if name in contacts:
        birthday = contacts[name].get("birthday")
        if birthday:
            return Fore.YELLOW + f"{name}'s birthday is on {birthday.strftime('%d.%m.%Y')}."
        else:
            return Fore.RED + f"No birthday found for {name}."
    else:
        return Fore.RED + "Contact not found."

@input_error
def birthdays(args, contacts):
    today = datetime.today().date()
    upcoming_birthdays = []
    for name, details in contacts.items():
        birthday = details.get("birthday")
        if birthday:
            next_birthday = birthday.replace(year=today.year)
            if next_birthday < today:
                next_birthday = next_birthday.replace(year=today.year + 1)
            days_until = (next_birthday - today).days
            if days_until <= 7:
                upcoming_birthdays.append((name, next_birthday))
    
    if upcoming_birthdays:
        result = Fore.CYAN + "Upcoming birthdays:\n"
        for name, date in sorted(upcoming_birthdays, key=lambda x: x[1]):
            result += Fore.YELLOW + f"{name}: {date.strftime('%d.%m.%Y')}\n"
        return result.strip()
    else:
        return Fore.RED + "No upcoming birthdays in the next week."

def main():
    contacts = {}
    print(Fore.GREEN + "Welcome to the assistant bot!")
    while True:
        user_input = input(Fore.BLUE + "Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(Fore.GREEN + "Good bye!")
            break

        elif command == "hello":
            print(Fore.GREEN + "How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_phone(args, contacts))

        elif command == "all":
            print(show_all(contacts))

        elif command == "add-birthday":
            print(add_birthday(args, contacts))

        elif command == "show-birthday":
            print(show_birthday(args, contacts))

        elif command == "birthdays":
            print(birthdays(args, contacts))

        else:
            print(Fore.RED + "Invalid command.")

if __name__ == "__main__":
    main()