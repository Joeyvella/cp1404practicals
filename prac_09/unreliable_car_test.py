"""
Test UnreliableCar class.
"""

from unreliable_car import UnreliableCar

def main():
    # Create two cars with different reliability
    good_car = UnreliableCar("Almost Perfect", 100, reliability=90)
    bad_car = UnreliableCar("Barely Works", 100, reliability=30)

    print("Testing UnreliableCar")

    print("\n--- Good Car (90% reliability) ---")
    for attempt in range(10):
        distance = good_car.drive(10)
        print(f"Attempt {attempt + 1}: Drove {distance} km")

    print("\n--- Bad Car (30% reliability) ---")
    for attempt in range(10):
        distance = bad_car.drive(10)
        print(f"Attempt {attempt + 1}: Drove {distance} km")