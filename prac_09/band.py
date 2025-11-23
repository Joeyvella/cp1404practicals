"""
Band class for CP1404
"""

class Band:
    """Band class that holds a list of musicians."""

    def __init__(self, name):
        """Initialise a Band with a name and empty musician list."""
        self.name = name
        self.musicians = []