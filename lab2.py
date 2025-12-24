#######################################################
# CODE NEXT - BREAKBEATCODE
# Week 2: Conditionals & Musical Decision Making
# Lab 2: Conditionals, Decisions, Dynamic DJ Set
#######################################################

from earsketch import *
from random import randint

# PART 1 - CONDITIONALS PRACTICE (Pure Python)

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



# 2. Write a conditional to determine a student's letter grade based
# on their numerical score
# Resource: https://bigfuture.collegeboard.org/plan-for-college/get-started/how-to-convert-gpa-4.0-scale



# 3. Write a conditional that checks a user's age and
# determines what movies they can see based on MPAA ratings (G/PG/PG-13/R)
# Make sure to ask the user for their age and store it in a variable

    

# 4. Write a conditional that takes in a user's age and
# determines if that user is old enough to vote. If they
# are not old enough to vote, print out how many years they
# have to wait until they can vote

    

# 5. Write a conditional that takes in a genre of music and 
# plays a sound based on the genre selected by the user
# Include 3 or more genres of music that the user can choose from
# Tip: what if there's a typo in the user input? 
# Can you think of ways to account for human error in your code?





##############################

# PART 2 - CONDITIONALS x EARSKETCH

setTempo(120)

# 1. GENRE PREFERENCES
# a) Create three variables that have sounds from three different genres (house, funk, etc.)
# b) Ask a user what their preferred genre of music is out of the three and
# c) Write a conditional statement to determine what sound to play
# d) Stretch: what happens if the user types in all caps/lower/mixed case? Can you
#    use a string method to account for this? https://www.w3schools.com/python/python_ref_string.asp





# 2. TEMPO AND GENRE
# a) Find a beat pattern that you like and store it in a variable
# b) Ask a user what their preferred genre of music is using the genres on this resource:
#    https://learningmusic.ableton.com/make-beats/tempo-and-genre.html
# c) Based on the user's choice, play the drum pattern at a random tempo in the specified
#    range for that genre, as indicated on the Ableton resource 
#    Hint: look at line 7 for a clue about random





# 3. CHOOSE AN ARTIST
# a) Create three variables that have vocals from three different artists
# b) Ask a user to choose one artist from the three choices and
# c) Write a conditional statement to determine what sound to play




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



##############################

# PART 3 - DYNAMIC DJ SET
# Create and 8-16 measure composition where some aspect of the music changes based
# on a condition. This could be user input, a condition based on tempo, a stored
# variable, or some other program attribute. Try to use at least two conditional
# branches in your composition's control flow!

# Tip: Comment out code above so it doesn't interfere with this part of the lab!






