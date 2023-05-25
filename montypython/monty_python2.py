#!/usr/bin/env python3

# This is code that I created while following along. It needs to be improved with lots of comments in the future.
# Make sure you SPACE and NOT TAB over. 4 spaces for while loop, 8 spaces for if, elif, break, else inside the while loop

round = 0

while True:
    round = round + 1
    print('Finish the movie title, "Monty Python\'s The Life Of _____"')
    answer = input("Your guess--> ")
    if answer == 'Brian':
        print('Correct!')
        break
    elif round == 3:
        print('Sorry, the answer was Brian.')
        break
    else:
        print('Sorry, Try again!')


