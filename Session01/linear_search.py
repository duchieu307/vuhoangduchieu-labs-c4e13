numbers = [1, 5, 12, 124 ,12234, 12342]
n = int(input("Enter a numbers "))

found_index = -1

for i , j in enumerate(numbers):
    if j == n :
        print(j, 'at', i + 1)
        found_index = i
        # found_index: them mot bien vao vong for, neu n ton tai trong list thi gan gia tri found_index = i va ket thuc vong lap
        break

if found_index == -1 :
    print("Not Found")
