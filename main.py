"""
I took the idea from a video by freeCodeCamp.org - Six Quick Python Projects, but I want to develop this project using lists. 
Furthermore, I want to challenge myself by generating a password with at least 20% of its length consisting of random numbers 
in random positions and 30% with random symbols also in random positions.
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
    # I generate this strings with chatgpt :)
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numbers = '0123456789'
    symbols = '!@#$%^&*()_+-=[];:,<.>/?|'

    # Distribution of password characters
    chars_length = round(password_length * 0.5)
    numbers_length = round(password_length * 0.2)
    symbols_length = round(password_length * 0.3)

    # Normalization
    distribution_length = chars_length + numbers_length + symbols_length

    if distribution_length > password_length:
        chars_length = chars_length - (distribution_length - password_length)

    # Passwords Generator
    for pwd in range(password_amount):
        password = ''

        distribution_list = ['chars', 'numbers', 'symbols']

        chars_control = chars_length
        numbers_control = numbers_length
        symbols_control = symbols_length

        for c in range(password_length):
            distribution_choice = random.choice(distribution_list)
            if distribution_choice == 'chars':
                password += random.choice(chars)
                chars_control -= 1
                if chars_control == 0:
                    distribution_list.remove('chars')

            if distribution_choice == 'numbers':
                password += random.choice(numbers)
                numbers_control -= 1
                if numbers_control == 0:
                    distribution_list.remove('numbers')

            if distribution_choice == 'symbols':
                password += random.choice(symbols)
                symbols_control -= 1
                if symbols_control == 0:
                    distribution_list.remove('symbols')
        # include in list code
        password_list.append(password)

    # Output of Data
    if password_amount == 1:
        print(f'Here are your password: {password_list[0]}')
    else:
        print(f'Here are your {password_amount} passwords: ')
        for x in password_list:
            print(x)
