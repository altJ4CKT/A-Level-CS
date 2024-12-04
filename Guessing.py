import random

guessed = False
number = random.randint(1, 20)
numbers_guessed = []


while not guessed:
    print(f"The numbers you have guessed so far: ")
    for i in numbers_guessed:
        print(i)
    guess = input("Guess a number between 1 and 20: ")
    numbers_guessed.append(guess)
    if int(guess) == number:
        guessed = True
    else:
        print("Try again!")
        
if guessed:
    number_tries = len(numbers_guessed)
    if number_tries <= 5:
        print("Well done, you are genius")
    elif number_tries > 5 and number_tries <= 10:
        print("Well done good work")
    elif number_tries > 10 and number_tries <= 15:
        print("Well done, finally you got it")
    elif number_tries > 15 and number_tries <= 20:
        print("Well done")
    elif number_tries > 20:
        print("I am bored! good luck next time!")
