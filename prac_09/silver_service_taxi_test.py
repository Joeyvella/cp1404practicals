from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    # Test fanciness multiplier + flagfall
    hummer = SilverServiceTaxi("Hummer", 200, 2)
    hummer.drive(18)


    expected_fare = 48.8
    actual_fare = hummer.get_fare()

