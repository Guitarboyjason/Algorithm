import sys
input = sys.stdin.readline

N,K = map(int, input().split())
friends = [int(input())for _ in range(N)]

answer = N
diffs = list()
if N == K:
    print(answer)
else:
    for i in range(1,N):
        diffs.append(friends[i] - friends[i-1])

    diffs.sort(reverse=True)
    for i in range(N-K):
        answer += diffs.pop()-1
    
    print(answer)