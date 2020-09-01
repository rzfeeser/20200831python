#!/usr/bin/python3
round = 0
answer = " "

# a python dictionary of possible answers
correctanswers = {
        "brian": "correct",
        "shrubbery": "We are no longer the knights who say Ni! We are now the knights who say ekki-ekki-ekki-pitang-zoom-boing!",
        "tim": "Oh great wizard! What do they call you?\nWizard: Some call me... Tim..."
        }


while round < 3:

    round += 1     # increase the round counter by 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')

    # transform answer into something "common" to test
    answer = answer.lower()

    # if what the user typed in is "brian", "shrubbery", or "tim"
    if answer in correctanswers:
        print(correctanswers.get(answer))
        break
    # if counter reaches 3
    elif round == 3:    # logic to ensure round has not yet reached 3
        print("Sorry, the answer was Brian.")
    else:                 # if answer was wrong
        print("Sorry. Try again!")


# say goodbye!
print("Thanks for playing!")
