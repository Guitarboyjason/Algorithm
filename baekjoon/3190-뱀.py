# def is_death()
from collections import deque
directions = [(1,0),(0,1),(0,-1),(-1,0)]
def snake(graph):
    # 꼬리 끝단을 어떻게 표현하지
    # 하나씩 cnt를 늘려가며 제일 작은 하나를 없애주면 되겠다.
    direction = 1
    pos_x,pos_y = 0,0
    cnt = 0 # 시간 확인
    if turn:
        next_turn = turn.popleft()
    while 0<=pos_x<N and 0<=pos_y<N:
        cnt += 1

        
        # 머리를 박으면서 끝나는 시간을 재야겠네
        nx,ny = pos_x + directions[direction][0], pos_y + directions[direction]
        
        #check
        if nx<0 or nx>=N or ny<0 or ny>=N or (graph[nx][ny] != "#" and graph[nx][ny] != -1):
            break
        
        else:
            pos_x = nx
            pos_y = ny
            if graph[pos_x][pos_y] != "#":
                tail_x = [i for i in]
            graph[pos_x][pos_y] = cnt
            
            # 꼬리 지우기
            
        
        if cnt == int(next_turn[0]): # 방향 맞추기
            if next_turn[1] == "L":
                direction -= 1
            else:
                direction += 1
            if direction == -1:
                direction = 3
            if direction == 4:
                direction = 0
            
            if turn:
                next_turn = turn.popleft()
            else:
                next_turn = ["-1", "-1"]    #돌지 않기 위해
    
    print(cnt)

N = int(input())
graph = [[-1 for _ in range(N)] for _ in range(N)]
graph[0][0] = 0
K = int(input())

# apples = [list(map(int,input().split()))for _ in range(K)]
for _ in range(K):
    for pos in list(map(int,input().split())):
        graph[pos[0]][pos[1]] = "#"
        

L = int(input())
turn = deque([list(input().split())for _ in range(L)])

