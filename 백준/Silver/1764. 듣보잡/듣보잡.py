#1764-듣보잡.py

import sys

N,M = map(int, sys.stdin.readline().split())

no_heard = {}
no_heard_seen = []
for i in range(N):
    no_heard[sys.stdin.readline().rstrip()] = i

for i in range(M):
    people = sys.stdin.readline().rstrip()
    if people in no_heard:
        no_heard_seen.append(people)
    # if people in no_heard:
    #     no_heard_seen.append(people)
no_heard_seen.sort()
print(len(no_heard_seen))
for i in no_heard_seen:
    print(i)
