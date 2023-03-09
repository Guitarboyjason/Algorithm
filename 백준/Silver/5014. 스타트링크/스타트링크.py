
import heapq
import sys

INF = sys.maxsize

F, S, G, U, D = map(int, input().split())

# 층을 배열로 만들어서 해당 배열에 몇번만에 도달할 수 있는지를 정함


def dijkstra(start):
    cnt_commands = [INF for _ in range(F+1)]
    cnt_commands[start] = 0
    hq = []
    heapq.heappush(hq, start)
    while hq:
        node = heapq.heappop(hq)
        if node + U <= F and cnt_commands[node + U] > cnt_commands[node] + 1:
            cnt_commands[node + U] = cnt_commands[node] + 1
            heapq.heappush(hq, node+U)
        if node - D > 0 and cnt_commands[node - D] > cnt_commands[node] + 1:
            cnt_commands[node - D] = cnt_commands[node] + 1
            heapq.heappush(hq, node-D)
    return cnt_commands


if dijkstra(S)[G] == INF:
    print("use the stairs")
else:
    print(dijkstra(S)[G])
