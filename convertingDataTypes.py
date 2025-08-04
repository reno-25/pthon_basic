num_int = 7
print(type(num_int))

num_str = '7'
print(type(num_str))

num_sum = num_int + int(num_str)
print(num_sum)
print(type(num_sum))
# or
num_str_conv = int(num_str)
print(type(num_str_conv))

num_sum1 = num_int + num_str_conv
print(num_sum1)
print(type(num_sum1))

list_type = [1, 2, 3]
print(type(list_type))

print(type(tuple(list_type)))

list_type = [1, 2, 3, 3, 2, 1, 2, 3, 2, 1]

print(set(list_type))
print(type(set(list_type)))

dict_type =  {'name': 'Alex', 'age': 30, 'city': 'New York'}
print(type(dict_type))

print(dict_type.items())
print(dict_type.values())
print(dict_type.keys())

print(
    type(
        list(
            dict_type.items())))
print(
    type(
        list(
            dict_type.values())))
print(
    type(
        list(
            dict_type.keys())))

long_str = "I like to party"

print(
    list(long_str)  # Convert string to list of characters
)
