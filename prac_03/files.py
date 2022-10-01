# 1.
name = input("Name: ")
out_file = open('name.txt', 'w')
print(name, file=out_file)
out_file.close()

# 2.
out_file = open('name.txt', 'r')
print("Your name is", out_file.read())
out_file.close()

# 3.
sum_of_numbers = 0
out_file = open('numbers.txt', 'r')
for line in range(2):
    sum_of_numbers += int(out_file.readline())
print(sum_of_numbers)
out_file.close()

# 4.
sum_of_numbers = 0
out_file = open('numbers.txt', 'r')
for line in out_file:
    sum_of_numbers += int(line)
print(sum_of_numbers)
out_file.close()
