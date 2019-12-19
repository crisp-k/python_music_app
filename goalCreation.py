# goalCreation.py

i = 0
n = 0

f = open('scale.txt')
for line in f:
    Scale = [line.strip() for line in f]
f.close()

f = open('practice.txt')
for line in f:
    array2 = ('a', 'b', 'c', 'd', 'e', 'f')

f = open('goals.txt', 'w+')

while i <= len(array1):
    while n <= len(array2):
        savedLine = (str(array1[i]) + array2[n] + '\n')
        f.write(savedLine)
        n = n + 1
        if n == len(array2):
            i = i + 1
            n = 0

f.close()