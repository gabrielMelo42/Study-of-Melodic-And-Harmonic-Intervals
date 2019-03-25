#example

from music21 import *
n=note.Note("D#3")
n.duration.type='half'
n.show()
littleMelody=converter.parse("tinynotation 3/4 c4 d8 f g16 a g f#")
littleMelody.show()
littleMelody.show('midi')