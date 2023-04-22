# 신맛은 모든 신맛의 곱
# 쓴맛은 모든 쓴맛의 합
# 신맛과 쓴맛의 차이가 가장 작은 요리
from itertools import combinations

N = int(input())

taste = [list(map(int,input().split())) for _ in range(N)]
# N 의 범위가 10까지니까 브루트포스로 접근해도 될듯


# print(list(combinations(taste)))
possible = []
for i in range(1,N+1):
    possible.extend(list(combinations(taste,i)))
# print(possible)

# min([i for i in possible])
for idx,i in enumerate(possible):
    sin = 1
    ssn = 0
    for taste in i:
        sin *= taste[0]
        ssn += taste[1]
        
    possible[idx] = abs(sin-ssn)
# print(possible)
print(min(possible))