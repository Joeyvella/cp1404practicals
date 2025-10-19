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