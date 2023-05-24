#!/usr/bin/env python3

# From this list, create a print function that outputs "My eyes! The goggles do nothing!"

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]

trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]

nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

# part 1
# gather data

eyes = challenge[2][1]
goggles = challenge [2][0]
nothing = challenge [3]

print(f"My {eyes}! The {goggles} do {nothing}!")

# part 2

# eyes = trial[2]['goggles']
# goggles = trial[2].get('eyes')
# nothing = trial[3] 

# part 3

