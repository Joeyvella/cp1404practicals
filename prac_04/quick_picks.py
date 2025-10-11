"""
CP1404/CP5632 Practical
Quick Pick Lottery Ticket Generator (no global variables)
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
