from guitar import Guitar
import csv


def main():
    """Read file of guitar details, save as objects, display sorted by year."""
    guitars = []

    in_file = open('guitars.csv', 'r')
    in_file.readline()

    for line in in_file:

        parts = line.strip().split(',')
        name = parts[0]
        year = int(parts[1])
        cost = float(parts[2])

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)

    in_file.close()
    guitars.sort()

    print("These are my guitars sorted by year:")
    for guitar in guitars:
        print(guitar)



main()