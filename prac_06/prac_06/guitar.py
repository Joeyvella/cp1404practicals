"""
Guitar class
Estimate: 20
Actual:40
"""

CURRENT_YEAR = 2025

class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a nicely formatted guitar string."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return how old the guitar is in years."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old."""
        return self.get_age() >= 50