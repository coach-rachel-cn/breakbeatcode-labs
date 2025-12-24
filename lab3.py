#######################################################
# CODE NEXT - BREAKBEATCODE
# Week 3: Python Lists
# Lab 3: Lists, Mood Music, MusicFX
#######################################################

from earsketch import *
from random import randint

# PART 1 - LISTS
# Lists are ordered collections of items, like strings, numbers,
# variables, sounds, or even lists of lists
# Here is an example:

# fruits = ["apple", "banana", "orange"]

# Predict: What will this output to the console?
# print(fruits[0])

# To modify a list element, assign a new value to its index
# fruits[1] = "grape"

# What will this print to the console?
# print(fruits[1])

# Use the len() function to determine a list's length
# print(len(fruits))

# Use the append() method to add elements to the end of a list
# fruits.append("pear")
# print(fruits)


# YOUR TURN - ANAGRAMS
# As you may know, an anagram is a new word created by reorganizing all the letters in a word.
# This list of anagrams are all based on the word "Stop"
anagrams = ["plots", "post", "stop", "puts", "tops"]

# Run this program after you try each step and see if it worked.
# At the very bottom of section is a line of code that prints out the list after your code is run.
# You're welcome to print additional debugging statements if you need.

# 1. Print out the third word in the list using bracket notation.





# 2. The word "opts" is also an anagram of the word "stop". 
# Find a way to add "opts" to the end of the list.





# 3. The word "puts", on the other hand, is not an anagram of the word "stop". 
# Find a way to replace it with the word "pots".





# 4. Use the documentation to figure out what the method ".pop()" does.
# Now use it to remove the word "plots" (which isn't a correct anagram of "stop") from our list.





# 5. Put the final list of anagrams in alphabetical order




# This code prints the list after you've manipulated it above.
print(anagrams)




##############################

# PART 2 - LISTS x EARSKETCH

setTempo(120)

# 1. GENRE PREFERENCES
# a) Create three lists that have sounds from three different genres (house, funk, etc.)
# b) Ask a user what their preferred genre of music is out of the three and
# c) Play a random sound from the user's chosen genre (Hint: look at line 7 for a clue about random)





# 2. CHOOSE AN ARTIST
# a) Create a list of sample sounds from various artists in the EarSketch library
# b) Ask a user who their preferred artist is out of the artists you chose, or if
#    they don't know, they can opt for a random artist from the list
# c) Play a sound based on the user's choice; also think about ways your code can
#    account for typos (capitalization, spelling, etc.) to make it more flexible

artists = []



# 3. RANDOM GROOVE
# a) You are going to randomly generate a groove with drums, guitar, and bass. First
#    create lists for each instrument and populate them with four or more sounds each:

drums = []
guitar = []
bass = []

# b) The user selects a number 1-4 to dictate what sound should play for each instrument



# c) Create the groove by playing the corresponding sounds selected by the user
#    The user chose a number 1-4, so remember to think about list indexes accordingly
#    Make sure that all of the sounds will play for the same number of measures





# 4. MOOD MUSIC PART 2
# We're going to expand on the mood music code you wrote from the last lab using lists:
# a) Choose three emotions (happy, sad, excited, etc.). These can be the same as last
#    time or different! Create three lists: one to store melodies, one to store bass lines,
#    and one to store drum/beat patterns.
# b) Populate each list with sounds that you think emulate your chosen emotions. The order
#    of your sounds will matter - if you choose "happy" as an emotion, your happy melody 
#    should be at the same list index as your happy bass sound and happy beat pattern.
# c) Ask the user how they are feeling, and use a conditional statement to play the sounds
#    from the list corresponding to the emotion they selected





# 5. FREESTYLE! You choose what you compose - make a groove, beat, or remix that
# uses lists in some way. Consider taking in user input with input(), using randint(),
# and/or using conditional statements to influence the program output





##############################

# PART 3 - EARSKETCH X MUSICFX
# Create an 8-16 measure composition featuring a sound you created with AI in MusicFX
# Link to MusicFX: https://labs.google/fx/tools/music-fx
# Download your 30 second sound from MusicFX and upload it in the Sounds tab of EarSketch by choosing +Add sound
# Once a sound is uploaded, you will see your EarSketch username as the artist for that sound
# See what you can create by combining your Python & EarSketch skills with MusicFX!
# Try to incorporate the Python concepts we've practiced to date: variables, user input, conditionals, and lists




