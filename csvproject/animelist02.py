#!/usr/bin/env python3

# import the csv module
import csv

# This is the csv file being used
# url = https://raw.githubusercontent.com/csfeeser/Python/master/data%20sets/animelist.csv


# def manga(name):
  
  # open the csv file you created in read mode and make it an object
with open("animelist.csv", "r") as mangafile:

    #counter to start at the top row of data
    i = 0
  #
    for row in csv.reader(mangafile):
        i = i + 1
        name = row[0]
        episodes = row[2]

        print(name,episodes)

        



