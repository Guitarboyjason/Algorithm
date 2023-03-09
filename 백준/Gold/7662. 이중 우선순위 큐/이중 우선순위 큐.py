import heapq
import sys

input = sys.stdin.readline

for T in range(int(input())):
    k = int(input())
    max_q = []
    hq = []
    visited = [False]*1_000_001
    for i in range(k):
        command = input().split()
        if command[0] == "I":
            heapq.heappush(hq,(int(command[1]),i))
            heapq.heappush(max_q,(-int(command[1]),i))
            visited[i] = True
        elif command[1] == "1":
            while max_q and not visited[max_q[0][1]]:
                heapq.heappop(max_q)
            if max_q:
                visited[heapq.heappop(max_q)[1]]=False
        else:
            while hq and not visited[hq[0][1]]:
                heapq.heappop(hq)
            if hq:
                visited[heapq.heappop(hq)[1]] = False
    answer = []
    while hq and not visited[hq[0][1]]:
        heapq.heappop(hq)
    while max_q and not visited[max_q[0][1]]:
        heapq.heappop(max_q)
    if max_q:
        answer.extend([-max_q[0][0],hq[0][0]])
    else:
        answer.append("EMPTY")
    print(*answer)