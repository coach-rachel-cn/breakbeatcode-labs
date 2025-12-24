#######################################################
# CODE NEXT - BREAKBEATCODE
# Week 5: Loops & Beats
# Lab 5.1: Programming with Loops
#######################################################

# INSTRUCTOR-FACING KEY #
# NOTE: The solutions below represent only one of many possible solutions
# to the lab challenges

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
# for i in range(1, 101):
#     print(i)

# 2. Print out every number 50-100 (inclusive)
# for i in range(50, 101):
#     print(i)

# 3. Print out only the even numbers from 1-100
# for i in range(1, 101):
#     if i % 2 == 0:
#         print(i)

# 4. Find the sum of all the numbers 1-100 and print it out
# sum = 0
# for i in range(101):
#     sum += i
# print(sum)

# 5. Print out every multiple of three from 1-100
# for i in range(1, 101):
#     if i % 3 == 0:
#         print(i)

# 6. SPICY: Print out the numbers 1-100 which are multiples of 3 OR multiples of 2, 
# but not multiples of both
# for i in range(1, 101):
#     if i % 3 == 0:
#         if not i % 2 == 0:
#             print(i)
#     elif i % 2 == 0:
#         if not i % 3 == 0:
#             print(i)
        

# 7. SUPER SPICY: print out the first 40 numbers of the Fibonacci sequence
# num1 = 0
# num2 = 1
# for i in range(40):
#     print(num1)
#     temp = num1
#     num1 = num2
#     num2 = temp + num2


###################################

# PART 2 - LOOPING THROUGH LISTS

# Here's a list of all of Alex's favorite foods.
favorite_foods = ["Sushi", "Pizza", "Salmon", "Tamales dulces", "Yuca fries", 
                  "Apple pie", "Katsu curry", "Shrimp and grits", "Waffles"]

# 1. For each food in the list, print out a statement that says 
# "I really love _____" and then fill in the blank with each.
# Note: this is a for IN loop - it's a little different than for i in range()
# for food in favorite_foods:
#     print("I really love " + food + "!")



# 2. Let's expand the dialogue - For each food in the list, print out three lines.
#    "Have you ever tried ___?"
#    "I really recommend that you try _____."
#    "_____ is delicious."
# for food in favorite_foods:
#     print("Have you ever tried " + food + "?")
#     print("I really recommend that you try " + food)
#     print(food + " is delicious.")



# 3. Below is a list of numbers. Iterate over the list 
#    and print out only the numbers less than 100.
many_numbers = [109, 141, 44, 51, 133, 366, 339, 248, 226, 321, 97, 195, 245, 252, 238, 
                1, 366, 47, 189, 91, 148, 88, 194, 106, 5, 128, 165, 337, 380, 181, 143, 95]



# 4. Now iterate over the list but print out only the even ones.
# for num in many_numbers:
#     if num % 2 == 0:
#         print(num)


# 5. Use a loop to help you find the sum of all the numbers in the many_numbers list
# sum = 0
# for num in many_numbers:
#     sum += num
# print(sum)



# 6. Below is a list of 99 names. 
# Iterate over them all and print out only the names that include the letter "a".
# Optional: create a function that accomplishes this task and call it to test it
many_names = ["Alexa","Burke","Kasimir","Baxter","Carissa","Vielka","Derek","Jemima","Jackson","Keegan","Graham","Melissa","Jeanette","Grant","Kirsten","Naida","Brody","Ishmael","Kane","Seth","Rae","Eagan","Camille","Alana",
  "Vance","Melinda","Tarik","Risa","Jordan","Camilla","Karly","Baker","Adena","Calvin","Kendall","Nasim","Kellie","Dana","Rhoda","Linus","Tyler","Ahmed","Dante","Shay","Lael","Tana","Claudia","Chadwick","Tara",
  "Fulton","Justine","Malcolm","Rowan","Christopher","Ciaran","Ivan","Hiram","Blake","Colton","Nathaniel","Moses","Cynthia","George","Ignacia","Chanda","Wyatt","Amethyst","Vladimir","Adam","Boris","Joseph","Scarlett","Kieran","Curran",
  "Dalton","Paul","Phillip","Plato","Renee","Natalie","Barbara","Keiko","Oleg","Xerxes","Caesar","Kareem","Ahmed","Charles","Cyrus","Adria","Winifred","Pandora","Wynne","Simon","Wanda","Coby","Nolan","Marsden","Courtney"]




# 7. Now iterate over the list and print out only the names which have more 
# than 6 letters in them.
# Optional: create a function that accomplishes this task and call it to test it
def long_names():
    for name in many_names:
        if len(name) > 5:
            print(name)

# long_names()


# 8. Iterate over the list and find the longest name in the whole thing. 
# Then print out "The longest name in the list is ______. It has ___ letters in it."
# Optional: create a function that accomplishes this task and call it to test it

def find_longest(list):
    longest = list[0]
    for item in list:
        if len(item) > len(longest):
            longest = item
    return longest

# print(find_longest(many_names))

# 9. Are there more long names or short names? Write code to figure that out.
# Optional: create a function that accomplishes this task and call it to test it
def long_or_short():
    long = []
    short = []
    for name in many_names:
        if len(name) > 5:
            long.append(name)
        else:
            short.append(name)
    if len(long) > len(short):
        return "There are more long names than short names"
    else:
        return "There are more short names than long names"

# print(long_or_short())


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
# for measure in range(1, 9):
#     insertMedia(beat, 1, measure)



# You might be thinking this is no different than fitMedia. You're right!
# But now you can do some more interesting things - let's say you want to play
# a sound every other measure instead of every measure. Try making this happen
# using a for loop, conditional, and the MODULO operator to play the beat on odd measures

# for measure in range(1, 13):
#     if measure % 2 == 1:
#         insertMedia(beat, 1, measure)



# MUSIC THEORY TIME - a drum fill is a short break from the main drum beat of a song that
# is used to transition to the next part of the song. It's more decorative! In a four-bar
# phrase of music, the drum fill will play every FOURTH measure. Use a for loop and if/else 
# to play the beat pattern every measure, unless it's the 4th/8th/12th/etc measure of the  
# phrase - in those measures, play the fill instead!

fill = RD_ROCK_POPRHYTHM_FILL_2

# for measure in range(1, 9):
#     if measure % 4 == 0:
#         insertMedia(fill, 1, measure)
#     else:
#         insertMedia(beat, 1, measure)


#########################################

# PRACTICE 2 - STORE INSTRUMENT SOUNDS

setTempo(80)
# Lists provide a great way to organize components of your song
# For example, the list called vocals stores each vocal verse sound
# for the song "Outcast" by Twin Flames. Each sound is 2 measures

vocals = [TFLAMES_OC_VOX_VRS_1, TFLAMES_OC_VOX_VRS_2, 
          TFLAMES_OC_VOX_VRS_3, TFLAMES_OC_VOX_VRS_4]
# populate this list with the piano verse sounds for Outcast
piano = [TFLAMES_OC_PIANO_VRS_1,TFLAMES_OC_PIANO_VRS_2,
         TFLAMES_OC_PIANO_VRS_3,TFLAMES_OC_PIANO_VRS_4]

# STRETCH: Add lists with sounds for additional instruments
# Take note of how long the sounds are compared to vocals and piano
synth = [TFLAMES_OC_SYNTH_VRS_1, TFLAMES_OC_SYNTH_VRS_2]
drums = TFLAMES_OC_SNARE_VRS_1

# The start variable keeps track of the starting measure
start = 1
# Use a for loop to play each sound stored in the instrument lists
# Comment in the code below!
for i in range(len(vocals)):
    # play the vocal sound at index i of vocals 
    insertMedia(vocals[i], 1, start)
    # Add an insertMedia call to play the piano sounds on a different track
    insertMedia(piano[i], 2, start)
    # increment the start variable for the next iteration of the loop
    start += 2

# STRETCH CHALLENGE: Add additional instruments
# Look at the other parts for the verse of Twin Flames "Outcast"
# and add another list above that stores a different instrument's sounds
# for the verse (drums, synth, etc). The catch is that not all sounds
# for the additional instruments are the same number of measures - how can you
# leverage loops and insertMedia to play these sounds?
start = 1
# PLAY SYNTH - each synth sound is 2 bars, so we can loop through the synth list twice
# This is an example of a NESTED for loop
for i in range(2):
    # play each sound in the list
    for synth_sound in synth:
        insertMedia(synth_sound, 3, start, start+2)
        start+=2


# Play drums with fitMedia
start = 1
fitMedia(drums, 4, start, start + 8)



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



