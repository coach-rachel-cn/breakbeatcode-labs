#######################################################
# CODE NEXT - BREAKBEATCODE
# Week 4: Functions & SFX
# Lab 4.1 KEY: Programming with Functions
#######################################################

# INSTRUCTOR-FACING KEY #
# NOTE: The solutions below represent only one of many possible solutions
# to the lab challenges

from earsketch import *

# PART 1 - FUNCTIONS PRACTICE

# 1. Write a function called shout that takes in a string
# as an argument and returns it in all capital letters
# Hint: Visit https://www.w3schools.com/python/python_ref_string.asp
def shout(string):
    # pass is a placeholder for future code
    # it can be used to avoid getting errors
    return string.upper()

# call the function to test it out!
print(shout("breakbeatcode"))

# 2. Write a function called whisper that takes in a string
# as an argument and returns it in all lowercase letters
def whisper(string):
    return string.lower()

# call the function to test it out!
print(whisper("AHHHHHHHHHHHHH"))

    
# 3. Write a function called how_many_letters that takes in
# a string as an argument and returns the nmber of letters in
# that string
def how_many_letters(word):
    return len(word)

print(how_many_letters("Supercalifragilisticexpialidocious"))

# 4. Write a function that calculates the area of a rectangle
# Bonus: Build in a way to detect if the rectangle is a square
def calculate_area(width, height):
    area = width * height
    if width == height:
        return "This is a square with an area of " + str(area) + " units^2"
    return str(area) + " units^2"

print(calculate_area(5, 6,))

# 5. Write a function to determine whether a number is even or odd
def even_odd(num):
    if num % 2 == 0:
        return str(num) + " is EVEN"
    else:
        return str(num) + " is ODD"


# 6. Write a function to convert a temperature from Celsius to Fahrenheit
def c_to_f(celsius):
    print(celsius)
    fahrenheit = 1.8 * celsius + 32
    return str(celsius) + " C is " + str(int(fahrenheit)) + " F"

print(c_to_f(100))

# 7. STRETCH: Refactor (reorganize) your temperature conversion
# function such that it can convert temps from C to F or F to C
# Hint: There are many possible solutions, but consider using input()
# to help you get started!

def temp_converter(temp, unit):
    if unit.lower() == "f" or unit.lower() == "fahrenheit":
        new_temp = (temp-32) * 0.56
        print(new_temp)
        return str(temp) + " " + unit.capitalize() + " is " + str(int(new_temp)) + " Celsius"
    else:
        new_temp = 1.8*temp + 32
        return str(temp) + " " + unit.capitalize() + " is " + str(int(new_temp)) + " Fahrenheit"
    

print(temp_converter(212, "f"))

###############################

# PART 2 - FUNCTIONS X EARSKETCH

setTempo(120)

# 1. Create a function called playSounds() that plays at least 2 different
# sounds on different tracks in the DAW for at least 4 measures

def playSounds():
    track = 1
    start = 1
    stop = 9
    beat = RD_UK_HOUSE_MAINBEAT_14
    fitMedia(beat, track, start, stop)
    track = 2
    synth = RD_TRAP_DARKPAD_1
    fitMedia(synth, track, start, stop)
    
# test your playSounds() function by calling it
# playSounds()


# 2. Refactor your playSounds() function so that it takes in a 
# measure argument that indicates what measure the sounds will
# start and stopplaying - for example: a call of playSounds(1, 5) would 
# begin playing the sounds in measure 1 and end after measure 4
def playSounds2(start, stop):
    track = 1
    beat = RD_UK_HOUSE_MAINBEAT_14
    fitMedia(beat, track, start, stop)
    track = 2
    synth = RD_TRAP_DARKPAD_1
    fitMedia(synth, track, start, stop)

# test your refactored function by calling it
# playSounds2(1,5)


# 3. STRETCH: Create a playChorus() function that plays the chorus of 
# a song in the EarSketch sound library. Choose an artist that you like
# and examine the sounds that have "chorus" in their name. Try to piece
# together components of that song's chorus (vocals, piano, drums, etc)
# so that it plays cohesively when the function is called!
# Optional: give your function parameters like measure, tempo, etc. to
# make it even more flexible

def playChorus(start, stop):
    # theme from Set by Ciara
    setTempo(88)
    # using a list to store the vocals
    vocals = [CIARA_SET_VOX_HOOK_1, CIARA_SET_VOX_HOOK_2, CIARA_SET_VOX_HOOK_3, CIARA_SET_VOX_HOOK_4]
    track = 1
    # bracket notation to access each of the vocal parts
    insertMedia(vocals[0], track, start)
    insertMedia(vocals[1], track, start+2)
    insertMedia(vocals[2], track, start+4)
    insertMedia(vocals[3], track, start+6)
    track = 2
    beat = CIARA_SET_DRUMBEAT_1
    fitMedia(beat, track, start, stop)
    track = 3
    bass = CIARA_SET_BASSLINE_1
    fitMedia(bass, track, start, stop)
    
    

# test your playChorus() function by calling it!
playChorus(1, 9)

