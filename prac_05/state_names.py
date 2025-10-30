"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""


code_to_state = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria", "TAS": "Tasmania",
    "SA": "South Australia"
}

def search_loop(code_to_state):
    """Ask for state code and print using EAFP."""
    code = input("Enter short state: ").strip().upper()
    while code != "":
        try:
            print(f"{code} is {code_to_state[code]}")
        except KeyError:
            print("Invalid short state")
        code = input("Enter short state: ").strip().upper()

def print_states_neatly(code_to_state):
    """Print the dictionary as a neat two column table."""
    code_w = max(len(code) for code in code_to_state)
    name_w = max(len(name) for name in code_to_state.values())

    print("\nAll states and names:")
    for code, name in code_to_state.items():
        print(f"{code:<{code_w}}  is  {name:<{name_w}}")


search_loop(code_to_state)
print_states_neatly(code_to_state)