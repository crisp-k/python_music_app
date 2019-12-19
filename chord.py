# chord.py
import random

def randChord(scalePos):
    f = open('chord.txt')
    numChord = ['I', 'ii', 'iii', 'IV', 'V', 'vi', 'vii']

    for line in f:
        b = [line.strip() for line in f]

    chords = b.pop(scalePos)
    chordsClean = chords.split(' ')
    
    chordPool = {key:value for key, value in zip(numChord, chordsClean)}

    toPull = input("How many chords would you like to pull? ")
    
    chordRand = random.sample(chordPool.items(), int(toPull))
    print(*chordRand)    

# print(*numChord, sep='\n')

