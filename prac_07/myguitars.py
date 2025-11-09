from guitar import Guitar
import csv


def main():
    """Read file of guitar details, save as objects, display sorted by year."""
    guitars = []

    in_file = open('guitars.csv', 'r')
    in_file.readline()

    for line in in_file:
        # print(repr(line))  # debugging
        parts = line.strip().split(',')
        # print(parts)       # debugging

        name = parts[0]
        year = int(parts[1])
        cost = float(parts[2])