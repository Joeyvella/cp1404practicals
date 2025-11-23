"""
CP1404/CP5632 Practical
UnreliableCar class
"""

import random
from prac_09.car import Car


class UnreliableCar(Car):
    """Specialised version of a Car that may not drive depending on reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = float(reliability)

    def drive(self, distance):
        """Drive car a random distance between 0 and 100, choose if it will be reliable then return distance driven."""
        chance = random.uniform(0,100)
        if chance < self.reliability:
            return super().drive(distance)
        return 0
