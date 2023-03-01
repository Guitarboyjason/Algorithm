from itertools import permutations

N, M = map(int, input().split())
set(permutations(range(1, N+1)+range(1, N+1), M))
