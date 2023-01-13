import random


def guess_the_number(x):

    print("===============================================")
    print("Welcome to the game.")
    print("===============================================")
    print("You goal is to guess the number generated by the computer.")    

    random_number = random.randint(1, x) 

    prediction = 0

    while prediction != random_number:
        prediction = int(input(f"Guess one number between 1 and {x}: "))

        if prediction < random_number:
            print("Try again. This number is too small.")
        elif prediction > random_number:
            print("Try again. This number is too large.")
        
    print(f"¡Congratulations! You guessed the number {random_number} correctly.")    


guess_the_number(31)