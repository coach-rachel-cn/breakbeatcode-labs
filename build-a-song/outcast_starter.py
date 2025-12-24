#######################################################
# CODE NEXT - BREAKBEATCODE
# Week 7: Data Structures Practice
# Lab 7: Song Building Challenge - Outcast STARTER
####################################################### 

# SONG BUILDING CHALLENGE INSTRUCTIONS
# Using what you know about Python so far, your challenge is to code out
# a song in the EarSketch library. Listen to the original song first for
# inspiration and to get a sense of the song's structure. The verse has
# been modeled for you, and your task is to build out as much of the rest
# of the song as you can!

# INSPIRATION: Outcast by Twin Flames
# YouTube link: https://www.youtube.com/watch?v=AvLb64KXu54

from earsketch import *

# This dictionary keeps track of information about the song
song_info = {
    "tempo": 80,
    "melody": 1,
    "piano": 2,
    "drums": 3
}

# VERSE
verse = {
    "melody": [TFLAMES_OC_VOX_VRS_1, TFLAMES_OC_VOX_VRS_2, 
               TFLAMES_OC_VOX_VRS_3, TFLAMES_OC_VOX_VRS_4],
    "piano": [TFLAMES_OC_PIANO_VRS_1, TFLAMES_OC_PIANO_VRS_2, 
              TFLAMES_OC_PIANO_VRS_3, TFLAMES_OC_PIANO_VRS_4],
    "drums": [TFLAMES_OC_OH_VRS_1, TFLAMES_OC_OH_VRS_1, 
              TFLAMES_OC_OH_VRS_2, TFLAMES_OC_OH_VRS_3]
}

# Your turn - create dictionaries for other parts of the song!!
# Use dictionaries and lists to organize the song components how you see fit

# CHORUS
chorus = {

    
}





# FUNCTIONS TO PLAY PARTS OF THE SONG
def playVerse(measure):
    # start will be the measure the sound will begin 
    start = measure

    # Outer loop - loops through each part (melody, piano, drums)
    # of the verse dictionary
    for part in verse:
        # Inner loop - loops through each sound in the list
        for sound in verse[part]:
            # use the loop variable part to access the
            # track numbers stored in song_info
            insertMedia(sound, song_info[part], start)
            start += 2
        # reset the start variable for the piano and drums
        start = measure
    



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
