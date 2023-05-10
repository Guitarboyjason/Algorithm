# 내부의 공기를 어떻게 표현할지가 관건인 것 같음
# 0 -> 공기
# 1 -> 치즈
# 차례차례로 지우면 안되고 지울 것들을 저장해 뒀다가 한번에 지우기
# 이후 내부의 공기를 외부 공기와 접촉했는지 update
# 맨 가장자리에는 치즈가 놓이지 않는다.

import sys
input = sys.stdin.readline

# 주어진 상태에서 한시간 뒤의 모습을 update할 함수
directions = [(0,1),(0,-1),(1,0),(-1,0)]
def after_1_hour():
    melting_cheese_list = []
    
    for i in range(1,N-1):#가장자리에는 치즈가 없음
        for j in range(1,M-1):
            if board[i][j] == 1:
                out_connected_cnt = 0
                for nx,ny in directions:
                    nx += i
                    ny += j
                    if 0<=nx<N and 0<=ny<M:
                        if board[nx][ny] == 0:
                            out_connected_cnt += 1
                if out_connected_cnt >= 2:
                    melting_cheese_list.append((i,j))
    # 한번에 업데이트
    for x,y in melting_cheese_list:
        board[x][y] = 0
    # 공기에 대한 업데이트
    update_air()        
    
    
def update_air():
    visited = []
    for i in range(1,N-1):
        for j in range(1,M-1):
            if (i,j) not in visited:
                if board[i][j] == 2:
                    list_to_update,flag = update_dfs((i,j))
                    visited.extend(list_to_update)
                    if flag:
                        for x,y in list_to_update:
                            board[x][y] = 0
    
def update_dfs(root) -> list([list,bool]):
    stack = [root]
    visited = [root]
    flag_to_update = False
    list_to_update = [root]
    while stack:
        x,y = stack.pop()
        for nx,ny in directions:
            nx += x
            ny += y
            if 0<=nx<N and 0<=ny<M:
                if (nx,ny) not in visited:
                    visited.append((nx,ny))
                    if board[nx][ny] == 2:
                        list_to_update.append((nx,ny))
                        stack.append((nx,ny))
                    if board[nx][ny] == 0:
                        flag_to_update = True
                        stack.append((nx,ny))
    
    return [list_to_update,flag_to_update]
def cnt_time():
    cnt = 0
    while True:
        if sum([sum(i) for i in board]) == 0:
            break
        after_1_hour()
        cnt += 1
    return cnt

N,M = map(int,input().split())
board = [list(map(int,input().split()))for _ in range(N)]
# 외부와 내부를 확인하기 위한 초기화
for i in range(1,N-1):
    for j in range(1,M-1):
        if board[i][j] == 0:
            board[i][j] = 2 # 내부라는 뜻
update_air()

print(cnt_time())