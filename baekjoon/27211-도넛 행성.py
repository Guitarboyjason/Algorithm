# N 칸 위/아래로 움직이면 원래 자리로 돌아온다
# M 칸 왼/오른쪽으로 움직이면 원래 자리로 돌아온다.

# A = (p1,q1)에서 시작, B(p2,q2)에 도달할 수 있다 --> 같은 구역
# 도달할 수 없다 --> 다른 구역
# 탐험할 수 있는 빈 구역의 갯수가 몇개인가.
from collections import deque
directions = [(i,j) for j in range(-1,2) for i in range(-1,2) if i != j and (i==0 or j == 0)]


def donut_update_bfs(root,number):    # 인식 번호
    stack = list()
    visited = []
    stack.append(root)
    visited.append(root)
    while stack:
        x,y = stack.pop()
        donut_graph[x][y] = number  # 인식표 달기
        for nx,ny in directions:
            nx += x
            ny += y
            if 0<=nx<N and 0<=ny<M and (nx,ny) not in visited and donut_graph[nx][ny] == 0:
                stack.append((nx,ny))
                visited.append((nx,ny))

# print(directions)
N, M = map(int,input().split())
donut_graph = [list(map(int,input().split()))for _ in range(N)]
# 0 이면 비어있는 것, 1이면 숲으로 막혀있는 것.
area_number =  2
for x in range(N):
    for y in range(M):
        if donut_graph[x][y] == 0:
            donut_update_bfs((x,y),area_number)
            area_number += 1

# area_number은 실제 인식표보다 하나만큼 더 높음

def connect_finder(root):
    stack = list()
    stack.append(root)
    visited = [root]
    connect_nums = [donut_graph[root[0]][root[1]]]
    while stack:
        x,y = stack.pop()
        for nx,ny in directions:
            nx+=x
            ny += y
            if (not 0<=nx<N or not 0<=ny<M) and (nx,ny) not in visited:
                # print(1)
                if nx < 0:
                    nx = N-1
                if ny < 0:
                    ny = M-1
                if nx >= N:
                    nx = 0
                if ny >= M:
                    ny = 0
                visited.append((nx,ny))
                stack.append((nx,ny))
                # print(connect_nums)
                for nums in connect_nums:
                    # print(1)
                    connect_dict[nums].append(donut_graph[nx][ny])

connect_dict = {i:[] for i in range(2,area_number)}
nums_set = set([i for i in range(2,area_number)])
# print(nums_set)
for x in range(N):
    for y in range(M):
        if (x == 0 or x == N-1 or y == 0 or y == M-1) and (donut_graph[x][y] != 0 or donut_graph[x][y] != 1):   #영역별로 확인
            connect_finder((x,y))
for val in connect_dict.values():
    print(val)
    nums_set -= set(val)
print(nums_set)
# 결국 1로 둘러쌓인 0의 범위를 알아내는 것이 핵심인 것 같다.
# 처음에 빈 구역의 갯수를 단순하게 찾아내고, 이후 바운더리에서 하나의 점으로 연결되는 부분이 있는지를 확인한다.... 근데 이렇게만 하면 어려울 것 같은게
# 하나 뿐만 아니라 두개 구역 이상이 연결 된 경우는 어떻게 할까,,, 인식표처럼 0대신 숫자를 부여해서 구역을 나눠볼까

                

        