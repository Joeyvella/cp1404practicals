def main():

    score = get_valid_score()

    MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_score(score)
            print(result)
        elif choice == "S":
            print("*" * int(score))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()

    print("Farewell.")

def get_valid_score():
        score = float(input("Enter score (0-100): "))
        while score < 0 or score > 100:
            print("Invalid score! Must be between 0 and 100.")
            score = float(input("Enter score (0-100): "))
        return score

def determine_score(score):
    if score < 0 or score > 100:
        return "Invalid"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


main()
