# note.py 

import random

 
def noteList(scalePos):
    # Aquires potential note choices based on users chosen scale.
    f = open('notePool.txt')

    # Combs through note text file and creates an array.
    for line in f: 
        b = [line.strip() for line in f]

    scaleNotes = b.pop(scalePos)

    # Creates another array by spliting popped string.
    notePool = scaleNotes.split(' ')
    print(*notePool, sep = ' ')

    b.clear()
    f.close()

    noteRand(notePool)


def noteRand(notePool):
    # Uses notePool to randomly pick number of notes- chosen by user.

    noteRand = []
    i = 0 
    toPull = int(input("How many notes to pull?: "))

    while i < toPull: 
        # print(random.choice(notePool))
        i = i + 1
        noteRand.append(random.choice(notePool))

    print(noteRand)
	

