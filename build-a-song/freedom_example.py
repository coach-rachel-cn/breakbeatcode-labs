#######################################################
# CODE NEXT - BREAKBEATCODE
# Week 7: Data Structures Practice
# Lab 7: Song Building Challenge - Freedom EXAMPLE
####################################################### 


from earsketch import *

freedom = {
    "tempo": 112,
    "intro": {
        "vox": [DKBEAR_FREE_TALK_DOING_THIS, DKBEAR_FREE_TALK_MUST_DO, DKBEAR_FREE_TALK_NEED_TO],
        "synth": DKBEAR_FREE_THEME_PIANO,
        "sfx" : DKBEAR_FREE_PERC_WHOOSH
    },
    "verse": {
        "vox": [DKBEAR_FREE_VOX_VERSE_1A, DKBEAR_FREE_VOX_VERSE_1B, DKBEAR_FREE_VOX_VERSE_2A, DKBEAR_FREE_VOX_VERSE_2B],
        "beat": DKBEAR_FREE_BEAT_FULL,
        "synth": DKBEAR_FREE_THEME_PIANO
    },
    "prechorus": {
        "vox": [DKBEAR_FREE_VOX_PRECHORUS_1, DKBEAR_FREE_VOX_PRECHORUS_2],
        "beat": DKBEAR_FREE_BEAT_FULL,
        "synth": DKBEAR_FREE_THEME_PIANO
    },
    "chorus": {
        "vox": [DKBEAR_FREE_VOX_CHORUS_1, DKBEAR_FREE_VOX_CHORUS_2],
        "beat": DKBEAR_FREE_BEAT_FULL,
        "synth": DKBEAR_FREE_THEME_PIANO
        
    },
    "outro": {
        "synth": DKBEAR_FREE_THEME_SYNTH_1,
        "sfx": DKBEAR_FREE_THEME_BASS
    }
}

# returns a number to indicate the track for a particular part
def getTrack(part):
    if part == "vox":
        return 1
    elif part == "synth":
        return 2
    elif part == "beat":
        return 3
    elif part == "sfx":
        return 4
    else:
        return "error"

        
# INTRO - 8 bars
# the measure parameter will indicate the bar that this section starts
def intro(measure):
    intro_start = measure
    for part in freedom["intro"]:
        if part == "vox":
            for line in freedom["intro"][part]:
                insertMedia(line, getTrack(part), intro_start)
                intro_start += 2
        elif part == "sfx":
            fitMedia(freedom["intro"][part], getTrack(part), intro_start+6, intro_start+8)
        else:
            fitMedia(freedom["intro"][part], getTrack(part), intro_start, intro_start+8)
        intro_start = measure

# VERSE - each phrase is 8 bars - 32 total
def verse(measure):
    verse_start = measure
    for part in freedom["verse"]:
        if part == "vox":
            for sound in freedom["verse"][part]:
                insertMedia(sound, getTrack(part), verse_start)
                verse_start += 8
        else:
            fitMedia(freedom["verse"][part], getTrack(part), verse_start, verse_start+32)
        verse_start = measure

            
# PRECHORUS - 16 bars
def prechorus(measure):
    prechorus_start = measure
    for part in freedom["prechorus"]:
        if part == "vox":
            # each prechorus sample is 8 bars
            for sound in freedom["prechorus"][part]:
                insertMedia(sound, getTrack(part), prechorus_start)
                prechorus_start += 8
        else:
            fitMedia(freedom["prechorus"][part], getTrack(part), prechorus_start, prechorus_start+16)
        prechorus_start = measure


        
# CHORUS - 16 bars
def chorus(measure):
    chorus_start = measure
    for part in freedom["chorus"]:
        if part == "vox":
            # each chorus sample is 8 bars
            for sound in freedom["chorus"][part]:
                insertMedia(sound, getTrack(part), chorus_start)
                chorus_start += 8
        else:
            fitMedia(freedom["chorus"][part], getTrack(part), chorus_start, chorus_start+16)
        chorus_start = measure

        
# OUTRO - 4 bars
def outro(measure):
    outro_start = measure
    for part in freedom["outro"]:
        insertMedia(freedom["outro"][part], getTrack(part), outro_start)
        outro_start = measure


# PLAY THE SONG W/ FUNCTION CALLS
setTempo(freedom["tempo"])
intro(1)
verse(9)
prechorus(41)
chorus(57)
outro(73)
