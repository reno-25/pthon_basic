integers = [1, 2, 3, 4, 5]
for i in integers:
    print(i)

for i in integers:
    print('Hello World!')

integers = [1, 2, 3, 4, 5]
for body in integers:
    print(body + body)

data = {'name': 'Alice', 'age': 30, 'city': 'New York'}

for char in data.values():
    print(char)

for key, value in data.items():
    print(key, '-> ',value)

for key, value in data.items():
    print(f"{key}: {value}")

flavors = ['chocolate', 'vanilla', 'strawberry']
toppings = ['sprinkles', 'nuts', 'chocolate chips']

for x in flavors:
    for y in toppings:
        print(x, 'topped with', y)
