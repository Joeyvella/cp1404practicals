"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
state_name = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
print(state_name)

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in state_name:
        print(state_code, "is", state_name[state_code])
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ")
