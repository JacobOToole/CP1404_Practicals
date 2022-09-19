minimum_length = 5

password = input("Password: ")
while len(password) < 5:
    print("Password is too short")
    password = input("Password: ")

print('*' * len(password))
