"""
Band class for CP1404
"""

class Band:
    """Band class that holds a list of musicians."""

    def __init__(self, name):
        """Initialise a Band with a name and empty musician list."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return string representation of Band: name (list of musicians)."""
        return f"{self.name} ({self.musicians})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)