from music21 import *
f=note.Note("F5")
print(f)
print (f.name)
print(f.octave)
print(f.pitch)
print(f.pitch.frequency)
print(f.pitch.pitchClassString)
print(f.octave==5)
print(f.pitch.pitchClassString==5)
print(f.pitch.pitchClassString=='5')
print(f.pitch.pitchClassString=="5")
print(f.pitch.pitchClass)
#print(f.pitchClass==5)
siBemol=note.Note("B-2")
print(siBemol.pitch.accidental)
acc=siBemol.pitch.accidental
print(acc.alter)#shows how many semitones this accidental changes the Note 
#flat:negative; sharp:positive
print(siBemol.pitch.accidental.alter)
#print(acc.displayLocation)
#acc.displayLocation = 'above'
#print(acc.displayLocation)
