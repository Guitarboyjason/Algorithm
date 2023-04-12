# 연결된 모든 노드의 색을 변경한다..?
# 만약 이미 색칠이 되어 있는데 칠해야하는 색과 다른 색이 칠해져있다면 False를 return하면 될 것.
from collections import deque
import sys
input = sys.stdin.readline
T = int(input())
for test_case in range(T):
    n,m = map(int,input().split())
    graph = {i+1 :[] for i in range(n)}
    # paint_color = [False for _ in range(n+1)]
    # print(graph)
    for _ in range(m):
        x,y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)
    visited = [-1 for _ in range(n+1)]
    try:
        DEFAULT_COLOUR = True
        while -1 in visited[1:]:
            root_index = visited[1:].index(-1) + 1
            queue = deque([(root_index,DEFAULT_COLOUR)])
            # print(queue)
            while queue:
                if -1 not in visited[1:]: # 무한루프 방지
                    break
                node, color = queue.popleft()
                # queue.(graph[node])
                for child in graph[node]:
                    if visited[child] == -1:
                        queue.append((child,not color))
                    elif visited[child] == color:
                        raise()
                if visited[node] != -1 and visited[node] != color: # 불가능할때의 조건
                    raise()
                visited[node] = color
        print("possible")
    except:
        print("impossible")