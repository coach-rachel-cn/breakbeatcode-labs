#######################################################
# CODE NEXT - BREAKBEATCODE
# Week 5: Loops & Beats
# Lab 5.1: Programming with Loops
#######################################################

from earsketch import *

# PART 1 - LOOPS
# Loops are so powerful in programming - loops can automate  
# programming tasks that would otherwise be terribly tedious

# For instance, this loop prints out the numbers 0-10 
# Note that the number passed into range() is exclusive
# Uncomment the next two lines to see the for loop in action
# for i in range(11):
#     print(i)

# YOUR TURN!
# 1. Print out every number 1-100 (inclusive)


# 2. Print out every number 50-100 (inclusive)


# 3. Print out only the even numbers from 1-100


# 4. Find the sum of all the numbers 1-100 and print it out


###################################

# PART 2 - LOOPING THROUGH LISTS

# Here's a list of all of Alex's favorite foods.
favorite_foods = ["Sushi", "Pizza", "Salmon", "Tamales dulces", "Yuca fries", 
                  "Apple pie", "Katsu curry", "Shrimp and grits", "Waffles"]

# 1. For each food in the list, print out a statement that says 
# "I really love _____" and then fill in the blank with each.
# Note: this is a for IN loop - it's a little different than for i in range()
for food in favorite_foods:
    pass




# 2. Below is a list of 99 names. 
# Iterate over them all and print out only the names that include the letter "a".
# Optional: create a function that accomplishes this task and call it to test it
many_names = ["Alexa","Burke","Kasimir","Baxter","Carissa","Vielka","Derek","Jemima","Jackson","Keegan","Graham","Melissa","Jeanette","Grant","Kirsten","Naida","Brody","Ishmael","Kane","Seth","Rae","Eagan","Camille","Alana",
  "Vance","Melinda","Tarik","Risa","Jordan","Camilla","Karly","Baker","Adena","Calvin","Kendall","Nasim","Kellie","Dana","Rhoda","Linus","Tyler","Ahmed","Dante","Shay","Lael","Tana","Claudia","Chadwick","Tara",
  "Fulton","Justine","Malcolm","Rowan","Christopher","Ciaran","Ivan","Hiram","Blake","Colton","Nathaniel","Moses","Cynthia","George","Ignacia","Chanda","Wyatt","Amethyst","Vladimir","Adam","Boris","Joseph","Scarlett","Kieran","Curran",
  "Dalton","Paul","Phillip","Plato","Renee","Natalie","Barbara","Keiko","Oleg","Xerxes","Caesar","Kareem","Ahmed","Charles","Cyrus","Adria","Winifred","Pandora","Wynne","Simon","Wanda","Coby","Nolan","Marsden","Courtney"]




# 3. Now iterate over the list and print out only the names which have more 
# than 6 letters in them.
# Optional: create a function that accomplishes this task and call it to test it



# 4. Iterate over the list and find the longest name in the whole thing. 
# Then print out "The longest name in the list is ______. It has ___ letters in it."
# Optional: create a function that accomplishes this task and call it to test it




#############################

# PART 3 LOOPS & LISTS X EARSKETCH

setTempo(88)

# PRACTICE 1 - NUMBER OF MEASURES

# We've used fitMedia to repeat a sound for a specified number of 
# measures, but you can accomplish this with a loop as well!
# Here's a sound that is one measure long - use a for loop with range()  
# to play it for eight measures. Hint: you will need to specify two arguments
# for range() so the sound starts at the correct measure (can't start at 0!)

beat = COMMON_LOVE_DRUMBEAT_1




    

# You might be thinking this is no different than fitMedia. You're right!
# But now you can do some more interesting things - let's say you want to play
# a sound every other measure instead of every measure. Try making this happen
# using a for loop, conditional, and the MODULO operator to play the beat on odd measures






# MUSIC THEORY TIME - a drum fill is a short break from the main drum beat of a song that
# is used to transition to the next part of the song. It's more decorative! In a four-bar
# phrase of music, the drum fill will play every FOURTH measure. Use a for loop and if/else 
# to play the beat pattern every measure, unless it's the 4th/8th/12th/etc measure of the  
# phrase - in those measures, play the fill instead!

fill = RD_ROCK_POPRHYTHM_FILL_2



#########################################

# PRACTICE 2 - STORE INSTRUMENT SOUNDS
setTempo(80)

# Lists provide a great way to organize components of your song
# For example, the list called vocals stores each vocal verse sound
# for the song "Outcast" by Twin Flames. Each sound is 2 measures

vocals = [TFLAMES_OC_VOX_VRS_1, TFLAMES_OC_VOX_VRS_2, 
          TFLAMES_OC_VOX_VRS_3, TFLAMES_OC_VOX_VRS_4]
# populate this list with the piano verse sounds for Outcast
piano = []

# STRETCH: Add lists with sounds for additional instruments
# Take note of how long the sounds are compared to vocals and piano


# The start variable keeps track of the starting measure
start = 1
# Use a for loop to play each sound stored in the instrument lists
# Comment in the code below!
# for i in range(len(vocals)):
#     # play the vocal sound at index i of vocals 
#     insertMedia(vocals[i], 1, start)
#     # Add an insertMedia call to play the piano sounds on a different track
  
#     # increment the start variable for the next iteration of the loop
#     start += 2

# STRETCH CHALLENGE: Add additional instruments
# Look at the other parts for the verse of Twin Flames "Outcast"
# and add another list above that stores a different instrument's sounds
# for the verse (drums, synth, etc). The catch is that not all sounds
# for the additional instruments are the same number of measures - how can you
# leverage loops and insertMedia to play these sounds?




#########################################

# PRACTICE 3 - SONG FORM

# In music theory, nearly all compositions follow some sort of song form or structure
# Most songs you listen to will generally have the following song components:
# INTRO - VERSE - CHORUS - OUTRO
# Songs will generally have multiple different verses, and the chorus will be
# repeated more than once. This is a structure we are going to replicate here!

# Populate the lists below with the sounds you want to use for each song component
# You can use existing artists' sounds (like the last example) or any sound in the library
intro = []
verse = []
chorus = []
outro = []

# Set up any variables you need (start, track, etc.)


def playSong():
    # delete pass when you have your function code written
    pass
    # use a loop to play the intro

    # use a loop to play the verse

    # use a loop to play the chorus

    # use a loop to play the outro


# Make a call to your playSong() function to play your song!



