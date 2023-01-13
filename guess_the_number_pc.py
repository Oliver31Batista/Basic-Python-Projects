import random


def guess_the_number_pc(x):
    print("===============================================")
    print("Welcome to the game.")
    print("===============================================")
    print(f"Select one number between 1 and {x} for the pc to try to guess...")  

    lower_limit = 1
    top_limit = x

    response = ""

    while response != "c":
        #generate prediction
        if lower_limit != top_limit:
            prediction = random.randint(lower_limit, top_limit)
        else:
            prediction = lower_limit
        
        #Get the response from the user
        response = response = input(f"My prediction is {prediction}. If is to large, type (A). If is to small, type (B). If is correct, type (C): ").lower()

        if response == "a":
            top_limit = prediction - 1
        elif response == "b":
            lower_limit = prediction + 1

    print(f"¡Congratulations! The computer guess your number correctly: {prediction}")


guess_the_number_pc(31)   