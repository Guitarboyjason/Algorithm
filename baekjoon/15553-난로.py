import sys
input = sys.stdin.readline

N,K = map(int, input().split())
friends = [int(input())for _ in range(N)]

## 기본적으로 N == K 면 return N하면 돼
## K == N-1 이면 차이의 최소를 빼 내고 -1만큼을 빼서 더한다...?
answer = N  # default
diffs = list() # 차이를 저장하는 배열
if N == K:
    print(answer)
else:
    for i in range(1,N):
        diffs.append(friends[i] - friends[i-1])

    diffs.sort(reverse=True) # pop()을 사용하기 위해, deque를 써도 되지만 변환하는 데 시간이 '조금' 소요되므로 list로 해결
    for i in range(N-K):
        answer += diffs.pop()-1
    
    print(answer)