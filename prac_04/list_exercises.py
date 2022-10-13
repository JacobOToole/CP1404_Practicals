# Basic List Operations

AMOUNT_OF_NUMBERS = 5
numbers = []
sum_of_numbers = 0

for q in range(AMOUNT_OF_NUMBERS):
    number = int(input("Number: "))
    numbers.append(number)

for i in numbers:
    sum_of_numbers += i
average = sum_of_numbers / AMOUNT_OF_NUMBERS

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {average}")


# Woefully Inadequate Security Checker

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

username = input("Username: ")

if username in usernames:
    print("Access granted")
else:
    print("Access denied")