#!/usr/bin/env python3

"""This script helps you decide what to eat and will eventually prepare a shopping list for you"""

# Create a menu using dictionary and key value pairs
menu={"steak":['t-bone','sirloin','ribeye'],"chicken":['grilled','fried','baked'],"pasta":['pesto','alfredo','lasagna']}

# display the menu choices to user
print('press 1 for steak')
print('press 2 for chicken')
print('press 3 for pasta',end='\n')

# prompt user to choose between beef chicken or pasta

choice= input('Please pick a number ---> ')
print('Great, here are the options for ' + choice) and int(choice)

round = 0

while round < 3 and (int(choice) != '1' or '2' or '3'):

    round += 1
    if int(choice) == 1:
        print(menu["steak"])
        break
    elif int(choice) ==2:
        print(menu["chicken"])
        break
    elif int(choice) ==3:
        print(menu["pasta"])
        break
    else:
        print('Maybe you\'re not hungry?, please choose a number between 1-3')














# Here's what you should eat based on your response



# Here are some cool recipes



# followed by a shopping list
