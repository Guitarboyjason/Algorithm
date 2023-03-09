
from collections import deque

N, K = map(int, input().split())

queue = deque(i for i in range(1, N+1))
yosepus = list()
cnt = 0
while queue:
    cnt += 1
    node = queue.popleft()
    if cnt == K:
        yosepus.append(node)
        cnt = 0
        continue
    queue.append(node)

print("<", end="")
for i in range(len(yosepus)-1):
    print(yosepus[i], end=", ")
print("{}>".format(yosepus[-1]))
