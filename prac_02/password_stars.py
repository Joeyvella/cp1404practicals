password = input("Enter password: ")

while len(password) < 8:
    print(f"Password must be at least 8 characters long.")
    password = input("Enter password: ")

print("*" * len(password))