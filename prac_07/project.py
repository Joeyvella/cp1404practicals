"""CP1404/CP5632 Practical – Project class
Estimate: 45 min | Actual: ___ min
"""

from datetime import datetime

DATE_FMT = "%d/%m/%Y"
class Project:
    """Represent a Project object."""

    def __init__(self, name, start_date, priority, cost_estimate, completion):
        """Initialise a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion

    def is_complete(self):
        """Return True if the project is 100% complete."""
        return self.completion >= 100

    def __lt__(self, other):
        """Compare Projects by priority (smaller number = higher priority)."""
        return self.priority < other.priority