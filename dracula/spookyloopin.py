#!/usr/bin/env python3

# create a file object of the dracula novel
# Read in the content of the Dracula novel as a file object

counter = 0


with open("dracula.txt", 'r') as foo:
    # with opening (this file in read mode) as foo
    # foo is a placeholder for a value that can change depending on conditions or info



    with open("vampytimex.txt",'w') as fang:
        # opens a txt and renames as fang for obj

        #Loop over every line in Dracula, print each line out!
        for line in foo:
             # for every line in foo(which remember is a placeholder for changed variable)

        #Actually, fix that, only print out the line if it has the word vampire in it!
            if "vampire" in line.lower():
                # if "this word" is in there regardless of case
                print(line)
                # print this line

                # Count that up! How many lines contain the word vampire?
                counter += 1 
                
""" Take the lines from Dracula that have vampire in it and write them to a second file named vampytimes.txt."""

                fang.write(line)
                # and write it to the fang obj/file


    print(counter)
    # print the full counter


""" I know this doesn't make total sense. It is a mixture of two different tasks that I am compiling together to remember the different options. I will make two different vim files once i have more time."""
