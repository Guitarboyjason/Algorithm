#14425-문자열집합.py
import sys
input = sys.stdin.readline


N,M = map(int,input().split())
S = []
for i in range(N):
    S.append(input())
count = 0
for i in range(M):
    tmp = input()
    if tmp in S:
        count += 1
print(count)