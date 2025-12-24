#######################################################
# CODE NEXT - BREAKBEATCODE
# Week 5: Loops & Beats
# Lab 5.2: Making Beats with makeBeat()
#######################################################

# INSTRUCTOR-FACING KEY #
# NOTE: The solutions below represent only one of many possible solutions
# to the lab challenges


# NOTE!! For this lab, you will want to use this beat-making reference:
# https://learningmusic.ableton.com/make-beats/make-beats.html

from earsketch import *
from random import randint

setTempo(100)

# PART 1 - Find sounds and create beat strings

# First, play around with the beats maker here: https://learningmusic.ableton.com/make-beats/beat-and-tempo.html
# Configure the player to a beat/combination you like - you will be recreating it here!
# Once you've got a beat that you like, you'll build it in the following steps


# Now it's time to find sounds for your beat. In the sounds tab, search "makebeat"
# Find sounds for open hi hat, closed hi hat, snare/clap, and kick that you like. Store them in variables!
# Note: you can use other sounds to make beats, but we'll focus on the four percussion sounds first

exampleSound = OS_LOWTOM01

openhat = OS_OPENHAT04
closedhat = OS_CLOSEDHAT03
clap = OS_SNARE05
kick = OS_LOWTOM04


# Next you will create beat strings for each of your sounds - the pattern of sounds that will play in the DAW
# when you create a beat string, 0 means the sound plays, - means the sound stops, and + means the sound is sustained
# here is an example beat string that plays four sounds exactly on the beat (every fourth character of the beat string)

exampleBeat = '0---0---0---0---'

# the above example has 16 steps, meaning it takes up a full measure in the DAW. Each measure has four beats,
# so the whole beat string is one measure broken up into 16ths


# Create the beat strings for each of your sounds based on what you created on the Ableton site
# Make sure that each of your beat strings has 16 steps so that it takes up a full measure
# Reminder: the beat strings need to be enclosed in single or double quotes!

openhatbeat = '----0--0---0----'
closedhatbeat = '-0-0--0---0----0'
clapbeat = '0---0--0-0--0--0'
kickbeat = '0---0---0---0---'


# PART 2 - Play your beats!

# You will use the makeBeat() function to play each of your beat strings
# An example is shown below, and you can also search makeBeat in the API tab to learn more about makeBeat()

# makeBeat(exampleSound, 1, 1, exampleBeat)

# Play your beats with makeBeat(sound, track, start, beat)
# makeBeat(openhat, 1, 1, openhatbeat)
# makeBeat(closedhat, 2, 1, closedhatbeat)
# makeBeat(clap, 3, 1, clapbeat)
# makeBeat(kick, 4, 1, kickbeat)



# PART 3 - LOOPING with makeBeat()

# You probably want your beat to play for more than one measure. This is where loops come in!

# this example plays the example beat for four measures
# when using the range function, start at 1 because the DAW doesn't start at measure 0. 
# notice that the second number in range() is excluded. Uncomment the example to hear it in action

# for measure in range(1, 5):
#     makeBeat(exampleSound, 1, measure, exampleBeat)


# Use a for loop to play your beats for multiple measures
# Experiment with changing your sounds, beat string variables, and how you set up your for loop(s)

# for measure in range(1, 5):
#     makeBeat(openhat, 1, measure, openhatbeat)
#     makeBeat(closedhat, 2, measure, closedhatbeat)
#     makeBeat(clap, 3, measure, clapbeat)
#     makeBeat(kick, 4, measure, kickbeat)




# PART 4 - FUNCTIONS + makeBeat()

# Let's now combine the power of variables, makeBeat(), and loops with functions
# See how you might tackle the challenges below using what you've learned so far with Python & EarSketch
# In these challenges, as with most of programming, there isn't one way to solve the challenges...there are often many!

# Challenge 1 - create a function that takes in a tempo and length as parameters, and the beat play for that length and speed

def playBeat(tempo, length):
    setTempo(tempo)
    for measure in range(1, length+1):
        makeBeat(openhat, 1, measure, openhatbeat)
        makeBeat(closedhat, 2, measure, closedhatbeat)
        makeBeat(clap, 3, measure, clapbeat)
        makeBeat(kick, 4, measure, kickbeat)

# playBeat(88, 4)

# Challenge 2 - create a function that asks the user to input a genre, 
# and the beat plays a tempo for that genre
# for tempo reference check out: https://learningmusic.ableton.com/make-beats/tempo-and-genre.html

def chooseGenre():
    genre = input("Choose a genre (hip-hop, house, dubstep): ").lower()
    if genre == "hip-hop":
        tempo = randint(60, 100)
    elif genre == "house":
        tempo = randint(115, 130)
    elif genre == "dubstep":
        tempo = randint(135, 145)
    else:
        chooseGenre()

    # use the function we already wrote to play the beat for 4 bars
    playBeat(tempo, 4)


# chooseGenre()
    
# Challenge 3 - create a function that asks the user to input the tempo and number of measures a beat should play,
# and the beat plays for that many measures

def chooseLength():
    measures = input("How many measures should the beat play for? ")
    tempo = input("Enter a numerical tempo (beats per minute) for the beat: ")
    # using int() to cast the variables as numbers
    # and the playBeat function we previously defined
    playBeat(int(tempo), int(measures))
    
# chooseLength()

# Challenge 4 - create a function that allows the user to select from a menu of different beats, 
# and whatever beat is chosen then plays




# Challenge 5 - COMBO PLATTER! create a function that does all of the above ^^^ but in one function





# Challenge 6 - FREESTYLE! Dealer's choice - what else can you cook up that showcases all of these skills?





