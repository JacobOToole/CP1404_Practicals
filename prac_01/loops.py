for i in range(1, 21, 2):
    print(i, end=' ')
print()

for i in range(0, 100, 10):
    print(i, end=' ')

for i in range(20, 0, -1):
    print(i, end=' ')

number = int(input("Number of stars: "))
for i in range(0, number):
    print('*', end='')

number = int(input("Number of stars: "))
for i in range(0, number + 1):
        print('*' * i)