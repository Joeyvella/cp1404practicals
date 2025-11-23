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
        """Return string representation of the Band."""
        return f"{self.name} ({self.musicians})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return output of each musician playing their first instrument."""
        results = []
        for musician in self.musicians:
            results.append(musician.play())
        return "\n".join(results)