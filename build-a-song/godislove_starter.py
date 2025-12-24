#######################################################
# CODE NEXT - BREAKBEATCODE
# Week 7: Data Structures Practice
# Lab 7: Song Building Challenge - God is Love STARTER
####################################################### 

# SONG BUILDING CHALLENGE INSTRUCTIONS
# Using what you know about Python so far, your challenge is to code out
# a song in the EarSketch library. Listen to the original song first for
# inspiration and to get a sense of the song's structure. The first verse
# has been modeled for you, and your task is to build out as much of the
# rest of the song (eg. choir, verse 2, etc.) as you can!

# INSPIRATION: God is Love by Common
# YouTube link: https://youtu.be/rpR0D6g0k5I?si=_ScKebR94zOHRjac

from earsketch import *

# This dictionary keeps track of information about the song
song_info = {
    "tempo": 86,
    "vocals": 1,
    "piano": 2,
    "beat": 3,
    "choir": 4
}

# VERSE 1
verse1 = {
    "vocals": [COMMON_LOVE_VOX_COMMON_1, COMMON_LOVE_VOX_COMMON_2, 
               COMMON_LOVE_VOX_COMMON_3, COMMON_LOVE_VOX_COMMON_4],
    "piano": [COMMON_LOVE_THEME_PIANO_3, COMMON_LOVE_THEME_PIANO_4],
    "beat": COMMON_LOVE_DRUMBEAT_1
}

# Your turn - create dictionaries for other parts of the song!!
# Use dictionaries and lists to organize the song components how you see fit

# VERSE 2
# Listen carefully to the original - strings are added in the second verse!
verse2 = {
    
}


# CHOIR
# The choir plays twice during the song, but the second time the adlib vocals
# are added in, so think about how you want to structure this
choir = {

    
}


# FUNCTIONS TO PLAY PARTS OF THE SONG
def playVerse1(measure):
    # start will be the measure the sound will begin
    start = measure
    # play drum beat for 16 measures
    fitMedia(verse1["beat"], song_info["beat"], start, start+16)
    for sound in verse1["vocals"]:
        insertMedia(sound, song_info["vocals"], start)
        start +=4
    # reset the start variable for piano
    start = measure
    # Outer loop - to loop through the piano list twice
    for i in range(2):
        # Inner loop - play each sound in the piano list
        for sound in verse1["piano"]:
            insertMedia(sound, song_info["piano"], start)
            start += 4
    


# Your turn - build out the functions for the other sections of the song
def playChoir(measure):
    pass




def playVerse2(measure):
    pass





    
# PLAY THE SONG!
# Set the tempo using the value stored in the song_info dictionary
setTempo(song_info["tempo"])

# Function call to play the chorus starting at measure 1
playVerse1(1)

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