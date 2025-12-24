#######################################################
# CODE NEXT - BREAKBEATCODE
# Week 6: Dictionaries
# Lab 6: Programming with Dictionaries
#######################################################

from earsketch import *

# PART 1 - Dictionaries (pure Python)

# Dictionaries are data structures that can be used to store more complex data
# Dictionaries are declared with curly brackets and contain a series of keys with 
# associated values. Keys are on the left and values are on the right. Commas are
# used to separate sets of key-value pairs. Putting key-value pairs on their own
# lines is not required, but using whitespace makes them more easily readable


# Here's a small dictionary of favorite books, each keyed to a different person.
# For example, "diana" is a key and the value for that key is "Crime and Punishment"
favorite_books = {
  "diana": "Crime and Punishment",
  "sophie": "The Secret History",
  "cory": "Fahrenheit 451",
  "gabe": "The Hobbit",
  "danny": "Lonesome Dove",
  "dan": "Don Quixote",
  "katie": "10:04",
  "zara": "Rebecca",
  "david": "The Sun Also Rises",
  "alexandra": "Hyperbole and a Half",
  "martin": "The House on Mango Street",
  "jeff": "The Hitchhiker's Guide to the Galaxy"
}

# 1. Print out Martin's favorite book.
# to access the value at a given key, use bracket notation
# print(favorite_books["diana"])


# 2. Print out Alexandra's favorite book.



# 3. Before we get started, let's adjust a few things. First off, Jeff just read 
#    a new  book called  "The Martian" and loved it. With just one line of code,  
#    change Jeff's favorite book to "The Martian"



# 4. Print out Jeff's favorite book to confirm that the change was successful.




# 5. We should also add Ronald to the list. His favorite book is "Lies my History 
#    Teacher Told Me." Add that info to the dictionary as a new key-value pair.



# 6. Confirm that Ronald's book was added by printing it out.




# 7. Now let's start iterating. For each person in the dictionary, print out a   
#    statement that says "___'s favorite book is ____" and fill in the blanks 
#    with that name person's name and favorite book.

for person in favorite_books:
    pass






##################################

# PART 2 - Dictionaries x EarSketch

# PRACTICE 1 - BEATS
# In this example, you will be using a dictionary to store components of a drum
# beat, and you will use makeBeat and bracket notation to access data stored in
# the dictionary and play the beat

# MUSIC THEORY REMINDER - a drum beat typically consists of 4 voices: kick/bass,
# snare/clap, open hi-hat, and closed hi-hat. Search makebeat to find these 
# in the EarSketch library to find these sounds!

mybeat = {
    "tempo": 72,
    "kick": OS_KICK01,
    "kick-beat": '0------0--0----0',
    "snare":OS_CLAP03,
    "snare-beat": '----0-------0---'
    # don't forget to add a comma after each key-value pair!
    # add sounds and beat strings for a closed hat and open hat:

    
}

# Use bracket notation to access the tempo value stored in the dictionary
setTempo(mybeat["tempo"])

# Play the beat strings using makeBeat and bracket notation to access the values
# Uncomment the next two lines to play the kick and snare beat strings
# makeBeat(mybeat["kick"], 1, 1, mybeat["kick-beat"])
# makeBeat(mybeat["snare"], 2, 1, mybeat["snare-beat"])

# Use makeBeat to play the beat strings you created for the open and closed hi-hat




# Now let's LOOP your beat pattern so it lasts longer than one measure (AKA one bar)
# Create a function called playBeat that takes a length parameter
# Use a loop and your makeBeat function calls to play the beat for the
# specified duration. Don't forget to call your function to test it!
# Tip: comment out or move your makeBeat function calls above





# PRACTICE 2 - SONG FORM
# In this example, you will be constructing elements of a song, like a
# verse and chorus, using dictionaries. The dictionaries for the verse
# and chorus are populated for you, but you will need to create the 
# function to play the chorus (theme). Feel free to add more sounds to
# the dictionaries based on what you hear in the original song

# Inspiration: "Set" by Ciara
# YouTube link: https://youtu.be/hmnyOp9dw88?si=Gm2kKCC3WlUgmoXY

# VERSE DICTIONARY
verse = {
    "vocals": [CIARA_SET_VOX_VERSE_1, CIARA_SET_VOX_VERSE_2],
    "beat": CIARA_SET_DRUMBEAT_1,
    "bass": CIARA_SET_BASSLINE_1
    # optional: try adding some additional sounds:
    
}

# FUNCTION TO PLAY VERSE
def playVerse(measure):
    # set the start variable to what is passed in to the function
    start = measure
    # play vocals using a for...in loop
    for sound in verse["vocals"]:
        insertMedia(sound, 1, start)
        # incrementing start by 2 because the sounds are 2 bars long
        start += 2
        
    # reset the start variable for beat and bass
    start = measure
    # use fitMedia to loop beat and bass 
    fitMedia(verse["beat"], 2, start, start+4)
    fitMedia(verse["bass"], 3, start, start+4)

    
# CHORUS DICTIONARY
chorus = {
    "vocals": [CIARA_SET_VOX_HOOK_1, CIARA_SET_VOX_HOOK_2, CIARA_SET_VOX_HOOK_3, CIARA_SET_VOX_HOOK_4],
    "beat": CIARA_SET_DRUMBEAT_2,
    "synth": CIARA_SET_THEME_MAIN_1
    # optional: try adding some additional sounds
    
}


# YOUR TURN - DEFINE THE CHORUS FUNCTION
# using the dictionary above
def playChorus(measure):
    pass


# FUNCTION CALLS TO PLAY SONG
# Not sure what tempo to use? Try this tool that lets you 
# tap a tempo: https://taptempo.io/
setTempo(80)
# Play the verse starting at measure 1
playVerse(1)
# Call your function to play the chorus


