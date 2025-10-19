"""
CP1404/CP5632 Practical
Wimbledon champions data processing
Estimate time: 20 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    """Read Wimbledon data, count champions, and display results."""
    records = get_wimbledon_data(FILENAME)
    champion_to_count = count_champions(records)
    countries = get_countries(records)

    display_champions(champion_to_count)
    display_countries(countries)

def get_wimbledon_data(filename):
    """Read the data file and return a list of lists."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # Skip the header line
        data = [line.strip().split(",") for line in in_file]
    return data


def count_champions(data):
    """Count how many times each champion has won."""
    champion_to_count = {}
    for record in data:
        champion = record[2]
        if champion in champion_to_count:
            champion_to_count[champion] += 1
        else:
            champion_to_count[champion] = 1
    return champion_to_count
