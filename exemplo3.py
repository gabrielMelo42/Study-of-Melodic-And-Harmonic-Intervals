from music21 import *

p1=pitch.Pitch("b-4")
print(p1.octave)
print(p1.pitchClass)
print(p1.name)
print(p1.accidental.alter)
print(p1.nameWithOctave)
print(p1.midi)
p1.name="d#"
p1.octave=3
print(p1.nameWithOctave)
p2=p1.transpose("M7")
print(p2)
print(p2.nameWithOctave)
repr(p2)
doSustenido=note.Note("C#4")
print(doSustenido.name)
print(doSustenido.pitch.name)
print(doSustenido.octave)
print(doSustenido.pitch.octave)
print(doSustenido.pitch.spanish)
#doSustenido.spanish nao funciona
print(doSustenido.pitch.unicodeName)
print(doSustenido.pitch.getEnharmonic())
print(doSustenido.pitch.getLowerEnharmonic())

minima=duration.Duration("half")
dottedQuarter=duration.Duration(1.5)#intermediario entre seminima e colcheia
#aqui se tem uma forma de notacao e de set baseado nas colcheias(1/8)
print(dottedQuarter.quarterLength)
#quarterLength ratorna a duracao da nota em relacao a uma colcheia
print(minima.quarterLength)
print(minima.type)
print(dottedQuarter.type)
#type diz o "nome" da nota no padrao americano, que eh sua duracao
print(minima.dots)
print(dottedQuarter.dots)
#dot eh o nome para o ponto que fica do lado de uma nota e demonstra que ela eh uma nota "quebrada",
#ou seja, um intermediario entre dois tipos de notas conhecidos, como um intermediario entre uma seminima e uma colcheia

for x in range(2,4):
	dottedQuarter.dots=x
	print(dottedQuarter.quarterLength)
	#quarterLength eh em relacao a "quantidade" de colcheias de cada nota

dottedQuarter.quarterLength=0.25
print(dottedQuarter.type)
#type eh o "nome" da nota
print(dottedQuarter.dots)
if dottedQuarter.dots==0:
	print ("eh igual a zero porque essa mudanca fez com que ele se tornasse uma nota natural")

#observacao do python:
# / imprime com ponto flutuante e // imprime so o inteiro("truncamento")
print(6/5)
print(6//5)

n1=note.Note()
print(n1.pitch)
print(n1.duration)
#o default de um objeto note eh o C4, com duracao de uma semibreve (um tempo inteiro)

#podemos depois modificar n1

n1.pitch.nameWithOctave = 'E-5'
n1.duration.quarterLength=3.0 
print(n1.duration.type)
print(n1.duration.dots)
print(n1.pitch.name)
print(n1.pitch.accidental)
print(n1.octave)
print(n1.name)
print(n1.quarterLength)
f6=note.Note("F6")
f6.lyric="Some lyric stuff here"
print(f6)
print(f6.lyric)
n1.addLyric(n1.nameWithOctave)
n1.addLyric(n1.pitch.pitchClassString)
n1.addLyric('QL: %s' % n1.quarterLength)
n1.show()
n1.quarterLength=6.25
n1.show()