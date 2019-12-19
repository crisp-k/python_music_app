# permutataions.py
import itertools
# a = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
# b = list(itertools.permutations(a, ))
# print(b)

a = "A B C D E F G".split()
for permutation in itertools.permutations(a, ):
    print(*permutation)