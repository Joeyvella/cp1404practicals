"""
CP1404/CP5632 Practical
Quick Pick Lottery Ticket Generator
"""

import random


def main():
    numbers_per_line = 6
    min_number = 1
    max_number = 45

    quick_picks = int(input("How many quick picks? "))

    for i in range(quick_picks):
        pick = generate_quick_pick(numbers_per_line, min_number, max_number)
        display_pick(pick)


def generate_quick_pick(numbers_per_line, min_number, max_number):
    """Generates a single quick pick with numbers."""
    pick = []
    while len(pick) < numbers_per_line:
        number = random.randint(min_number, max_number)
        if number not in pick:
            pick.append(number)
    pick.sort()
    return pick


def display_pick(pick):
    """Displays one number that is lined up"""
    print(" ".join(f"{num:2}" for num in pick))


main()