# python code
#######################################################
# CODE NEXT - BREAKBEATCODE
# Week 7: Data Structures Practice
# Lab 7: Song Building Challenge - Freedom STARTER
####################################################### 

# SONG BUILDING CHALLENGE INSTRUCTIONS
# Using what you know about Python so far, your challenge is to code out
# a song in the EarSketch library. Listen to the original song first for
# inspiration and to get a sense of the song's structure. Part of the verse has
# been modeled for you, so your task is to build out the rest of the verse, and
# as much of the rest of the song (eg. prechorus, chorus) as you can!

# INSPIRATION: Freedom by Dakota Bear
# YouTube link: https://youtu.be/BdZJaxBybTA?si=w3BSUUF5TBSp6xOl

from earsketch import *

# This dictionary keeps track of information about the song
song_info = {
    "tempo": 112,
    "vocalTrack" : 1,
    "beatTrack": 2,
    "synthTrack": 3
}

# VERSE
verse = {
    "vocals": [DKBEAR_FREE_VOX_VERSE_1A, DKBEAR_FREE_VOX_VERSE_1B],
    "beat": DKBEAR_FREE_BEAT_FULL,
    "synth": DKBEAR_FREE_THEME_PIANO
}




# Your turn - create dictionaries for other parts of the song!!
# Use dictionaries and lists to organize the song components how you see fit

# CHORUS
chorus = {
    "vocals": []
}


# PRECHORUS
prechorus = {

    
}




# FUNCTIONS TO PLAY PARTS OF THE SONG
def playVerse(measure):
    # start will be the measure the sound will begin 
    start = measure
    
    # play the vocals in the vocal list with a for loop
    for sound in verse["vocals"]:
        insertMedia(sound, song_info["vocalTrack"], start)
        # adding 8 because the verse sounds are 8 measures each
        start += 8
    
    # reset the start variable for the beat and synth
    start = measure

    # play the beat and synth sounds - end the sound 32 measures after start
    fitMedia(verse["beat"], song_info["beatTrack"], start, start+16)
    fitMedia(verse["synth"], song_info["synthTrack"], start, start+16)



# Your turn - build out the functions for the other sections of the song
def playChorus(measure):
    pass




def playPrechorus(measure):
    pass





    
# PLAY THE SONG!
# Set the tempo using the value stored in the song_info dictionary
setTempo(song_info["tempo"])

# Function call to play the chorus starting at measure 1
playVerse(1)

# Your turn - call the functions you've created to play the song
# Think about the order of your function calls so the song makes musical sense!



#######################################

# OPTIONAL STRETCH IDEAS
# 1. Intro and outro - listen to the original and try to craft an intro and outro
# for the song based on the sounds you have available in the EarSketch library. Don't
# worry if it doesn't match the original exactly - be creative!

# 2. Additional layers - if there are additional instrument or voice parts for your 
# song in the sound library, add those in to your program

# 3. Effects - use setEffect() to do some mixing for your song - set volume levels and
# other effects. You can use the original song for inspiration or your own ideas

# 4. SPICY - Refactor your code so that one data structure (list or dictionary) contains
# all of the data for your song. For example, you might have a list of dictionaries
# or a dictionary that houses multiple dictionaries

# 5. SPICY - Instead of using a dictionary to keep track of the track numbers for your
# instrument voices, define a getTrack function that takes in a part and returns a 
# number for that part's track in the DAW. For example, in this program main vocals are
# on track 1 and piano is on track 2, so getTrack("vocals") would return 1, and
# getTrack("piano") would return 2. When you've written the function, refactor your 
# program to use the getTrack function instead of the song_info dictionary
