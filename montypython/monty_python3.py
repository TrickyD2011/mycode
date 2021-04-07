#!/usr/bin/python3
"""System variables"""
ROUND = 0
ANSWER = " "
mylist = ('brian', 'shrubbery')

"""System Module"""
while ROUND < 3 and ANSWER.lower() not in mylist:
    ROUND += 1     # increase the round counter by 1
    ANSWER = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
    if ANSWER.lower() == "brian": # logic to check if user gave correct answer
        print("Correct!")
    elif ROUND == 3:    # logic to ensure round has not yet reached 3
        print("Sorry, the answer was Brian.")
    elif ANSWER.lower() == "shrubbery": #secret answer
        print("You gave the super secret answer!")
    else:                 # if answer was wrong
        print("Sorry. Try again!")
