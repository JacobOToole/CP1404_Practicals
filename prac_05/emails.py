"""
CP1404 Practical
Email name using dictionary
"""

email_name_dictionary = {}


def main():
    email = input("Email: ")
    while email != "":
        name = extract_name(email)
        answer = input(f"Is your name {name}? (Y/n) ").lower()
        if answer != "" and answer != "y":
            name = input("Name: ")
        email_name_dictionary[name] = email
        email = input("Email: ")
    for i in email_name_dictionary:
        print(f"{i} ({email_name_dictionary[i]})")


def extract_name(email):
    email_elements = email.split('@')
    email_elements = email_elements[0]
    email_elements = email_elements.split('.')
    name = ' '.join(email_elements).title()
    return name


main()
