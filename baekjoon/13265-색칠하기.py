# 연결된 모든 노드의 색을 변경한다..?
# 노드의 색을 칠하고 연결된 노드들은 다른 색으로 칠한다.
# queue를 만들어 queue에 append 될 때 조건들을 따져 try,except로 print를 다르게 했습니다. 

import sys 
from collections import deque   # queue
input = sys.stdin.readline      # 시간초과 때문에 사용했습니다.

DEFAULT_COLOUR = True       # 색을 True와 False로 확인을 해줍니다.

T = int(input())
for test_case in range(T):
    n,m = map(int,input().split())
    graph = {i+1 :[] for i in range(n)}     # 딕셔너리 형태로 구현했습니다.
    for _ in range(m):
        x,y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)
    visited = [-1 for _ in range(n+1)]      # not visited를 -1로 구현했습니다. (False로 구현을 하니 color를 뒤집을 때 헷갈려서 이와 같이 구현)
    try:
        while -1 in visited[1:]:    # -1 이 존재한다면 -> 아직 visited하지 않은 노드 존재
            root_index = visited[1:].index(-1) + 1  # 0번째는 확인해주지 않으므로 index가 -1 형태로 나오기 때문에 +1로 상쇄
            queue = deque([(root_index,DEFAULT_COLOUR)])    # node의 index와 color를 넣어줍니다. (Default로 해도 괜찮은 이유는 연결 안된 노드들 중 처음 노드기 때문입니다.)
            while queue:
                if -1 not in visited[1:]: # 무한루프 방지용으로 적었는데 이게 없으면 시간 초과가 나옵니다. 일종의 early stop이네요
                    break
                node, color = queue.popleft()
                for child in graph[node]:       # 연결된 노드들을 확인
                    if visited[child] == -1:    # 아직 방문하지 않았다면
                        queue.append((child,not color)) # 색을 뒤집어 queue에 append
                    elif visited[child] == color:   # 연결된 노드의 색이 현재 색과 동일하다면
                        raise()                 # impossible을 출력
                visited[node] = color           # 현재 노드 색칠
        print("possible")
    except:
        print("impossible")