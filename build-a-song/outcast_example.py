#######################################################
# CODE NEXT - BREAKBEATCODE
# Week 7: Data Structures Practice
# Lab 7: Song Building Challenge - Outcast EXAMPLE
####################################################### 

from earsketch import *

# DICTIONARY
# Song components from Twin Flames "Outcast"
outcast = {
    "tempo": 80,
    "intro": {
        "drums": TFLAMES_OC_SNARE_CHOR_1,
        "synth": TFLAMES_OC_SYNTH_CHOR_1,
        "guitar": TFLAMES_OC_GUITARS_CHOR,
        "bass": TFLAMES_OC_BASS_CHOR
    },
    "verse": {
      "melody": [TFLAMES_OC_VOX_VRS_1, TFLAMES_OC_VOX_VRS_2, TFLAMES_OC_VOX_VRS_3, TFLAMES_OC_VOX_VRS_4],
      "piano": [TFLAMES_OC_PIANO_VRS_1, TFLAMES_OC_PIANO_VRS_2, TFLAMES_OC_PIANO_VRS_3, TFLAMES_OC_PIANO_VRS_4],
      "drums": [TFLAMES_OC_OH_VRS_1, TFLAMES_OC_OH_VRS_1, TFLAMES_OC_OH_VRS_2, TFLAMES_OC_OH_VRS_3]
    },
    "chorus": {
         "melody": [TFLAMES_OC_VOX_CHOR_1, TFLAMES_OC_VOX_CHOR_2],
         "harmony": [TFLAMES_OC_VOX_BKUP_CHOR_1, TFLAMES_OC_VOX_BKUP_CHOR_2],
         "drums": [TFLAMES_OC_SNARE_CHOR_1, TFLAMES_OC_SNARE_CHOR_2],
         "guitar": [TFLAMES_OC_GUITARS_CHOR, TFLAMES_OC_GUITARS_CHOR],
         "bass": [TFLAMES_OC_BASS_CHOR, TFLAMES_OC_BASS_CHOR]
    },
    "outro": TFLAMES_OC_SYNTH_VRS_2
}

# FUNCTIONS
# instead of creating variables for tracks (original thought), this function returns the track # for each part
# this function also allowed me to get rid of the track variable I was using to loop through dictionaries
# this was WAY more useful than I was expecting it to be :D
def getTrack(part):
    if part == "synth":
        return 1
    elif part == "drums":
        return 2
    elif part == "guitar":
        return 3
    elif part == "bass":
        return 4
    elif part == "melody":
        return 5
    elif part == "piano":
        return 6
    elif part == "harmony":
        return 7
    else:
        return "error"

# FUNCTIONS TO RUN DIFF COMPONENTS OF THE SONG
# each take in a measure parameter to indicate what measure to start
def intro(measure):
    setTempo(outcast["tempo"])
    # two bars of synth intro
    insertMedia(outcast["intro"]["synth"], getTrack("synth"), measure)
    # two bars of lead-in to verse
    for part in outcast["intro"]:
        # no play synth part for lead-in to verse
        if part != "synth":
            fitMedia(outcast["intro"][part], getTrack(part), measure+2, measure+4)
        
def chorus(measure):
    chorus_start = measure
    for part in outcast["chorus"]:
        for sound in outcast["chorus"][part]:
            fitMedia(sound, getTrack(part), chorus_start, chorus_start + 2)
            chorus_start += 2
        chorus_start = measure


def verse(measure):
    verse_start = measure
    # outer loop of verse parts (dictionaries)
    for part in outcast["verse"]:
        # how to get to the list of sounds --> outcast["verse"][part]
        # inner loop to loop through the vocals and pianos lists
        for sound in outcast["verse"][part]:
            fitMedia(sound, getTrack(part), verse_start, verse_start + 2)
            verse_start += 2
        # reset start so additional verse parts are below vocals
        verse_start = measure


def outro(measure):
    insertMedia(outcast["outro"], getTrack("synth"), measure)
        
# FUNCTION CALLS TO PLAY SONG 
intro(1)
verse(5)
chorus(13)
chorus(17)
outro(21)
