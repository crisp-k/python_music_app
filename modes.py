# modes.py

chromaticRoots = ['Cb', 'C', 'C#', 'Db', 'D', 'D#', 'Eb',
                   'E', 'E#', 'Fb', 'F', 'F#', 'Gb', 'G', 
                   'G#', 'Ab', 'A', 'A#', 'Bb', 'B', 'B#']
modes = ['Ionian', 'Dorian', 'Phyrgian', 'Lydian', 
          'Mixolydian', 'Aeolian', 'Locrian']

for root in chromaticRoots:
    for mode in modes:
        print(root + ' ' + mode)
