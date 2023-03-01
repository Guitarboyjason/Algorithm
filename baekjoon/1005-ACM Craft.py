from collections import deque
import sys
sys.stdin = open("baekjoon/input.txt","rt")

for _ in range(int(input())):
    N,K = map(int,input().split())
    building_time = [-1]+list(map(int,input().split()))
    graph = dict()
    for _ in range(K):
        first,later = map(int,input().split())
        if later in graph:
            graph[later].append(first)
        else:
            graph[later]= [first]
    
    W = int(input())
    queue = deque()
    
    queue.append(W)
    timer = 0
    while queue:
        node = queue.popleft()
        timer += building_time[node]
        if node in graph:
            queue.append(max(graph[node],key=lambda x:building_time[x]))
            # queue.extend(graph[node])
    print(timer)