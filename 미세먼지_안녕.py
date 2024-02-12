# 1.미세먼지가 확산된다. 확산은 미세먼지가 있는 모든 칸에서 동시에 일어난다.
# (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산된다.
# 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
# 확산되는 양은 Ar,c/5이고 소수점은 버린다.
# (r, c)에 남은 미세먼지의 양은 Ar,c - (Ar,c/5)×(확산된 방향의 개수) 이다.
# 2.공기청정기가 작동한다.
# 공기청정기에서는 바람이 나온다.
# 위쪽 공기청정기의 바람은 반시계방향으로 순환하고, 아래쪽 공기청정기의 바람은 시계방향으로 순환한다.
# 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동한다.
# 공기청정기에서 부는 바람은 미세먼지가 없는 바람이고, 공기청정기로 들어간 미세먼지는 모두 정화된다.

import copy
import sys
input = sys.stdin.readline


directions = [(1,0),(-1,0),(0,1),(0,-1)]
def inputer():
    R,C,T = map(int,input().split())
    board = [list(map(int,input().split()))for _ in range(R)]
    return R,C,T,board

def spread_every_dust():
    n_board = copy.deepcopy(board)
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0: #미세먼지
                spread_dust((i,j))

def spread_dust(root):
    spread_cnt = 0
    x,y = root
    for nx,ny in directions:
        nx += x
        ny += y
        if 0<=nx<R and 0<=ny<C

if __name__ == "__main__":
    R,C,T,board = inputer()
    print(board)