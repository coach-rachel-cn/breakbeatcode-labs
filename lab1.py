#######################################################
# CODE NEXT - BREAKBEATCODE
# Week 1: Intro to EarSketch & Python
# Lab 1: Variables, User Input & Musical Mad Libs 
#######################################################

# This statement imports the earsketch module
from earsketch import *

# PART 1 - WORKING WITH VARIABLES (Pure Python)
# EXAMPLE - create a variable that stores your name
name = "YOUR NAME HERE"

# This is a new function! Uncomment the next line by deleting the #
# Run the code - what does print() do?
# print(name)

# Here is a way to combine strings (characters in quotes) and variables
# This is called CONCATENATION - uncomment and run the code!
# print("My name is " + name + "!")


# YOUR TURN! Create a variable called dj_name that stores your stage name
# Type your stage name in between the quotation marks!
dj_name = "YOUR STAGE NAME HERE"

# Print your stage name to the console


# Now print your stage name to the console in a sentence, such as
# "Please welcome to the stage, {DJ NAME}!"


# We can also store numbers in variables!
# Create a variable called age that stores your current age


# Print your age to the console


# Now print your age to the console in a sentence, such as
# "I am {AGE} years old"


# Hmmm...did you run into an error? Try searching up the Python str() function
# What did you find out about this function? How did you fix the error?


# Now let's combine variables. Print out a sentence that uses both the name, stage name,
# and age variables, such as "{NAME}, AKA {STAGE NAME} is {AGE} years old!"





# Uncomment the the two lines below to see what the output to the console is
# Think about it: what does the type() function appear to do?
# print(type(dj_name))
# print(type(age))


###########################################

# PART 2 - USER INPUT
# EXAMPLE - uncomment the lines below to observe how the input() function works
# new_name = input("What is your name? ")
# print("Hello, " + new_name)


# YOUR TURN! Create a variable called genre that asks & stores what the user's favorite genre of music is


# Create a variable called artist that asks and stores who the user's favorite artist is



# Print a statement that expresses the user's favorite genre and artist, such as:
# "{NAME}'s favorite genre of music is {GENRE} and their favorite artist is {ARTIST}"



###########################################

# PART 3 - MAKE SOME MUSIC
# This function sets the tempo (speed) of your song - try changing the number!
setTempo(120)

# Explore the sounds library and find 3 sounds that you like
# Store your sounds in variables like the example on line 60
beat1 = COMMON_LOVE_DRUMBEAT_1

# your sounds here!



# Play your sounds using the function insertMedia()
# insertMedia() takes 3 arguments - the sound, the track you want the sound to play on, 
# and what bar to start the sound
# Uncomment the next line to play the sound stored in the beat1 variable on track 1 at bar 1
# insertMedia(beat1, 1, 1)

# Use insertMedia() to play your sounds on various tracks in various measures




# Now for something a little different - comment out the insertMedia() lines above and comment in line 81
# What seems to be going on here? If you're not sure, use the API tab on the left 
# to search up the fitMedia() function
# How are insertMedia() and fitMedia() similar? Different?
# fitMedia(beat1, 1, 1, 9)


###########################################

# PART 4 - MUSICAL MAD LIBS!
# GOAL: Create an 8 bar musical snippet given a random comibination of adjectives and keywords!
# Aim for incorporating 3+ sounds stored in variables

# TIP: you might want to comment out lines of code from above as you work on this challenge

# Code your musical mad libs below!











