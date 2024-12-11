def say_hello(name):
    return f"Hello, {name}!"

# print("You imported hello.py")
# say_hello('user')

# ---------------------------------------
# if __name__ == '__main__':
#     print("You imported hello.py")
#     say_hello('user')
# OR - better pattern - use main() function
def main():
    print("You imported hello.py")
    say_hello('user')

if __name__ == '__main__':
    main()
