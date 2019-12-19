# static.tree.py

import random
import scale
import note
import menuOption
import chord

notePool = []


menuOption.menuPrompt()
menuChoice = int(input("Choice: "))

if menuChoice == 1:
    scale.scaleRand()
elif menuChoice == 2:
    scalePos = scale.scaleAquire()
    notePool = note.noteList(scalePos)
elif menuChoice == 3:
    scalePos = scale.scaleAquire()
    chord.randChord(scalePos)

