"""
Guitar_test
Estimated: 10
Actual: 20
"""



from guitar import Guitar


def main():
    """Test the Guitar class methods."""

    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another = Guitar("Another Guitar", 2013, 500)

    print("Gibson L-5 CES get_age() - Expected 103. Got", gibson.get_age())
    print("Another Guitar get_age() - Expected 12. Got", another.get_age())

    print("Gibson L-5 CES is_vintage() - Expected True. Got", gibson.is_vintage())
    print("Another Guitar is_vintage() - Expected False. Got", another.is_vintage())

main()