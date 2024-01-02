import random
LOWER = 1
UPPER = 100

computer_guess = random.randint(LOWER, UPPER)
for i in range(0, 5):
    user_guess = 0
    while user_guess == 0:
        try:
            user_guess = int(input('Please guess (1-100): '))
            if user_guess > 100 or user_guess < 1:
                print('Please enter a NUMBER (1-100)!')
                user_guess = 0
        except:
            print('Please enter a NUMBER (1-100)!')

    if user_guess == computer_guess:
        print('Hoora! You win')
        break
    else:
        print('No')
        if user_guess < computer_guess:
            print('Your number is smaller')
        elif user_guess > computer_guess:
            print('Your number is bigger')
        print('You have {} turn'.format(4 - i))
else:
    print('You Loose. The number was ' + str(computer_guess))