"""
CP1404/CP5632 Practical
Emails to names dictionary program
Estimate time: 15 minutes
"""

def main():
    """Store emails and names in a dictionary and display them."""
    email_to_name = {}

    email = input("Email: ").strip()
    while email != "":
        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if confirmation != "" and confirmation != "y":
            name = input("Name: ").strip().title()

        email_to_name[email] = name
        email = input("Email: ").strip()

    # Display results
    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")