number = 0

while number < 5:
    print(number)
    number = number + 1 #or number += 1

number = 0

while number < 5:
    print(number)
    if number == 3:
        break
    number += 1

number = 0

while number < 5:
    print(number)
    if number == 6:
        break
    number += 1
else:
    print('No longer < 5')

number = 0

while number < 5:
    number += 1
    if number == 3:
        continue 
    print(number)
else:
    print('No longer < 5')
