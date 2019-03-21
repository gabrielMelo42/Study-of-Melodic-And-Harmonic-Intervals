from music21 import *
print("Hello world")
dictionary = {
	"C--0": -50, "C-0": -49,
	"C0": -48, "C#0": -47, "D0":-46, "D#0":-45, "E0":-44, "F0":-43, "F#0":-42, "G0":-41, "G#0":-40,"A0":-39,"A#0":-38,"B0":-37,
	"C1": -36, "C#1": -35, "D1":-34, "D#1":-33, "E1":-32, "F1":-31, "F#1":-30, "G1":-29, "G#1":-28,"A1":-27,"A#1":-26,"B1":-25,
	"C2": -24, "C#2": -23, "D2":-22, "D#2":-21, "E2":-20, "F2":-19, "F#2":-18, "G2":-17, "G#2":-16,"A2":-15,"A#2":-14,"B2":-13,
	"C3": -12, "C#3": -11, "D3":-10, "D#3":-9, "E3":-8, "F3":-7, "F#3":-6, "G3":-5, "G#3":-4,"A3":-3,"A#3":-2,"B3":-1,
	"C4": 0, "C#4": 1, "D4":2, "D#4":3, "E4":4, "F4":5, "F#4":6, "G4":7, "G#4":8,"A4":9,"A#4":10,"B4":11,
	"C5":12, "C#5": 13, "D5":14, "D#5":15, "E5":16, "F5":17, "F#5":18, "G5":19, "G#5":20,"A5":21,"A#5":22,"B5":23,
	"C6": 24, "C#6": 25, "D6":26, "D#6":27, "E6":28, "F6":29, "F#6":30, "G6":31, "G#6":32, "A6":33,"A#6":34,"B6":35,
	"C7": 36, "C#7": 37, "D7":38, "D#7":39, "E7":40, "F7":41, "F#7":42, "G7":43, "G#7":44,"A7":45,"A#7":46,"B7":47,
	"C8": 48
}

#music=converter.parse(HD/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/music21/corpus/mozart/k80movement2.mxl)
music=converter.parse(MacBook-Pro-2/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages (5.5.0)/)

maoDireita=music.getElementsByClass(stream.Part)[0].getElementsByClass(stream.Measure)
maoEsquerda=music.getElementsByClass(stream.Part)[1].getElementsByClass(stream.Measure)

notasComoNumeros=[]
notasComoNumerosDireita=[]
notasComoNumerosDireita=[] 

for x in maoDireita:
	notas=x.getElementsByClass()


for x in maoDireita:
	notasD=x.getElementsByClass(note.Note)
	for y in notasD:
		notasComoNumerosDireita.append(dictionary[y.nameWithOctave])

for z in maoEsquerda:
	notasE=z.getElementsByClass(note.Note)
	for a in notasE:
		notasComoNumerosEsquerda.append(dictionary[a.nameWithOctave])

intervalosHarmonicos = []

txt=open("intervalosHarmonicos.txt", "w+")

for i in range(0, len(notasComoNumerosEsquerda)-1, 2)
	for j in range(0, len(notasComoNumerosDireita)-1,2)
		intervalos.append(notasComoNumerosEsquerda[i]-notasComoNumerosDireita[j])
txt=open("intervalos.txt", "w+")

for i in range(0, len(notasComoNumeros)-1, 2)
	intervalos.append(notasComoNumeros[i+1]-notasComoNumeros[i])

for x in intervalos:
	txt.write(str(x)+"\n")

txt.close()
