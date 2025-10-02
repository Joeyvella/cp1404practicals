"""
CP1404/CP5632 - Practical
Files exercises
"""

# 1. Asking user for name and opening a file to write down there name
name = input("Enter your name: ")
out_file = open("name.txt", "w") #opens name.txt and writes
print(name, file=out_file)
out_file.close()

