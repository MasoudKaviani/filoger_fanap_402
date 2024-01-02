import random

levels = [1, 2, 3, 4] # 1 -> easy, 2 -> medium, 3 -> hard, 4 -> iran mode
selected_level = 0
while (selected_level not in levels):
    try:
        selected_level = int(input('Level of The Game [1 -> easy, 2 -> medium, 3 -> hard, 4 -> iran mode]: '))
        if selected_level not in levels:
            print('Please Enter a Number between 1 and 4 for Level')
    except:
        print('Please Enter a Number between 1 and 4 for Level')
print(selected_level)

L = 0
U = 0
COUNT_GUESS = 0

if selected_level == 1:
    L, U, COUNT_GUESS = 1, 30, 10
elif selected_level == 2:
    L, U, COUNT_GUESS = 1, 50, 7
elif selected_level == 3:
    L, U, COUNT_GUESS = 1, 100, 5
elif selected_level == 4:
    L, U, COUNT_GUESS = 1, 1000, 1


computer_guess = int(random.randint(L, U))
for i in range(COUNT_GUESS):
    user_guess = -1
    while user_guess < L or user_guess > U:
        try:
            user_guess = int(input('Please Enter a Number Between {0} and {1}: '.format(L, U)))
        except:
            print('Please Enter a Valid Number Between {0} and {1}'.format(L, U))
    if user_guess == computer_guess:
        print("OK, That's it")
        break
    else:
        print('No')
        if user_guess < computer_guess:
            print('Your Number is Smaller Than The Computer Number')
        else:
            print('Your Number is Greater Than The Computer Number')
        print('You Have {0} Turn'.format(COUNT_GUESS-i))

print('The Number was {0}'.format(computer_guess))

input('Thank you, Please visit our website at mehrshad.com')