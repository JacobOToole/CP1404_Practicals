import random

SMALLEST_NUMBER = 1
LARGEST_NUMBER = 45
AMOUNT_OF_NUMBERS = 6
numbers = []

QUICK_PICKS = int(input("How many quick picks do you wish to generate? "))

for i in range(QUICK_PICKS):
    number = random.randint(SMALLEST_NUMBER, LARGEST_NUMBER + 1)
    while len(numbers) < AMOUNT_OF_NUMBERS:
        if number not in numbers:
            numbers.append(number)
        number = random.randint(SMALLEST_NUMBER, LARGEST_NUMBER + 1)
    numbers.sort()
    for i in numbers:
        print(f"{i:2}", end=" ")
    numbers = []
    print("")

