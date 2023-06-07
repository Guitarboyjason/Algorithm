"""
왼쪽에 더 큰 수가 수신을 한다.
(가장 먼저 만나는 큰 수 로 봐야할 듯)
N은 500_000까지 가능
단순하게 완탐은 시간초과 가볍게 넘김
NlogN도 불가능할 것 같다.

스택..

뒤에서부터 확인을 해야하나
작아지는건 무시
큰 수가 나오게 되면 업데이트 하는데
무시했던 수들을 현재의 index로 덮어씌운다?

앞에서부터 확인해도 되겠네

"""

import sys

input = sys.stdin.readline

N = int(input())
towers = list(map(int, input().split()))

stack = []

recept_tower = [0 for _ in range(N)]
for idx, i in enumerate(towers[::-1]):
    idx = N - idx - 1
    # if not stack:
    #     stack.append([i,idx])
    # else:
    while stack and stack[-1][0] < i:
        node = stack.pop()[1]
        recept_tower[node] = idx + 1
    stack.append([i, idx])
# print(stack)
print(*recept_tower)
