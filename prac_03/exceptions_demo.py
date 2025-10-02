"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
2. When will a ZeroDivisionError occur?
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0: # checks if the input of the denominator is equal to zero
        print("Denominator cannot be zero!")
    else:
        fraction = numerator / denominator #finishes of the code
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")

#1. a value error will occur when the user enters a symbol or letter
#2. a ZeroDivisionError would occur when a numerator is divided by a zero
#3. yes, as seen the use of an if else statement inside the try part will eliminate the need for a second except