"""
Test UnreliableCar class.
"""

from unreliable_car import UnreliableCar

def main():
    # Create two cars with different reliability
    good_car = UnreliableCar("Almost Perfect", 100, reliability=90)
    bad_car = UnreliableCar("Barely Works", 100, reliability=30)
