"""
CP1404/CP5632 Practical
Hex codes in a dictionary
"""

COLOUR_NAMES = {"blue": "#0048ba", "red": "#e32636", "green": "#006b3c", "yellow": "#fff600", "purple": "#9966cc",
               "white": "#f0f8ff", "black": "#000000", "orange": "#ed872d", "brown": "#cc5500", "magenta": "#de3163"}
print(COLOUR_NAMES)

colour = input("Enter colour: ").lower()
while colour != "":
    try:
        print(f"{colour:3} is {COLOUR_NAMES[colour]}")
    except KeyError:
        print("Invalid colour")
    colour = input("Enter another colour: ").lower()

