import random


def play():
    user = input("Choose one option to play:\n 1)Rock\n 2)Paper\n 3)Scissors \nYour choice: ").lower()
    computer = random.choice(['rock', 'paper', 'scissors'])

    if user == computer:
        return '¡TIE!'
    
    if player_win(user, computer):
        return '¡YOU WIN!'

    return '¡YOU LOSE!'


def player_win(user, opponent):
    if (user == 'scissors' and opponent == 'paper' or
        user == 'rock' and opponent == 'scissors' or
        user == 'paper' and opponent == 'rock' ):
        return True
    else:
        return False


print(play())