
# 0.5 씩 좌우로 간격을 둬야 한다.
# 그럼 L 만큼 커버가 가능한거네

from collections import deque
N, L = map(int, input().split())
location = list(map(int, input().split()))

location.sort()
location = deque(location)
# print(location)
start = location.popleft()
cnt = 1
while len(location) != 0:
    node = location.popleft()
    if start + L - 1 < node:
        start = node
        cnt += 1
print(cnt)
