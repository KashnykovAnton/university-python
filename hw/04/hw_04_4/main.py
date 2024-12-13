from colorama import Fore, init

init(autoreset=True)

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            return Fore.RED + "Contact already exists. Use 'change' to update the number."
        contacts[name] = phone
        return Fore.YELLOW + "Contact added."
    except ValueError:
        return Fore.RED + "Invalid number of arguments." + Fore.GREEN + "\nUsage: add <name> <phone>"

def change_contact(args, contacts):
    try:
        name, phone = args
        if name in contacts:
            contacts[name] = phone
            return Fore.YELLOW + "Contact updated."
        else:
            return Fore.RED + "Contact not found. Use 'add' to create a new contact."
    except ValueError:
        return Fore.RED + "Invalid number of arguments." + Fore.GREEN + "\nUsage: change <name> <phone>"

def show_phone(args, contacts):
    try:
        name = args[0]
        if name in contacts:
            return Fore.YELLOW + f"{name}: {contacts[name]}"
        else:
            return Fore.RED + "Contact not found."
    except IndexError:
        return Fore.RED + "Invalid number of arguments." + Fore.GREEN + "\nUsage: phone <name>"

def show_all(contacts):
    if contacts:
        result = Fore.CYAN + "All contacts:\n"
        for name, phone in contacts.items():
            result += Fore.YELLOW + f"{name}: {phone}\n"
        return result.strip()
    else:
        return Fore.RED + "No contacts found."

def main():
    contacts = {}
    print(Fore.GREEN + "Welcome to the assistant bot!")
    while True:
        user_input = input(Fore.BLUE + "Enter a command: ")
        command, *eargs = parse_input(user_input)

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

        else:
            print(Fore.RED + "Invalid command.")

if __name__ == "__main__":
    main()