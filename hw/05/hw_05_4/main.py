from colorama import Fore, init

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
    contacts[name] = phone
    return Fore.YELLOW + "Contact added."

@input_error
def change_contact(args, contacts):        
    name, phone = args
    if name in contacts:
        contacts[name] = phone
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

        else:
            print(Fore.RED + "Invalid command.")

if __name__ == "__main__":
    main()