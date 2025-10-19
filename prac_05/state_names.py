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
print(code_to_state)

state_code = input("Enter short state: ").strip().upper()
while state_code != "":
    try:
        print(f"{state_code} is {code_to_state[state_code]}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").strip().upper()

print("\nAll states and names:")
for code, name in code_to_state.items():
    print(f"{code:3} is {name}")