# menuOption.py

menuArray = []	

def menuPrompt():
    f = open('menuOption.txt')

    for line in f:
        b = [line.strip() for line in f]

    print(*b, sep = '\n')
