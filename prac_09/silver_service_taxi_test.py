from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    # Test fanciness multiplier + flagfall
    van = SilverServiceTaxi("van", 200, 2)
    van.drive(18)


    expected_fare = 48.8
    actual_fare = van.get_fare()

    print(van)
    print(f"Fare: ${actual_fare:.2f}")

    assert actual_fare == expected_fare, "Fare calculation is incorrect"


if __name__ == "__main__":
    main()

