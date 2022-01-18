#		python code
#		script_name: Computer Science Principles EarSketch Project
#
#		author: Ethan and Christine
#		description: Python Project


from earsketch import *

#Set Tempo Function
init()
setTempo(88)

#Envelope Points- these points help to make setting effects easier, especially when we need to incorporate multiple measures in a code
pointA = 1
pointB = 11
pointC = 12
pointD = 12.5
pointE = 16.5
pointF = 17
pointG = 17.25
pointH = 17.5
pointI = 16.75
pointJ = 25
pointK =36.5
pointL = 37.5
pointM = 42
pointN = 43.5

#Variable(s)- these variables make it easier for us to use the sounds in the code. This way we don't have to continue looking for the sound everytime we need it and if we needed to go back and fix or replace a sound we can just fix the variable instead of going back into the code to change each one.
gtar = "YG_ALT_POP_GUITAR_1"
piano = "ESAN_ECCOMPPIANO4"

#Introduction and Verse 1- this one uses the "gtar" variable so that we can reuse this sound and not have to change this certain sound if we decided it won't work out. We would just have to go back to where we set the variable to change the sounds for the codes we used the variables for.
fitMedia(gtar, 1, 1, 12)

#Loop- this loop allows us to use the sound a couple of times without using the function "fitMedia" multiple times. The range tells us how long it will loop for and how long the sound will play for, which in this case is 4 measures.
for measure in range(5,12): 
  fitMedia(piano, 2, measure, measure + 4)

#Volume Dynamics with Function- this effect helps us to fade away and then fade into the chorus using the envelope points we set in the beginning.
setEffect(1, VOLUME, GAIN, 0, pointA, -5, pointB)
setEffect(1, VOLUME, GAIN, -5, pointB, -20, pointC)
setEffect(1, VOLUME, GAIN, -20, pointC, 6, pointD)


#Chorus- the fitMedia is a function to put the sound in a certain row and starting/ending measures.
fitMedia(ESAN_ECCHUNK1, 1, 12, 17) 
  
#Verse 2
fitMedia(ESAN_CHUNK2, 2, 16.97, 20.87)
fitMedia(ESAN_CHUNK4, 3, 20.81, 24.675)

#Bridge
fitMedia(ESAN_CHUNK5, 2, 24.675, 32.5)

#Chorus
fitMedia(ESAN_ECCHUNK1, 1, 31.5, 36.5)

#Ending- the ending portion has a part where the sound decrescendos and then crescendos. At the end the sound shoul die down and cut off.
fitMedia(gtar, 1, 36.5, 43.5)
fitMedia(ESAN_CRASH, 3, 36.5, 38)
setEffect(1, VOLUME, GAIN, -20, pointK, 0, pointL)
setEffect(1, VOLUME, GAIN, 0, pointM, -50, pointN)
fitMedia(piano, 2, 40.5, 45)

finish()
