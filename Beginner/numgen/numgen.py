import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}\n'))

        if guess < random_number:
            print(f"Sorry but that is too low!\n")
        elif guess > random_number:
            print(f"Sorry but that is too high!\n")
        
    print(f"Congrats! You have guessed the right number, {random_number}!!!!\n")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low # Could be high because low == high in this case
        feedback = input(f"Is {guess} too high? (H), low (L), or correct (C)?".lower())

        if feedback == 'h':
            high = guess - 1
        if feedback == "l":
            low = guess + 1
    print(f"Yay, the computer wins! He guessed {guess} correctly!")


computer_guess(1000)