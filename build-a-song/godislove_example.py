#######################################################
# CODE NEXT - BREAKBEATCODE
# Week 7: Data Structures Practice
# Lab 7: Song Building Challenge - God is Love EXAMPLE
####################################################### 

from earsketch import *

common = {
    "tempo": 86,
    "beat": COMMON_LOVE_DRUMBEAT_1,
    "choir": {
        "vox": [COMMON_LOVE_VOX_CHOIR_1, COMMON_LOVE_VOX_CHOIR_2],
        "piano": [COMMON_LOVE_THEME_PIANO_1, COMMON_LOVE_THEME_PIANO_2],
        "adlib": [COMMON_LOVE_VOX_ADLIB_1, COMMON_LOVE_VOX_ADLIB_2, COMMON_LOVE_VOX_ADLIB_3, COMMON_LOVE_VOX_ADLIB_4]
    },
    "verse": {
        1: [COMMON_LOVE_VOX_COMMON_1, COMMON_LOVE_VOX_COMMON_2, COMMON_LOVE_VOX_COMMON_3, COMMON_LOVE_VOX_COMMON_4],
        2: [COMMON_LOVE_VOX_COMMON_5, COMMON_LOVE_VOX_COMMON_6, COMMON_LOVE_VOX_COMMON_7, COMMON_LOVE_VOX_COMMON_8],
        3: [COMMON_LOVE_VOX_LEON_1, COMMON_LOVE_VOX_LEON_2, COMMON_LOVE_VOX_LEON_3, COMMON_LOVE_VOX_LEON_4],
        "piano": [COMMON_LOVE_THEME_PIANO_3, COMMON_LOVE_THEME_PIANO_4],
        "strings": [COMMON_LOVE_THEME_STRINGS_1, COMMON_LOVE_THEME_STRINGS_2]
    },
    "outro": [COMMON_LOVE_THEME_JUNO_1, COMMON_LOVE_THEME_JUNO_2]     
}

# returns track number for each part in DAW
def getTrack(part):
    if part == "main":
        return 1
    elif part == "choir" or part == "vox":
        return 2
    elif part == "piano":
        return 3
    elif part == "strings":
        return 4
    elif part == "adlib":
        return 5
    elif part == "beat":
        return 6

# VERSE - number specifies which verse and measure specifies starting bar
def verse(number, measure):
    start = measure
    if number == 1:
        # drumbeat starts in bar 3 for verse 1
        fitMedia(common["beat"], getTrack("beat"), start+3, start+16)
    else:
        # strings for verses 2 and 3 - play through list twice
        for i in range(2):
            for sound in common["verse"]["strings"]:
                insertMedia(sound, getTrack("strings"), start)
                start += 4
        start = measure
        if number == 2:
        # drumbeat throughout verse 2
            fitMedia(common["beat"], getTrack("beat"), start, start+16)
        else:
            # end drums 2 bars from the end
            fitMedia(common["beat"], getTrack("beat"), start, start+12)
            # insertMedia(common["outro"][0], getTrack("adlib"), start+12)
        
    
    # reset start for vocals
    start = measure
    # play verse 1 or 2 vocals depending on what number is passed in
    for sound in common["verse"][number]:
        insertMedia(sound, getTrack("main"), start)
        start += 4

    # reset start for piano
    start = measure
    # play piano regardless of verse
    for i in range(2):
        for sound in common["verse"]["piano"]:
                insertMedia(sound, getTrack("piano"), start)
                start +=4

# CHOIR - number specifies 1st or 2nd time and measure specifies starting bar
def choir(number, measure):
    start = measure
    # drumbeat
    fitMedia(common["beat"], getTrack("beat"), start, start+8)
    # choir vocals and piano
    for part in common["choir"]:
        for sound in common["choir"][part]:
            if part != "adlib":
                insertMedia(sound, getTrack(part), start)
                start += 4
            else:
                # play adlib for choir second time
                if number == 2:
                    insertMedia(sound, getTrack(part), start+1)
                    start += 2
        start = measure
                

# PLAY SONG 
setTempo(common["tempo"])
verse(1, 1)
choir(1, 17)
verse(2, 25)
choir(2, 41)
verse(3, 49)