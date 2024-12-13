import sys
from pathlib import Path
from colorama import Fore, init

init(autoreset=True)

def print_folder_structure(folder: Path, indent: int = 0):
    try:
        for item in folder.iterdir():
            if item.is_dir():
                print(' ' * indent + Fore.YELLOW + item.name)
                print_folder_structure(item, indent + 4)
            else:
                print(' ' * indent + Fore.GREEN + item.name)
    except PermissionError:
        print(' ' * indent + Fore.RED + "Permission denied: " + str(folder))

def main():
    if len(sys.argv) != 2:
        print(Fore.RED + "Usage: python main.py <folder_path>")
        sys.exit(1)

    folder_path = Path(sys.argv[1])

    if not folder_path.exists():
        print(Fore.RED + "Error: The specified path does not exist.")
        sys.exit(1)

    if not folder_path.is_dir():
        print(Fore.RED + "Error: The specified path is not a directory.")
        sys.exit(1)

    print(Fore.CYAN + "Directory structure of: " + Fore.RED + str(folder_path) + "\n")
    print_folder_structure(folder_path)

if __name__ == "__main__":
    main()
