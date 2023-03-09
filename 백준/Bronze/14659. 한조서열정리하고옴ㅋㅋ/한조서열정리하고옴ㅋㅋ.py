import sys
input = sys.stdin.readline

N = int(input())
archor = list(map(int,input().split()))
answer = []
for i in range(N-1):
    cnt = 0
    for j in range(i+1,N):
        if archor[i] > archor[j]:
            cnt += 1
        else:
            break
    answer.append(cnt)
print(max(answer))