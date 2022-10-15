"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

STATE_NAMES = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
               "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(STATE_NAMES)

state_code = input("Enter short state: ").upper()
while state_code != "":
    try:
        print(f"{state_code:3} is {STATE_NAMES[state_code]}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()
