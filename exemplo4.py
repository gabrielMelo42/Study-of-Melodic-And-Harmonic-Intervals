from music21 import *
n1=note.Note("C4")
n2=note.Note("F#4")
n1.duration.type="half"
print(n1.duration.quarterLength)
#uma minima tem o dobro de tempo de uma seminima
print(n2.duration.quarterLength)
print(n1.step)
print(n2.step)
#how to declare an array in python: nameOfArray=[]
noteList=[n1,n2]
print(noteList)
for thisNote in noteList:
	print(thisNote.step)
n3=note.Note("B-2")
noteList.append(n3)
print("The length of noteList array is %i"  %len(noteList))
for thisNote in noteList:
	print(thisNote.step)
print(noteList[0])
print(noteList[1])
print(noteList.index(n3))
print(noteList[-1])#returns the last array element
print(noteList[-1] is noteList[2])




stream1=stream.Stream()
stream1.append(n1)
stream1.append(n2)
stream1.append(n3)

stream2=stream.Stream()
n4=note.Note("D#5")
stream2.repeatAppend(n4,4)
#stream2.show()

#stream1.show()

'''stream3=stream.Stream()
n5=note.Note("D#3")
n6=note.Note("B-3")
n7=note.Note("G-3")
n8=note.Note("F3")

i=0
while i<=3:
	stream3.append(n5)
	stream3.repeatAppend(n6,2)
	stream3.append(n7)
	stream3.repeatAppend(n8,4)
	stream3.append(n7)
	i+=1

stream3.show()'''

print(len(stream1))
stream1.show('text')#shows the offsets of each note
#Once a Note is in a Stream, we can ask for the offset of the Notes (or anything else) in it. 
#The offset is the position of a Note relative to the start of the Stream measured in quarter notes.
#So note1’s offset will be 0.0, since it’s at the start of the Stream
#We can say that  "offset" is the quantity of quarters we have until we analyse the note we're talking about

for thisNote in stream1:
	print(thisNote.step)

print(stream1[0])
print(stream1[-1].nameWithOctave)

n3Index=stream1.index(n3)
print(n3Index)
stream1.pop(n3Index)
#stream1.show()

#getElementByClass()
for thisNote in stream1.getElementsByClass(note.Note):
	print(thisNote, thisNote.offset)


#the same of:
for thisNote in stream1.getElementsByClass("Note"):
	print(thisNote, thisNote.offset)

#as the Stream has no Rest, the print command will be the same if we print only the Notes
for thisNote in stream1.getElementsByClass(["Note", "Rest"]):
	print(thisNote, thisNote.offset)
	

#variations:

#.notes=["Notes, "Chords]
for thisNote in stream1.notes:
	print(thisNote.pitch)

for thisNote in stream1.getElementsByClass(["Notes, Chords"]):
	print(thisNote.pitch.accidental)

#.notesAndRests=["Note", "Chord", "Rest"]
for thisNote in stream1.notesAndRests:
	print(thisNote.duration)

for thisNote in stream1.getElementsByClass(["Note", "Chord", "Rest"]):
	print(thisNote.nameWithOctave)

listOut=stream1.pitches
print(listOut)

sOut=stream1.getElementsByClass(note.Note)
sOut.show("text")

#if you really want to be sure:
sOut=stream1.getElementsByClass(note.Note).stream()
sOut.show("text")

sOut=stream1.getElementsByOffset(3)
a=len(sOut)
print(a)

#print(sOut[0])
sOut=stream1.getElementsByOffset(2,3).stream()
sOut.show("text")

#stream1.analyse('ambitus')#the range from the lowest note to the highest note; in other words, "interval"
print(n1.offset)
print(n2.offset)
print(n3.offset)
print(n4.offset)


for thisNote in stream1:
	print(thisNote.name, thisNote.offset)

#.offset is the same fo getOffsetBySite(stream)
#example:
print(n1.offset)
print(n1.getOffsetBySite(stream1))
#here we remember the getters methods
#the purpose of use getOffsetBySite() instead use .offset is because if you use various n1 objects in the part, 
#it's not so simple to return the n1 object you want
#But if you use the getter method, it will return you the correct offset

print(stream1.lowestOffset)
#the lowestOffset property returns the minimum of all offsets for all elements on the Stream.

stream1.show('midi')
stream1.show()
stream1.show("text")
#print(defaults.meterNumerator)
#print(dafaults.meterDenominator)

print(n1)
print(stream1)
stream1.id="someNotes"
print(stream1)
n1.id="abc"
print(n1)
#print(strteam1.duration)
#print(stream1.duration.type)
#print(stream1.duration.quarterLength)
#Notice that the len() of a Stream, which stands for “length”, is not the same as the duration.
#the len() of a Stream is the number of objects stored in it, so len(stream1) is 3
print(stream1.highestTime)
#The highestTime of a Stream is offsetOfTheLastNote+quarterLengthOfTheLastNote


biggerStream=stream.Stream()
n9=note.Note("D#5")
biggerStream.insert(0,n9)#inserir no Stream
biggerStream.append(stream1)
biggerStream.show("text")
print(n1 in stream1)
print(n1 in biggerStream)





