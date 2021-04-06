#!/usr/bin/python3
round = 0
answer = " "
mylist = ('brian', 'shrubbery')

while round < 3 and answer.lower() not in mylist:
    round += 1     # increase the round counter by 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
    if answer.lower() == "brian": # logic to check if user gave correct answer
        print("Correct!")
    elif round == 3:    # logic to ensure round has not yet reached 3
        print("Sorry, the answer was Brian.")
    elif answer.lower() == "shrubbery": #secret answer
        print("You gave the super secret answer!")
    else:                 # if answer was wrong
        print("Sorry. Try again!")

