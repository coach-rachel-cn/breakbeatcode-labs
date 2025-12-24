#######################################################
# CODE NEXT - BREAKBEATCODE
# Week 1: Intro to EarSketch & Python
# Lab 1 KEY: Variables, User Input & Musical Mad Libs
#######################################################

# INSTRUCTOR-FACING KEY #
# NOTE: The solutions below represent only one of many possible solutions
# to the lab challenges

# this statement imports the earsketch module
from earsketch import *

# PART 1 - WORKING WITH VARIABLES
# Create a variable called djname that stores your stage name
# Type your stage name in between the quotation marks!
djname = "DJ Edge"

# Create a variable called age that stores your current age
age = 16

# Print your djname to the console
print(djname)

# Print your djname variable in a sentence of some sort
# Example: "Please welcome to the stage, {DJ NAME}!"
print("Please welcome to the stage " + djname)


# Print your age to the console in a sentence, such as "{NAME} is {AGE} years old"
# Hint: if you run into an error, try searching up the Python str() function
# The int() function here is used to convert the number 16 to a string "16" so 
# it can be used in a sentence. Without it, the computer will show an error message
# because Python cannot combine strings with integers
print(djname + " is " + str(age) + " years old")

# Uncomment the lines below to see what the output to the console is
# Think about it: what does the type() function appear to do?
# print(type(djname))
# print(type(age))

# type() returns the data type of whatever was enclosed in the parentheses

###########################################

# PART 2 - USER INPUT
# uncomment the lines below to observe how it works
# name = input("What is your name? ")
# print("Hello, " + name)


# create a variable called genre that asks & stores what the user's favorite genre of music is
# genre = input("What is your favorite genre of music? ")

# create a variable called artist that asks and stores who the user's favorite artist is
# artist = "Who is your favorite artist? "

# Print a statement that expresses the user's favorite genre and artist, such as:
# "{NAME}'s favorite genre of music is {GENRE} and their favorite artist is {ARTIST}"
# print(name + "'s favorite genre of music is " + genre + " and their favorite artist is " + artist)


###########################################

# PART 3 - MAKE SOME MUSIC
# this function sets the tempo (speed) of your song - try changing the number!
setTempo(120)

# explore the sounds library and find 3 sounds that you like
# Store your sounds in variables like the example on line 60
beat1 = COMMON_LOVE_DRUMBEAT_1

# your sounds here!
guitar = BOYKINZ_NIGHT_THEME_GUITAR_1
bass = ENTREP_THEME_BASS_1
piano = AK_UNDOG_PIANO_2

# play your sounds using the function insertMedia()
# insertMedia() takes 3 arguments - the sound, the track you want the sound to play on, 
# and what bar to start the sound
# uncomment line 70 to play the sound stored in the beat1 variable on track 1 at bar 1
# insertMedia(beat1, 1, 1)

# use insertMedia() to play your sounds on various tracks in various measures
# insertMedia(guitar, 2, 2)
# insertMedia(bass, 3, 6)
# insertMedia(piano, 4, 8)



# now for something a little different - comment out the insertMedia() lines above and comment in line 81
# what seems to be going on here? If you're not sure, use the API tab on the left 
# to search up the fitMedia() function
# How are insertMedia() and fitMedia() similar? Different?
# fitMedia(beat1, 1, 1, 9)

# fitMedia takes an ending measure, so the sound loops until the specified end measure


# PART 4 - MUSICAL MAD LIBS!
# GOAL: Create an 8 bar musical snippet given a random comibination of adjectives and keywords!
# Aim for incorporating 3+ sounds stored in variables

# TIP: you might want to comment out lines of code from above as you work on this challenge

# Code your musical mad libs below!


