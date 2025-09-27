import random

def main():
    score = float(input("Enter score: "))
    result = determine_score(score)
    print(result)

    random_score = random.randint(0, 100)
    print(f"Random score: {random_score}")
    print(determine_score(random_score))

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
