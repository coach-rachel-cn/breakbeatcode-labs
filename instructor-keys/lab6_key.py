#######################################################
# CODE NEXT - BREAKBEATCODE
# Week 6: Dictionaries
# Lab 6: Programming with Dictionaries
#######################################################

# INSTRUCTOR-FACING KEY #
# NOTE: The solutions below represent only one of many possible solutions
# to the lab challenges


from earsketch import *

# PART 1 - Dictionaries

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
print(favorite_books["martin"])

# 2. Print out Alexandra's favorite book.
print(favorite_books["alexandra"])

# 3. Before we get started, let's adjust a few things. First off, Jeff just read 
#    a new  book called  "The Martian" and loved it. With just one line of code,  
#    change Jeff's favorite book to "The Martian"
favorite_books["jeff"] = "The Martian"

# 4. Print out Jeff's favorite book to confirm that the change was successful.
print(favorite_books["jeff"])

# 5. We should also add Ronald to the list. His favorite book is "Lies my History 
#    Teacher Told Me." Add that info to the dictionary as a new key-value pair.
favorite_books["ronald"] = "Lies My History Teacher Told Me"

# 6. Confirm that Ronald's book was added by printing it out.
print(favorite_books["ronald"])

# 7. Now let's start iterating. For each person in the dictionary, print out a   
#    statement that says "___'s favorite book is ____" and fill in the blanks 
#    with that name person's name and favorite book.

# for person in favorite_books:
#     print(person.capitalize() + "'s favorite book is " + favorite_books[person])



# LEVEL TWO
# Here is a large list of dictionaries called contacts. Expand it by 
# clicking the dropdown symbol to the left of contacts on line 77.  
# What are the key-value pairs that you see in each of the dictionaries?
contacts = [
    {"name": "Gail", "phone": "1-586-721-0425", "email": "volutpat.Nulla@ultricesVivamusrhoncus.ca", "company": "Nisl Consulting", "address": "Ap #713-1686 Ipsum Avenue"},
  	{"name": "Kiara", "phone": "1-570-815-0661", "email": "Curae.Donec.tincidunt@pharetra.edu", "company": "Lacus Cras Corporation", "address": "Ap #913-1818 Fermentum St."},
  	{"name": "Linda", "phone": "1-929-491-0254", "email": "lacinia.orci@nec.edu", "company": "Arcu Aliquam Ultrices Corporation", "address": "546-9340 Erat. Avenue"},
  	{"name": "Melodie", "phone": "1-505-323-3274", "email": "erat.in@Inornaresagittis.net", "company": "Morbi Tristique Senectus Corporation", "address": "296-2323 Vel Avenue"},
  	{"name": "Maya", "phone": "1-149-593-5099", "email": "Nunc@dapibusligulaAliquam.org", "company": "Varius Et Institute", "address": "224-9796 Auctor St."},
  	{"name": "Emerson", "phone": "1-241-993-6209", "email": "Aenean.egestas@diam.com", "company": "Vel Convallis In Consulting", "address": "624-6849 Sed St."},
  	{"name": "Connor", "phone": "1-303-953-7934", "email": "dolor.dolor@a.co.uk", "company": "Primis In Corp.", "address": "821-3495 Gravida Av."},
  	{"name": "Germaine", "phone": "1-384-255-3742", "email": "et.tristique.pellentesque@egestasFusce.co.uk", "company": "At LLP", "address": "Ap #572-407 Iaculis Rd."},
  	{"name": "Matthew", "phone": "1-643-678-4139", "email": "morbi.tristique.senectus@rutrum.net", "company": "Lacinia Orci Consulting", "address": "P.O. Box 361, 3873 Vehicula St."},
  	{"name": "Clinton", "phone": "1-894-550-5145", "email": "adipiscing.lacus@vulputate.org", "company": "Venenatis LLC", "address": "135-4643 Natoque Street"},
  	{"name": "Cheyenne", "phone": "1-911-952-7885", "email": "nec.tempus@mollisDuis.net", "company": "Sed Nec Metus Corporation", "address": "412-3689 Ullamcorper, St."},
  	{"name": "Gray", "phone": "1-706-895-7377", "email": "vehicula@nec.co.uk", "company": "Sapien Nunc Industries", "address": "Ap #497-7093 Libero Street"},
  	{"name": "Megan", "phone": "1-276-822-7525", "email": "nec.urna.et@utpellentesqueeget.co.uk", "company": "Dolor Tempus LLC", "address": "Ap #872-2688 Hymenaeos. Avenue"},
  	{"name": "Alvin", "phone": "1-350-597-2184", "email": "Ut@imperdietnec.edu", "company": "At Incorporated", "address": "166 Vivamus St."},
  	{"name": "Jelani", "phone": "1-654-449-2719", "email": "pretium@Loremipsum.org", "company": "Litora Incorporated", "address": "8254 Felis Rd."},
  	{"name": "Tanisha", "phone": "1-321-405-4607", "email": "mauris.sapien@tellus.co.uk", "company": "Primis In Corporation", "address": "P.O. Box 748, 4374 Mauris Av."},
  	{"name": "Bell", "phone": "1-217-787-2472", "email": "purus.Duis.elementum@mollisvitae.com", "company": "Non Justo Proin LLP", "address": "P.O. Box 155, 9358 Magna. St."},
  	{"name": "Robin", "phone": "1-476-868-0082", "email": "ipsum.dolor@interdumenim.co.uk", "company": "Ligula Consulting", "address": "846 Mauris Avenue"},
  	{"name": "Charde", "phone": "1-106-959-7497", "email": "magna.sed@famesacturpis.net", "company": "Aenean LLP", "address": "Ap #648-1017 Ut St."},
  	{"name": "Cleo", "phone": "1-723-991-9132", "email": "vehicula@arcuimperdiet.co.uk", "company": "Neque In Foundation", "address": "742-674 Nunc Av."},
  	{"name": "Vincent", "phone": "1-880-698-6725", "email": "Sed.eget.lacus@aliquet.co.uk", "company": "Duis Gravida Industries", "address": "P.O. Box 916, 9385 Ac Rd."},
  	{"name": "Benjamin", "phone": "1-357-440-3613", "email": "pede.sagittis@ametmassaQuisque.com", "company": "Magna Nam Industries", "address": "241-3333 Phasellus Rd."},
  	{"name": "Honorato", "phone": "1-611-901-1579", "email": "euismod@tristiquepellentesquetellus.edu", "company": "Arcu Aliquam Ultrices Limited", "address": "P.O. Box 270, 5889 Enim Avenue"},
  	{"name": "Nigel", "phone": "1-880-429-6399", "email": "lorem.ipsum@velitegetlaoreet.net", "company": "Justo Eu Industries", "address": "Ap #342-1888 Vulputate Av."},
  	{"name": "Yuli", "phone": "1-203-259-5725", "email": "non@quisdiam.org", "company": "Quis Diam Pellentesque Foundation", "address": "Ap #516-3394 Cras Road"}
]

# In this list, each dictionary representes a person, and has that person's name, 
# phone number, email, the company they work for, and their address. You can print 
#  the 7th person's email using this line of code - uncomment this to see if it works:
# print(contacts[6]["email"])

# 8. Print out the fifth person from the the address book.
# print(contacts[4])

# 9. Print out the email of the 10th person from the address book.
print(contacts[9]["email"])

# 10. Print out the name of the first person from the address book.
print(contacts[0]["name"])

# 11. Print out the name and phone number of the first person in the address book 
# in the following format: "_____ can be reached at ______" filling in the blanks 
# with the person's name and phone number.
print(contacts[0]["name"] + " can be reached at " + contacts[0]["phone"])

# 12. Print out the same information "_____ can be reached at ______" with names and 
# phone numbers for all of our contacts in the list.
# for contact in contacts:
#     print(contact["name"] + " can be reached at " + contact["phone"])

# 13. If we wanted to send an email that was only useful for college students and their professors, 
# we could send that email ONLY to folks in our contacts whose email addresses end in ".edu".
# Create a list called edu_emails and put every .edu email address from our contacts into that list.
# Print the list when you're done to check your work.

# edu_emails = []
# for contact in contacts:
#     if ".edu" in contact["email"]:
#         edu_emails.append(contact["email"])

# print(edu_emails)

    

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
    "snare-beat": '----0-------0---',
    # don't forget to add a comma after each key-value pair!
    # add sounds and beat strings for a closed hat and open hat:
    "closedhat": OS_CLOSEDHAT05,
    "closedhat-beat": '--0---00---0---0',
    "openhat": OS_OPENHAT04,
    "openhat-beat": '-0--------0---0-'
}

# Use bracket notation to access the tempo value stored in the dictionary
setTempo(mybeat["tempo"])

# Play the beat strings using makeBeat and bracket notation to access the values
# Uncomment the next two lines to play the kick and snare beat strings
# makeBeat(mybeat["kick"], 1, 1, mybeat["kick-beat"])
# makeBeat(mybeat["snare"], 2, 1, mybeat["snare-beat"])
# Use makeBeat to play the beat strings you created for the open and closed hi-hat
# makeBeat(mybeat["openhat"], 3, 1, mybeat["openhat-beat"])
# makeBeat(mybeat["closedhat"], 4, 1, mybeat["closedhat-beat"])



# Now let's LOOP your beat pattern so it lasts longer than one measure (AKA one bar)
# Create a function called playBeat that takes a length parameter
# Use a loop and your makeBeat function calls to play the beat for the
# specified duration. Don't forget to call your function to test it!
# Tip: comment out or move your makeBeat function calls above
def playBeat(length):
    for measure in range(1, length+1):
        makeBeat(mybeat["kick"], 1, measure, mybeat["kick-beat"])
        makeBeat(mybeat["snare"], 2, measure, mybeat["snare-beat"])
        makeBeat(mybeat["openhat"], 3, measure, mybeat["openhat-beat"])
        makeBeat(mybeat["closedhat"], 4, measure, mybeat["closedhat-beat"])


# playBeat(4)

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

# CHORUS DICTIONARY
chorus = {
    "vocals": [CIARA_SET_VOX_HOOK_1, CIARA_SET_VOX_HOOK_2, CIARA_SET_VOX_HOOK_3, CIARA_SET_VOX_HOOK_4],
    "beat": CIARA_SET_DRUMBEAT_2,
    "synth": CIARA_SET_THEME_MAIN_1
    # optional: try adding some additional sounds
    
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


def playChorus(measure):
    start = measure
    for sound in chorus["vocals"]:
        insertMedia(sound, 1, start)
        start +=2
    start = measure
    fitMedia(chorus["beat"], 2, start, start+8)
    fitMedia(chorus["synth"], 3, start, start+8)


# FUNCTION CALLS TO PLAY SONG
# Not sure what tempo to use? Try this tool that lets you 
# tap a tempo: https://taptempo.io/
setTempo(80)
# Play the verse starting at measure 1
playVerse(1)
# Call your function to play the chorus
playChorus(5)