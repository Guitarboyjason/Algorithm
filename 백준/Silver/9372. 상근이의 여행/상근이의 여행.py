import sys
input = sys.stdin.readline
for T in range(int(input())):
    N,M = map(int,input().split())
    planes = [input()for _ in range(M)]
    print(N-1)