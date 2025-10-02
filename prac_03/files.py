"""
CP1404/CP5632 - Practical
Files exercises
"""

#1 Asking user for name and opening a file to write down there name
name = input("Enter your name: ")
out_file = open("name.txt", "w") #opens name.txt and writes
print(name, file=out_file)
out_file.close()

#2
in_file = open("name.txt", "r")
""" the file name.txt is now open and being read"""
name = in_file.read().strip()
"""using strip function will grab the line with the users name on it"""
in_file.close()
print(f"Hi {name}!")

#3
with open("numbers.txt", "r") as in_file:
    number1 = int(in_file.readline())
    """ number1 will read the first line"""
    number2 = int(in_file.readline())
    """number2 will read the 2nd line"""
    in_file.close()
    print(number1 + number2)

#4
with open("numbers.txt", "r") as in_file:
    """opens numbers.txt to read"""
    total = 0
    for line in in_file:
        total += int(line)
        """will add the total integers together that it reads on each line"""
    print(total)
in_file.close()