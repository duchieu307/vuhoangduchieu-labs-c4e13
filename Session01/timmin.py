numbers = [10, 5, 12, -124 ,12234, -12342, -15]

min_number = numbers[0]
max_number = numbers[0]

for index, number in enumerate(numbers):
    if min_number > number  :
        min_number = number
    elif max_number < number:
        max_number = number

print(min_number)
print(max_number)
