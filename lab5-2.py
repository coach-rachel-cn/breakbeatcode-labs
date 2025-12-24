#######################################################
# CODE NEXT - BREAKBEATCODE
# Week 5: Loops & Beats
# Lab 5.2: Making Beats with makeBeat()
#######################################################

# NOTE!! For this lab, you will want to use this beat-making reference:
# https://learningmusic.ableton.com/make-beats/make-beats.html

from earsketch import *

setTempo(100)

# PART 1 - Find sounds and create beat strings

# First, play around with the beats maker here: https://learningmusic.ableton.com/make-beats/beat-and-tempo.html
# Configure the player to a beat/combination you like - you will be recreating it here!
# Once you've got a beat that you like, you'll build it in the following steps


# Now it's time to find sounds for your beat. In the sounds tab, search "makebeat"
# Find sounds for open hi hat, closed hi hat, snare/clap, and kick that you like. Store them in variables!
# Note: you can use other sounds to make beats, but we'll focus on the four percussion sounds first

exampleSound = OS_LOWTOM01

# openhat = 
# closedhat = 
# clap = 
# kick = 


# Next you will create beat strings for each of your sounds - the pattern of sounds that will play in the DAW
# when you create a beat string, 0 means the sound plays, - means the sound stops, and + means the sound is sustained
# here is an example beat string that plays four sounds exactly on the beat (every fourth character of the beat string)

exampleBeat = '0---0---0---0---'

# the above example has 16 steps, meaning it takes up a full measure in the DAW. Each measure has four beats,
# so the whole beat string is one measure broken up into 16ths


# Create the beat strings for each of your sounds based on what you created on the Ableton site
# Make sure that each of your beat strings has 16 steps so that it takes up a full measure
# Reminder: the beat strings need to be enclosed in single or double quotes!

# openhatbeat = ''
# closedhatbeat = ''
# clapbeat = ''
# kickbeat = ''


# PART 2 - Play your beats!

# You will use the makeBeat() function to play each of your beat strings
# An example is shown below, and you can also search makeBeat in the API tab to learn more about makeBeat()

makeBeat(exampleSound, 1, 1, exampleBeat)

# Play your beats with makeBeat(sound, track, start, beat)






# PART 3 - LOOPING with makeBeat()

# You probably want your beat to play for more than one measure. This is where loops come in!

# this example plays the example beat for four measures
# when using the range function, start at 1 because the DAW doesn't start at measure 0. 
# notice that the second number in range() is excluded. Uncomment the example to hear it in action

# for measure in range(1, 5):
#     makeBeat(exampleSound, 1, measure, exampleBeat)


# Use a for loop to play your beats for multiple measures
# Experiment with changing your sounds, beat string variables, and how you set up your for loop(s)






# PART 4 - FUNCTIONS + makeBeat()

# Let's now combine the power of variables, makeBeat(), and loops with functions
# See how you might tackle the challenges below using what you've learned so far with Python & EarSketch
# In these challenges, as with most of programming, there isn't one way to solve the challenges...there are often many!

# Challenge 1 - create a function that takes in a tempo and length as parameters, and the beat play for that length and speed



# Challenge 2 - create a function that asks the user to input a genre, 
# and the beat plays a tempo for that genre
# for tempo reference check out: https://learningmusic.ableton.com/make-beats/tempo-and-genre.html




# Challenge 3 - create a function that asks the user to input the tempo and number of measures a beat should play,
# and the beat plays for that many measures




# Challenge 4 - create a function that allows the user to select from a menu of different beats, 
# and whatever beat is chosen then plays




# Challenge 5 - COMBO PLATTER! create a function that does all of the above ^^^ but in one function





# Challenge 6 - FREESTYLE! Dealer's choice - what else can you cook up that showcases all of these skills?





