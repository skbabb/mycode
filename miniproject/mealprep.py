#!/usr/bin/env python3

""" This script helps you decide what to eat and will prepare a recipe for you as well"""

# First import the module that will assist in requesting information from the internet
import requests

# Your Edamam API credentials (from the food recipe API website)
#API_ID = "YOUR_API_ID"
#API_KEY = "YOUR_API_KEY"

# Dictionary meal options for a menu
menu = {
    "steak": ["Ribeye steak", "Potatoes", "Green beans", "Salt", "Pepper", "Olive oil"],
    "chicken": ["Chicken breasts", "Brown rice", "Broccoli", "Garlic", "Soy sauce", "Olive oil"],
    "pasta": ["Pasta", "Tomato sauce", "Ground beef", "Onion", "Garlic", "Parmesan cheese"],
}

# Function to help user decide what to eat
def decide_meal():
    print("Welcome! Let's decide what to eat.")
    print("Please choose one of the following options:")
    print("1. Steak")
    print("2. Chicken")
    print("3. Pasta")

    while True: # While any of these 1-3 options are true
        # create object named choice to equal a function
        choice = input("Enter the number of your choice (1-3): ")

        if choice == "1":
            return "steak"
        elif choice == "2":
            return "chicken"
        elif choice == "3":
            return "pasta"
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

# Function to fetch recipes from the Edamam API
def fetch_recipes(meal):
    # f string the url to avoid any errors such as integer vs string?
    url = f"https://api.edamam.com/search?q={meal}&app_id={API_ID}&app_key={API_KEY}&from=0&to=5"

# response object using request argument import.
    response = requests.get(url)
#NEED HELP FROM THIS POINT
    if response.status_code == 200:
        data = response.json()
        hits = data.get("hits", [])

        if hits:
            recipes = [hit["recipe"]["label"] for hit in hits]
            return recipes

    return []

# Main program
def main():
    meal_choice = decide_meal()
    grocery_list = menu.get(meal_choice, [])
    recipes = fetch_recipes(meal_choice)

    if grocery_list:
        print("Here's your grocery list for", meal_choice + ":")
        for item in grocery_list:
            print("- " + item)

    if recipes:
        print("\nHere are some recipe ideas for", meal_choice + ":")
        for recipe in recipes:
            print("- " + recipe)
    else:
        print("Invalid meal choice. Grocery list not available.")

if __name__ == "__main__":
    main()

