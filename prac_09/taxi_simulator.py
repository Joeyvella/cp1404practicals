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


def choose_taxi(taxis):
    """Let the user choose a taxi and return the chosen taxi object, or None."""
    print("Taxis available:")
    display_taxis(taxis)
    try:
        taxi_choice = int(input("Choose taxi: "))
        if taxi_choice < 0 or taxi_choice >= len(taxis):
            print("Invalid taxi choice")
            return None
        return taxis[taxi_choice]
    except ValueError:
        print("Invalid taxi choice")
        return None