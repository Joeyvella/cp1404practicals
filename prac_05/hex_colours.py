


color_to_code = {
    "absolute zero": "#0048ba",
    "acid green": "#b0bf1a",
    "alice blue": "#f0f8ff",
    "alizarin crimson": "#e32636",
    "amaranth": "#e52b50",
    "amber": "#ffbf00",
    "amethyst": "#9966cc",
    "antique white": "#faebd7",
    "apricot": "#fbceb1",
    "aqua": "#00ffff",
    "ash grey": "#b2beb5"
}

color_name = input("What color code would you like to see: ").strip().lower()
while color_name != "":
    if color_name in color_to_code:
        print(f"{color_name.title()} is {color_to_code[color_name]}")
    else:
        print("Invalid color")
    color_name = input("What color code would you like to see: ").strip().lower()
