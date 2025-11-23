from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    # Test fanciness multiplier + flagfall
    hummer = SilverServiceTaxi("Hummer", 200, 2)
    hummer.drive(18)


    expected_fare = 48.8
    actual_fare = hummer.get_fare()

    print(hummer)
    print(f"Fare: ${actual_fare:.2f}")

    assert actual_fare == expected_fare, "Fare calculation is incorrect"


if __name__ == "__main__":
    main()

