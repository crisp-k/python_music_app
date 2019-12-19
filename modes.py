# modes.py

i = 0
n = 0

chroma = ('Cb', 'C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'E#', 'Fb', 'F', 'F#', 'Gb', 'G',   'G#', 'Ab', 'A', 'A#', 'Bb', 'B', 'B#')

modes = ('Ionian', 'Dorian', 'Phyrgian', 'Lydian', 'Mixolydian', 'Aeolian', 'Locrian')

while i <= len(chroma):
    while n <= len(modes):
        chromaModes = (chroma[i] + ' ' + modes[n] + '\n')
        print(chromaModes)
        n = n + 1
        if n == len(modes):
            i = i + 1
            n = 0