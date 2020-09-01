#!/usr/bin/python3
round = 0
answer = " "

while round < 3 and answer != "brian" and answer != "shrubbery" and answer!= "tim":
    round += 1     # increase the round counter by 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')

    # transform answer into something "common" to test
    answer = answer.lower()

    # Correct Answer
    if answer == "brian":
        print("Correct!")
    # Easter Egg
    elif answer == "shrubbery":
        print("We are no longer the knights who say Ni! We are now the knights\
who say ekki-ekki-ekki-pitang-zoom-boing!")
    # Easter Egg 2
    elif answer == "tim":
        print("Oh great wizard! What do they call you?\nWizard: Some call me... Tim...")
    # if counter reaches 3
    elif round == 3:    # logic to ensure round has not yet reached 3
        print("Sorry, the answer was Brian.")
    else:                 # if answer was wrong
        print("Sorry. Try again!")
