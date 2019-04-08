from music21 import *
import array as arr

print("Hello world")

dictionary = {
	"C--0": -50, 
	"C-0": -49,
	"C0":-48,
	"D--0": -48,
	"C#0":-47,
	"D-0": -47,
	"C##0":-46,
	"D0":-46,
	"E--0":-46,
	"D#0":-45,
	"E-0":-45,
	"F--0": -45, 
	"D##0":-44,
	"E0":-44,
	"F-0": -44, 
	"E#0":-43,
	"F0":-43,
	"G--0":-43,
	"E##0":-42,
	"F#0":-42,
	"G-0":-42,
	"G0":-41, 
	"F##0":-41,
	"A--0":-41,
	"G#0":-40,
	"A-0":-40,
	"A0":-39,
	"G##0":-39,
	"B--0":-39,
	"A#0":-38,
	"B-0":-38,
	"C--1":-38,
	"B0":-37,
	"A##0":-37,
	"C-1": -37,





	 
	"C1":-36,
	"D--1": -36,
	"C#1":-35,
	"D-1": -35,
	"C##1":-34,
	"D0":-46,
	"E--0":-46,
	"D#0":-45,
	"E-0":-45,
	"F--0": -45, 
	"D##0":-44,
	"E0":-44,
	"F-0": -44, 
	"E#0":-43,
	"F0":-43,
	"G--0":-43,
	"E##0":-42,
	"F#0":-42,
	"G-0":-42,
	"G0":-41, 
	"F##0":-41,
	"A--0":-41,
	"G#0":-40,
	"A-0":-40,
	"A0":-39,
	"G##0":-39,
	"B--0":-39,
	"A#0":-38,
	"B-0":-38,
	"C--1":-38,
	"B0":-37,
	"A##0":-37,
	"C-1": -37,
	"C1":-36,
	"B#0":-36,
	"D--0":-36,
	"C#1":-35,
	"B##0":-35,
	"D-1":-35,
	"D1":-34,
	"C##1":-34,
	"E--1":-34,
	"D#1":-33,
	"E-1":-33,
	"F--1":-33,
	"E1":-32,
	"D##1":-32,
	"F-1":-32,
	"F1":-31,



	"C1": -36, "C#1": -35, "D1":-34, "D#1":-33, "E1":-32, "F1":-31, "F#1":-30, "G1":-29, "G#1":-28, "A-1":-28, "A1":-27,"A#1":-26, "B-1":-26, "B1":-25,
	"C2": -24, "C#2": -23, "D-2":-23, "D2":-22,  "D#2":-21, "E-2":-21,  "E2":-20, "F2":-19, "F#2":-18, "G2":-17, "G#2":-16, "A-2":-16, "A2":-15,"A#2":-14, "B-2": -14, "B2":-13,
	"C3": -12, "C#3": -11, "D-3":-11,  "D3":-10, "D#3":-9,  "E-3":-9, "E3":-8, "F3":-7, "F#3":-6, "G-3":-6,  "G3":-5, "G#3":-4, "A-3":-4, "A3":-3,"A#3":-2, "B-3":-2, "B3":-1,
	"C4": 0, "C#4": 1, "D-4":1, "D4":2, "D#4":3, "E-4":3, "E4":4,  "F4":5, "F#4":6,  "G-4":6, "G4":7, "G#4":8, "A-4":8, "A4":9,"A#4":10, "B-4":10, "B4":11,
	"C5":12, "C#5": 13,  "D-5":13, "D5":14, "D#5":15, "E-5":15, "E5":16, "F5":17, "F#5":18, "G5":19, "G#5":20, "A-5":20,  "A5":21,"A#5":22, "B-5":22, "B5":23,
	"C6": 24, "C#6": 25, "D6":26, "D#6":27, "E6":28, "F6":29, "F#6":30, "G6":31, "G#6":32, "A6":33,"A#6":34,"B6":35,
	"C7": 36, "C#7": 37, "D7":38, "D#7":39, "E7":40, "F7":41, "F#7":42, "G7":43, "G#7":44,"A7":45,"A#7":46,"B7":47,
	"C8": 48
}

music=converter.parse('/Library/Frameworks/Python.framework/Versions/3.7/lib/pythonIC/site-packages/music21/corpus/BohemianRhapsody.mxl')

maoDireita=music.getElementsByClass(stream.Part)[0].getElementsByClass(stream.Measure)
maoEsquerda=music.getElementsByClass(stream.Part)[1].getElementsByClass(stream.Measure)

maoDireitaAcordes=maoDireita.chordify()
maoEsquerdaAcordes=maoEsquerda.chordify()

notasComoNumeros=[]
notasComoNumerosDireita=[]
notasComoNumerosEsquerda=[]

intervalosDireita=[]
intervalosEsquerda=[]
intervalosHarmonicos = []

maoDireitaAcordesComoNumeros = []
maoEsquerdaAcordesComoNumeros = []

def transformarEmNumeros(comoMusica, comoNumero):
	for i in comoMusica:
		notas=i.getElementsByClass(note.Note)
		for j in notas:
			comoNumero.append(dictionary[j.nameWithOctave])

def intervalosMelodicos(melodia, intervalo):
	for i in range(0, len(melodia)-1):
		intervalo.append(melodia[i+1]-melodia[i])

def metodoIntervalosHarmonicos(melodia1, melodia2, intervalo):
	for i in range(0, len(melodia1)):
		if(melodia2>-1):
			intervalo.append(melodia1[i]-melodia2[i])
		else:
			break

'''	if (len(melodia1)==len(melodia2)):
		for i in range(0, len(melodia1)):#podia ser melodia2, ja que tanto faz
			intervalo.append(melodia1[i]-melodia2[i])

	if(len(melodia1)>len(melodia2)):
		for i in range(0, len(melodia1)):
			if(melodia2[i]>-1):
				intervalo.append(melodia1[i]-melodia2[i])
			else:
				break

	if(len(melodia1)<len(melodia2)):
		for i in range(0, len(melodia2)):
			if(melodia1>-1):
				intervalo.append(melodia1[i]-melodia2[i])
			else:
				break
'''


#notasComoNumerosDireita=arr.array('i', transformarEmNumeros(maoDireita, notasComoNumerosDireita))
#notasComoNumerosEsquerda=arr.array('i', transformarEmNumeros(maoEsquerda, notasComoNumerosEsquerda))
notasComoNumerosDireita=transformarEmNumeros(maoDireita, notasComoNumerosDireita)
notasComoNumerosEsquerda=transformarEmNumeros(maoEsquerda, notasComoNumerosEsquerda)
maoDireitaAcordesComoNumeros=transformarEmNumeros(maoDireitaAcordes, maoDireitaAcordesComoNumeros)
maoEsquerdaAcordesComoNumeros=transformarEmNumeros(maoEsquerdaAcordes, maoEsquerdaAcordesComoNumeros)
intervalosDireita=intervalosMelodicos(notasComoNumerosDireita, intervalosDireita)
intervalosEsquerda=intervalosMelodicos(notasComoNumerosEsquerda, intervalosEsquerda)
intervalosHarmonicos=metodoIntervalosHarmonicos(notasComoNumerosDireita, notasComoNumerosEsquerda, intervalosHarmonicos)



'''
for i in maoDireita:
	notas=i.getElementsByClass(note.Note)
	for j in notas:
		notasComoNumerosDireita.append(dictionary[j.nameWithOctave])

i=0
j=0

for i in maoEsquerda:
	notas=i.getElementsByClass(note.Note)
	for j in notas:
		notasComoNumerosEsquerda.append(dictionary[j.nameWithOctave])

for i in range(0, len(notasComoNumerosDireita)-1):
	intervalosDireita.append(notasComoNumerosDireita[i+1]-notasComoNumerosDireita[i])

for i in range(0, len(notasComoNumerosEsquerda)-1):
	intervalosEsquerda.append(notasComoNumerosEsquerda[i+1]-notasComoNumerosEsquerda[i])


for i in maoDireitaAcordes:
	notas=i.getElementsByClass(note.Note)
	for j in notas:
		maoDireitaAcordesComoNumeros.append(dictionary[j.nameWithOctave])

for i in maoEsquerdaAcordes:
	notas=i.getElementsByClass(note.Note)
	for j in notas:
		maoEsquerdaAcordesComoNumeros.append(dictionary[j.nameWithOctave])
'''
'''print(len(maoDireitaAcordesComoNumeros))

for i in range (0, len(maoDireitaAcordesComoNumeros)-1):
	print(maoDireitaAcordesComoNumeros[i].pitch)
	print(maoDireitaAcordesComoNumeros[i].pitch)
	intervalosHarmonicos.append(maoDireitaAcordesComoNumeros[i]-maoEsquerdaAcordesComoNumeros[i])



music.show()
maoDireitaAcordes.show()
maoEsquerdaAcordes.show()''
for i in maoDireita:
	notas=i.getElementsByClass(note.Note)
	for j in notas:
		notasComoNumerosDireita.append(dictionary[j.nameWithOctave])
for i in range(0, len(notasComoNumerosDireita)-1):
	intervalosDireita.append(notasComoNumerosDireita[i+1]-notasComoNumerosDireita[i])
'''
#for i in range(0, len)

'''#txt=open("intervalosHarmonicos.txt", "w+")

if len(intervalosEsquerda)>len(intervalosDireita):
	for i in range(0, len(notasComoNumerosEsquerda)-1, 2):
		for j in range(0, len(notasComoNumerosDireita)-1,2):
			intervalosHarmonicos.append(notasComoNumerosEsquerda[i]-notasComoNumerosDireita[j])

else:
	for i in range(0, len(notasComoNumerosDireita)-1, 2):
		for j in range(0, len(notasComoNumerosEsquerda)-1,2):
			intervalosHarmonicos.append(notasComoNumerosDireita[i]-notasComoNumerosEsquerda[j])
#txt=open("intervalos.txt", "w+")

for i in range(0, len(notasComoNumeros)-1, 2)
	intervalos.append(notasComoNumeros[i+1]-notasComoNumeros[i])

for x in intervalos:
	txt.write(str(x)+"\n")

txt.close()
'''
