if 10 > 5:
    print('it worked!')

if 10 < 5:
    print('it worked!')
else:
    print('it did not work...')

if 5 > 10:
    print('it worked!')
elif 15 < 20:
    print('elif worked!')
else:
    print('it did not work...')

print('it worked!') if 10 > 5 else print('it did not work...')

if (5 > 10) and (10 > 5):
    print('it worked!')
elif 15 < 20:
    print('elif worked!')
    if 10 > 5:
        print('nested if worked!')
    elif 20 < 15:
        print('nested elif worked!')
    else:
        print('nested else worked!')
else:
    print('it did not work...')
