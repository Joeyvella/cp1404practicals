def main():
    min_length = 8
    password = get_password(min_length)
    print_stars(password)

def get_password(min_length):
    password = input("Enter password: ")
    while len(password) < min_length:
        print(f"Password must be at least {min_length} characters long.")
        password = input("Enter password: ")
    return password

def print_stars(password):
    print("*" * len(password))
main()