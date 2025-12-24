#######################################################
# CODE NEXT - BREAKBEATCODE
# Week 3: Python Lists
# Lab 3 KEY: Lists, Mood Music, MusicFX
#######################################################

# INSTRUCTOR-FACING KEY #
# NOTE: The solutions below represent only one of many possible solutions
# to the lab challenges

from earsketch import *
from random import randint, choice

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
print(anagrams[2])


# 2. The word "opts" is also an anagram of the word "stop". 
# Find a way to add "opts" to the end of the list.
anagrams.append("opts")


# 3. The word "puts", on the other hand, is not an anagram of the word "stop". 
# Find a way to replace it with the word "pots".
anagrams[3] = "pots"



# 4. Use the documentation to figure out what the method ".pop()" does.
# Now use it to remove the word "plots" (which isn't a correct anagram of "stop") from our list.
anagrams.pop(0)


# 5. Put the final list of anagrams in alphabetical order
anagrams.sort()


# This code prints the list after you've manipulated it above.
print(anagrams)



##############################

# PART 2 - LISTS x EARSKETCH

setTempo(120)

# 1. GENRE PREFERENCES
# a) Create three lists that have sounds from three different genres (house, funk, etc.)
# b) Ask a user what their preferred genre of music is out of the three and
# c) Play a random sound from the user's chosen genre (Hint: look at line 7 for a clue about random)

funk = [YG_FUNK_BRASS_1, YG_FUNK_CONGAS_1, YG_FUNK_ELECTRIC_PIANO_1]
house = [HOUSE_BREAKBEAT_001, HOUSE_DEEP_CRYSTALCHORD_001, HOUSE_MAIN_BEAT_001]
latin = [IRCA_BOMBA_CONJUNTOS_CUEMBE, IRCA_BOMBA_HOLANDE_ELEC_GUITAR_PRI, IRCA_LATIN_JAZZ_1_PIANO_2]

# genre = input("Choose a genre of music [funk, house, or latin]: ").lower()
# num = randint(0, 2)
# if genre == "funk":
#     insertMedia(funk[num], 1, 1)
# elif genre == "house":
#     insertMedia(house[num], 1, 1)
# elif genre == "latin":
#     insertMedia(latin[num], 1, 1)
# else:
#     print("Error!")

# 2. CHOOSE AN ARTIST
# a) Create a list of sample sounds from various artists in the EarSketch library
# b) Ask a user who their preferred artist is out of the artists you chose, or if
#    they don't know, they can opt for a random artist from the list
# c) Play a sound based on the user's choice; also think about ways your code can
#    account for typos (capitalization, spelling, etc.) to make it more flexible

artists = [AK_UNDOG_VOCAL_BKUP_5, COMMON_LOVE_VOX_CHOIR_1, KHALID_NORM_VOX_HARMONY_3]

# artistPick = input("Choose your favorite artist (Alicia Keys, Khalid, Common, or not sure):" )

# if artistPick == "AK" or artistPick == "Alicia Keys" or artistPick == "ALICIA KEYS" or artistPick == "Keys":
#     artistPlay = artists[0]
# elif artistPick == "Common" or artistPick == "COMMON" or artistPick == "common":
#     artistPlay = artists[1]
# elif artistPick == "Khalid" or artistPick == "KHALID" or artistPick == "khalid":
#     artistPlay = artists[2]
# else:
#     # this solution uses the choice() method from the random module
#     artistPlay = choice(artists)

# fitMedia(artistPlay, 1, 1, 5)



# 3. RANDOM GROOVE
# a) You are going to randomly generate a groove with drums, guitar, and bass. First
#    create lists for each instrument and populate them with four or more sounds each:

drums = [AK_UNDOG_PERC_CYMB_1, CIARA_SET_PERC_HIHAT_2, DUBSTEP_DRUMLOOP_MAIN_004, HIPHOP_DUSTYGROOVE_001]
guitar = [Y05_GUITAR_1, TFLAMES_OC_GUITARS_VRS_2, TFLAMES_OMEN_GUITARS_2_VRS, Y01_GUITAR_1]
bass = [RD_EDM_WARMBASSLINE_1, RD_EDM_WOBBLEBASS_1, RD_ELECTRO_RAWBASSLINE_2, RD_POP_TB303BASSLINE_1]

# b) The user selects a number 1-4 to dictate what sound should play for each instrument

# instrumentPick = input("Choose a number from 1 to 4: ")

# remember when using input(), everything is a string!
# if instrumentPick == "1":
#     pickNum1 = drums[0]
#     pickNum2 = guitar[0]
#     pickNum3 = bass[0]
# elif instrumentPick == "2":
#     pickNum1 = drums[1]
#     pickNum2 = guitar[1]
#     pickNum3 = bass[1]
# elif instrumentPick == "3":
#     pickNum1 = drums[2]
#     pickNum2 = guitar[2]
#     pickNum3 = bass[2]
# elif instrumentPick == "4":
#     pickNum1 = drums[3]
#     pickNum2 = guitar[3]
#     pickNum3 = bass[3]
# else:
#     pickNum1 = random.choice(drums)
#     pickNum2 = random.choice(guitar)
#     pickNum3 = random.choice(bass)


# c) Create the groove by playing the corresponding sounds selected by the user
#    The user chose a number 1-4, so remember to think about list indexes accordingly
#    Make sure that all of the sounds will play for the same number of measures

# fitMedia(pickNum1, 1, 1, 5)
# fitMedia(pickNum2, 2, 1, 5)
# fitMedia(pickNum3, 3, 1, 5)


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





