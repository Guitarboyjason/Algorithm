# 1은 땅, 0은 바다.
# 가로 세로 대각선으로 1칸 떨어져 있는 땅은 이어져 있는 땅.
# 서로 떨어져 있는 땅의 갯수는?
def find_island(start_x,start_y):
    dx = [1,1,1,0,0,-1,-1,-1]
    dy = [-1,0,1,-1,1,-1,0,1]

    stack = list()
    stack.append([start_x,start_y])
    while stack:
        tmp = stack.pop()
        island_map[tmp[0]][tmp[1]] = 0
        for i in range(8):
            tmp_x = tmp[0]+dx[i]
            tmp_y = tmp[1]+dy[i]
            if 0<=tmp_x<h and 0<=tmp_y<w and island_map[tmp_x][tmp_y] == 1:
                stack.append([tmp_x,tmp_y])

w, h = map(int,input().split())

while w!= 0 and h != 0:
    island_map = [list(map(int,input().split()))for _ in range(h)]

    cnt = 0
    for idx_x,i in enumerate(island_map):
        for idx_y,j in enumerate(i):
            if j == 1:
                find_island(idx_x,idx_y)
                cnt += 1
    print(cnt)
    w, h = map(int,input().split())
