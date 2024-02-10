"""
I took the idea from a video by freeCodeCamp.org - Six Quick Python Projects, but I want to develop this project using lists. 
Furthermore, I want to challenge myself by generating a password with at least 20% of its length consisting of random numbers 
in random positions and 30% with random special characters also in random positions.
"""
import random

print('Welcome to the most advanced password generator!!!!')

# Input of Data
password_amount = int(
    input('\nPlease enter the number of passwords you wish to generate: '))

if password_amount == 0:
    print('You dont want any password? Get out of here!')
else:
    password_length = int(
        input('Please enter the desired length of the passwords: '))

    password_list = []

    # Code
    # I generate this string with chatgpt :)
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=[];:,<.>/?|0123456789'

    for pwd in range(password_amount):
        password = ''
        for c in range(password_length):
            password += random.choice(chars)
        # include in list code
        password_list.append(password)

    # Output of Data
    if password_amount == 1:
        print(f'Here are your password: {password_list[0]}')
    else:
        print(f'Here are your {password_amount} passwords: ')
        for x in password_list:
            print(x)
