import random

def play():
    user = input('What\'s your choice?' + "'r' for rock, 'p' for paper, or 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It\'s a tie"

    # r > s , s > p, p > r
    if is_win(user, computer):
        return 'You won!'


    return 'You lost!'


def is_win(player, op):
   # Return true if player wins 
   if (player == 'r' and op == 's' or player == 's' and op == 'p' or player == 'p' and op == 'r'):
       return True

print(play())