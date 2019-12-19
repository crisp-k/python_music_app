# scale.py

import random


def scaleAquire():
    f = open('scale.txt')

    for line in f: 
        b = [line.strip() for line in f]

    print(*b, sep = '\n')
    scale = input("Which scale to use?: ")
    scalePos = b.index(scale)

    f.close()

    return scalePos


def scaleRand():

    f = open('scale.txt')
   
    for line in f:
        c = [line.strip() for line in f]

    print(random.choice(c))
    f.close()
    