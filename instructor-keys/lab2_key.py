#######################################################
# CODE NEXT - BREAKBEATCODE
# Week 2: Conditionals & Musical Decision Making
# Lab 2 KEY: Conditionals, Decisions, Dynamic DJ Set
#######################################################

# INSTRUCTOR-FACING KEY #
# NOTE: The solutions below represent only one of many possible solutions
# to the lab challenges

from earsketch import *
from random import randint

# PART 1 - CONDITIONALS PRACTICE

#Example 1 - Magic Spell 
# Create a variable called magic_spell and 
#ask for input from the use to say the magic spell
# magic_spell = input("What is the magic spell?")

# #Check to see if the magic_spell is equal to 
# #Abracadabra, the spell used for opening doors
# if magic_spell == "Abracadabra":
    
# #If the user responds with the right magic spell, 
# #Abracadabra,then show "The door is open on the screen" 
#   print("The door is open")
# else:
# #else, show "The door is still locked on the screen"
#   print("The door is still locked.")



# Example 2 - Secret Number
# secret_number = 12 #change this value if you'd like!
# guess = input("Guess the secret number: ")

# # If the guess is less than the secret number
# if guess < secret_number:
#     print("Too low!")
# # If the guess is higher than the secret number
# # Use elif to add another branch to the conditional
# elif guess > secret_number:
#     print("Too high!")
# # Else (the only other option), the guess is correct!
# else:
#     print("You guessed the secret number!")


    
# YOUR TURN! 
# 1. Write a conditional to detect whether a number is positive,
# negative, or zero
# number = float(input("Enter any number: "))

# if number > 0:
#     print("Your number is positive")
# elif number == 0:
#     print("Your number is zero")
# else:
#     print("Your number is negative")


# 2. Write a conditional to determine a student's letter grade based
# on their numerical score
# Resource: https://bigfuture.collegeboard.org/plan-for-college/get-started/how-to-convert-gpa-4.0-scale
# numberGrade = int(input("What was your grade? "))

# if numberGrade >= 90:
#     print("Letter Grade = A")
# elif numberGrade >= 82 and numberGrade <= 89:
#     print("Letter Grade = B")
# elif numberGrade >= 70 and numberGrade <= 79:
#     print("Letter Grade = C")
# elif numberGrade >= 65 and number <= 69:
#     print("Letter Grade = D")
# else:
#     print("Letter Grade = F")


# 3. Write a conditional that checks a user's age and
# determines what movies they can see based on MPAA ratings (G/PG/PG-13/R)
# Make sure to ask the user for their age and store it in a variable
# ageForMovies = int(input("Welcome to the movies! What is your age? "))

# if ageForMovies >= 18:
#     print("Suited for all movies, including rated R movies")
# elif ageForMovies >= 17 and ageForMovies <= 13:
#     print("For your age bracket, you're suited for PG-13 movies")
# else:
#     print("Good for rated G movies. Parents should note PG movies may contain some material that may not be suitable for children")

    

# 4. Write a conditional that takes in a user's age and
# determines if that user is old enough to vote. If they
# are not old enough to vote, print out how many years they
# have to wait until they can vote

# ageToVote = int(input("How old are you? "))  

# if ageToVote < 18:
#     print("You are not old enough to vote")
#     print("You have to wait " + str(18-ageToVote) + " more years to vote!")
# else: 
#     print("You are able to vote!")    

# 5. Write a conditional that takes in a genre of music and 
# plays a sound based on the genre selected by the user
# Include 3 or more genres of music that the user can choose from
# Tip: what if there's a typo in the user input? 
# Can you think of ways to account for human error in your code?

# genreOfMusic = input("Give a genre of music: ")

# if genreOfMusic == "Rock" or genreOfMusic == "rock":
#     playableMusic = RD_ROCK_POPLEADSTRUM_GUITAR_2
# elif genreOfMusic == "Rap" or genreOfMusic == "rap":
#     playableMusic = CIARA_MELANIN_DRUMBEAT_2
# elif genreOfMusic == "Pop" or genreOfMusic == "pop":
#     playableMusic = RD_POP_MAINBEAT_7
# else:
#     print("Genre doesn't exist at the moment or you have a typo")
#     print("Here are some horns for now")
#     playableMusic = Y03_HORNS_1
    
# Click the green play button to play sound
# fitMedia(playableMusic, 1, 1, 8)


##############################

# PART 2 - CONDITIONALS x EARSKETCH

setTempo(120)

# 1. GENRE PREFERENCES
# a) Create three variables that have sounds from three different genres (house, funk, etc.)
# b) Ask a user what their preferred genre of music is out of the three and
# c) Write a conditional statement to determine what sound to play
# d) Stretch: what happens if the user types in all caps/lower/mixed case? Can you
#    use a string method to account for this? https://www.w3schools.com/python/python_ref_string.asp

funk = YG_FUNK_BRASS_1
house = HOUSE_BREAKBEAT_001
edm = EIGHT_BIT_ANALOG_DRUM_LOOP_002

# preferred = input("What is your favorite genre? Choose funk, house, or edm: ")

# using the lower() method to make all input lowercase
# if preferred.lower() == "funk":
#     insertMedia(funk, 1, 1)
# elif preferred.lower() == "house":
#     insertMedia(house, 1, 1)
# elif preferred.lower() == "edm":
#     insertMedia(edm, 1, 1,)
# else:
#     print("There was a typo!")

# 2. TEMPO AND GENRE
# a) Find a beat pattern that you like and store it in a variable
# b) Ask a user what their preferred genre of music is using the genres on this resource:
#    https://learningmusic.ableton.com/make-beats/tempo-and-genre.html
# c) Based on the user's choice, play the drum pattern at a random tempo in the specified
#    range for that genre, as indicated on the Ableton resource 
#    Hint: look at line 7 for a clue about random

# beat = CIARA_MELANIN_DRUMBEAT_2
# genre = input("What is your preferred genre of music? Choose hip-hop, house, or dubstep: ").lower()

# if genre == "hip-hop":
#     setTempo(randint(60, 100))
# elif genre == "house":
#     setTempo(randint(115, 130))
# else:
#     setTempo(randint(135, 145))

# insertMedia(beat, 1, 1)


# 3. CHOOSE AN ARTIST
# a) Create three variables that have vocals from three different artists
# b) Ask a user to choose one artist from the three choices and
# c) Write a conditional statement to determine what sound to play

ciara = CIARA_SET_VOX_PRE_1
khalid = KHALID_NORM_VOX_LEAD_CHORUS_1
common = COMMON_LOVE_VOX_COMMON_1

# artist = input("Who is your preferred artist? Choose Ciara, Khalid, or Common: ").lower()

# if artist == "ciara":
#     insertMedia(ciara, 1, 1,)
# elif artist == "khalid":
#     insertMedia(khalid, 1, 1)
# else:
#     insertMedia(common, 1, 1)

# 4. MOOD MUSIC
# a) Ask the user how they are feeling today - happy, sad, excited, etc.
# b) Write a conditional statement that plays short 4-8 bar samples with multiple 
#    sounds according to the emotion the user selected. Think about what sounds
#    might represent different emotions. 
# c) Music Theory note: You might consider filtering sounds by KEY, where major
#    keys tend to have a happier/cheerful sound and minor keys sound more somber





# 5. FREESTYLE! You choose what you compose - make a groove, beat, or remix that
# uses conditionals in some way. Consider taking in user input with input() and/or
# incorporating the randint() function that you explored above





