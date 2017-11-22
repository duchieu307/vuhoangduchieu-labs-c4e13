numbers = [1, 5, 12, 124 ,12234, 12342, 55]
numbers.sort()
start = 1
stop = len(numbers)
x = int(input('Enter a number '))
found_index = - 1
while start != stop :
    mid = (start+stop)//2
    if numbers[mid] == x :
        print(numbers[mid], mid)
        found_index = numbers[mid]

        exit()
    elif numbers[mid] > x :
        stop = mid -  1
        found_index = numbers[mid]
    elif numbers[mid] < x:
        start = mid + 1
        found_index = numbers[mid]
print(numbers[mid], mid)
if found_index == -1 :
    print(x, "not in numbers")
