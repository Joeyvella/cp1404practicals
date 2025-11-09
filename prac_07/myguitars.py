from guitar import Guitar
import csv


def main():
    """Read file of guitar details, save as objects, display sorted by year."""
    guitars = []

    in_file = open('guitars.csv', 'r')
    in_file.readline()
