#######################################################
# CODE NEXT - BREAKBEATCODE
# Week 4: Functions & SFX
# Lab 4.2: Exploring Sound Effects in EarSketch
#######################################################

from earsketch import *

# EXPERIMENT WITH EARSKETCH EFFECTS!!

# PROGRAM SETUP
# Variables to keep track of song components
# Adjust any of the values for the variables as you see fit!
sample = IRCA_BOMBA_YUBA_CUARTEADO_ELEC_GUITAR_PRI
track = 1
start = 1
tempo = 144
length = 4

# PLAY SAMPLE
# Play the sample as is to hear without effects
setTempo(tempo)
fitMedia(sample, track, start, length+1)


# ADD EFFECTS
# The setEffect() function can have 4 or 7 parameters
# setEffect() with 7 parameters specifies when the effect will end
# Look at the API and curriculum tabs for more detailed info

# Tip: Comment the example effects below in and out to 
# understand how they affect the program output

# VOLUME --> GAIN - the output volume, from -60db to 12db
# Adjust gain using setEffect with 4 arguments passed in
setEffect(track, VOLUME, GAIN, -40)
# Adjust gain using setEffect with 7 arguments passed in
setEffect(track, VOLUME, GAIN, -40, start, 10, length)


# REVERB --> REVERB_TIME - how long to decay sound, from 100 to 4000ms
# Adjust reverb with 4 arguments to setEffect
# setEffect(track, REVERB, REVERB_TIME, 4000)
# Adjust reverb with 7 arguments to setEffect
# setEffect(track, REVERB, REVERB_TIME, 4000, start, length-2, 100)


# DISTORTION --> DISTO_GAIN - amount of overdrive, from 0 to 50
setEffect(track, DISTORTION, DISTO_GAIN, 50)
# Your turn - set the DISTO_GAIN effect for part of the track 
# using setEffect() with 7 arguments passed in


# OTHER EFFECTS TO EXPERIMENT WITH!
# Use the API and Curriculum tabs to look up additional effects to
# explore. The effects are explained with sample code in section 10 
# of the curriculum tab. Find 3-4 more effects that interest
# you and experiment with them below:

# EFFECT 1 -->
# What it does:
# Try the effect with 4 or 7 arguments passed into setEffect()


# EFFECT 2 -->
# What it does:
# Try the effect with 4 or 7 arguments passed into setEffect()


# EFFECT 3 --> 
# What it does:
# Try the effect with 4 or 7 arguments passed into setEffect()


# EFFECT 4 --> 
# What it does
# Try the effect with 4 or 7 arguments passed into setEffect()



