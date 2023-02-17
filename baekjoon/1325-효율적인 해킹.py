from collections import deque
N,M = map(int,input().split())
graph = dict()
for i in range(N):
    graph[i+1] = []
for _ in range(M):
    A,B = map(int,input().split())
    graph[B].append(A)


hacking_cnt = [-1]
for i in range(1,N+1):
    hacking_possible = set()
    queue = deque()

    # print(hacking_possible)
    cnt = 0 
    queue.append(i)
    while queue:
        node = queue.popleft()
        # print(node)
        # print(hacking_possible)
        if node not in hacking_possible:
            hacking_possible.add(node)
            queue.extend(graph[node])
            cnt += 1
    hacking_cnt.append(cnt)    
# print(hacking_cnt)
answer = [index for index,i in enumerate(hacking_cnt) if i == max(hacking_cnt)]
print(answer)