# Comparison Operators
print(10 == 10)
print(5 != 10)
print(5 < 10)
print(10 > 5)
print(5 <= 10)
print(10 >= 5)
print('Vanilla' > 'Chocolate') # true because 'V' comes after 'C' in ASCII

# Logical Operators
print(not (5 < 10))
print(5 < 10 and 10 > 5)
print(5 < 10 or 10 < 5)

# Membership Operators
print('a' in 'apple')  # True, 'a' is in 'apple'
print('b' not in 'apple')  # True, 'b' is not in 'apple'

# Identity Operators
print(5 is 5)  # True, both are the same object
print(5 is not 10)  # True, they are different objects
print([] is [])  # False, two different empty lists
print([] == [])  # True, they are equal in value

# Bitwise Operators
print(5 & 3)  # Bitwise AND, results in 1 (0101 & 0011 = 0001)
print(5 | 3)  # Bitwise OR, results in 7 (0101 | 0011 = 0111)
print(5 ^ 3)  # Bitwise XOR, results in 6 (0101 ^ 0011 = 0110)
print(~5)  # Bitwise NOT, results in -6 (inverts bits of 5)
print(5 << 1)  # Bitwise left shift, results in 10 (0101 << 1 = 1010)
print(5 >> 1)  # Bitwise right shift, results in 2 (0101 >> 1 = 0010)
