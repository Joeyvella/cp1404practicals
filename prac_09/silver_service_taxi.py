"""
SilverServiceTaxi class
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised Taxi that includes fanciness and flagfall."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # Scale the price per km (instance variable)
        self.price_per_km = Taxi.price_per_km * fanciness

    def get_fare(self):
        """Return fare: base fare * distance + flagfall."""
        return super().get_fare() + self.flagfall

    def __str__(self):
        """Add flagfall info at the end."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"