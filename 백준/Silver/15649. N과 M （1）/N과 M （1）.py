from itertools import permutations
N, M = map(int, input().split())
for i in list(permutations(range(1, N+1), M)):
    print(*i)
