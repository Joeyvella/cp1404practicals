from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Run the taxi simulator program."""
    print("Let's drive!")
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    bill = 0

    menu = "q)uit, c)hoose taxi, d)rive\n>>> "

    user_choice = input(menu).lower()
    while user_choice != "q":
        if user_choice == "c":
            current_taxi = choose_taxi(taxis)
        elif user_choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                bill += drive_taxi(current_taxi)
        else:
            print("Invalid option")

        print(f"Bill to date: ${bill:.2f}")
        user_choice = input(menu).lower()

    print(f"Total trip cost: ${bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)
