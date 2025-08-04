print(type(12 + 10.25))

print(type(12 + 10.25))

print(type(12 + 3j))

#Boolean
print(type(True))

print(type(False))

print(type(1>5))

print(type(1 == 1))

print(1 > 5)

print(1 == 1)

#Strings
print('Single quotes')

print("Double quotes")

multiline = """
The ice cream 
is my favorite
Dessert
"""
print(multiline)
print(type(multiline))

a = 'Hello World!'
print(a[0])  # First character
print(a[1])  # Second character
print(a[2:5])  # Characters from index 2 to 4
print(a*3)
print(a + ' How are you?')  # Concatenation

#Lists
[1, 2, 3, 4, 5]

['Cookie', 'Ice Cream', 'Cake']

x = ['Vanilla', 3, ['Scoops', 'Toppings'], True]
print(type(x))
print(x)

ice_cream = ['Vanilla', 'Chocolate', 'Strawberry']

ice_cream.append('Mint')
print(ice_cream)

ice_cream.remove('Chocolate')
print(ice_cream)

ice_cream[0] = 'Cookies and Cream'
print(ice_cream)

nest_list = ['Vanilla', 3, ['Scoops', 'Toppings'], True]

print(nest_list[2][0]) # Accessing nested list element, Scoops

#Tuples
# cannot be changed if created
tuple_scoops = (1,2,3,2,1)
print(type(tuple_scoops))
print(tuple_scoops[0])
# tuple_scoops.append(4)  # This will raise an error since tuples are immutable

#Sets
# cannot have duplicates
set_scoops = {1, 2, 3}
print(type(set_scoops))
print(set_scoops)  # Output will be {1, 2, 3

daily_tasks = {1,2,3,1,3,6,43,645,6,3,2,1}
print(daily_tasks) # Output will be {1, 2, 3, 43, 645, 6}

daily_log = {1, 2, 3, 4, 5, 6, 7, 8, 9}

print(daily_log | daily_tasks)  # Union of two sets
print(daily_log & daily_tasks)  # Intersection of two sets
print(daily_log - daily_tasks)  # Difference of two sets
print(daily_tasks ^ daily_log)  # Symmetric difference of two sets

#Dictionaries
# key/value pairs

dict_cream = {'name': 'Alex', 'weekly intake': 5, 'favorite ice cream': ['MCC','Chocolate']}
print(type(dict_cream))
print(dict_cream)
print(dict_cream.values())
print(dict_cream.keys())
print(dict_cream.items())
print(dict_cream['name'])

dict_cream['name'] = 'John'
print(dict_cream)

dict_cream.update({'name': 'John', 'weekly intake': 10, 'weight': 300})
print(dict_cream)

del dict_cream['weekly intake']
print(dict_cream)
