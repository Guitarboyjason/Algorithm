# 한번에 한명만 방문
# 난로 -> 성냥
# K개의 성냥이 있다. 최대 K번 킬 수 있다. 처음엔 꺼져있다.
# 혼자있을 떄는 난로를 키지 않는다.
# 난로가 켜져있는 시간의 최솟값을 구해라....
# 사실 친구가 연속해서 들어오는 

# True False로 배열을 만들어서 True의 갯수를 나중에 return하면 될 것.
from collections import deque
import sys
input = sys.stdin.readline

N,K = map(int, input().split())
friends = [int(input())for _ in range(N)]

# fireplace = [False for _ in range(friends[-1]+1)]
## diff들에 대해서 dictionary형식으로 접근하려 했는데 될것 같은데...?
## 문제가 얼마나 차이나는게 최소인지를 알 방법이 없어
## dict로 접근하지 말고 그냥 queue를 만들어서 popleft 몇번 하면 되는거 아닌가...? 
## 기본적으로 N == K 면 return N하면 돼
## K == N-1 이면 차이의 최소를 빼 내고 -2만큼을 빼서 더한다...?
# diffs = dict()
answer = N
diffs = list()
if N == K:
    print(answer)
else:
    for i in range(1,N):
        diffs.append(friends[i] - friends[i-1])

    diffs.sort()
    diffs = deque(diffs)
    # print(diffs)
    for i in range(N-K):
        answer += diffs.popleft()-1
    
    print(answer)
    
# print(diffs)

