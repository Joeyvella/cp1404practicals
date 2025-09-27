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