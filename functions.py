def function():
    print("My first function.")

function()

def first():
    print('We did it!')

first()

def number_squared(x):
    print(x**2)

number_squared(5)

def number_squered_cust(num,power):
    print(num**power)

number_squered_cust(2, 3)

args_tuple = (5,6,1,3,4)

def number_args(*number):
    print(number[0]*number[1]) # prints the product of the first two numbers in the tuple

number_args(*args_tuple) # must use * to unpack the tuple

def number_squered_cust(num,power):
    print(num**power)

number_squered_cust(power=3, num=2) # keyword arguments can be used to specify the order

def num_kwargs(**num):
    print('My number is: ' + num['integer'] + ' and ' + num['integer2'])

num_kwargs(integer= '2000', integer2 = '3000')  # keyword arguments can be used to pass a dictionary-like structure
