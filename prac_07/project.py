"""CP1404/CP5632 Practical – Project class
Estimate: 45 min | Actual: 30 min
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

    def __str__(self):
        """Return a formatted string for displaying a Project."""
        return (f"{self.name}, start: {self.start_date.strftime(DATE_FMT)}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, "
                f"completion: {self.completion}%")


    def from_row(self, row):
        """Read data from a line in the file and update this Project’s attributes."""
        name, date, priority, cost, completion = row
        self.name = name.strip()
        self.start_date = datetime.strptime(date.strip(), DATE_FMT)
        self.priority = int(priority)
        self.cost_estimate = float(cost)
        self.completion = int(completion)

    def to_row(self):
        """Return a list of strings to save this Project to a file."""
        return [
            self.name,
            self.start_date.strftime(DATE_FMT),
            str(self.priority),
            f"{self.cost_estimate:.2f}",
            str(self.completion)]