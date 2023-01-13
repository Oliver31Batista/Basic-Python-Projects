import random


def play():
    user = input("Choose one option to play:\n 1)Rock\n 2)Paper\n 3)Scissors \nYour choice: ").lower()
    computer = random.choice(['rock', 'paper', 'scissors'])

    if user == computer:
        return print(f'{user} vs {computer} = ¡TIE!')
    
    if player_win(user, computer):
        return print(f'{user} vs {computer} = ¡YOU WIN!')

    return print(f'{user} vs {computer} = ¡YOU LOSE!')


def player_win(user, opponent):
    if (user == 'scissors' and opponent == 'paper' or
        user == 'rock' and opponent == 'scissors' or
        user == 'paper' and opponent == 'rock' ):
        return True
    else:
        return False


play()