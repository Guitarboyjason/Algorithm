"""
NxM, 0 : 이동가능, 1:벽
(1,1)에서 (N,M)으로 이동하려 한다.
최단 경로로 이동한다.
시작하는 칸과 끝나는 칸도 포함해서 센다.
한개의 벽을 부수고 이동하는 것이 좀 더 경로가 짧아진다면 벽을 한 개 까지 부수고 이동하여도 된다.
한 칸에서 이동할 수 있는 칸은 상하좌우로 인접한 칸이다.
"""

import sys
from pprint import pprint

input = sys.stdin.readline

# 모든 경우의 수 1000*1000을 하나하나 다 뚫어놓는다 --> 1_000_000
# Dfs로 최단경로를 구한다. ->


def dfs(board):
    start = (0, 0)
    # end = (N - 1, M - 1)
    stack = [start]
    # visited = [start]
    while stack:
        x, y = stack.pop()
        n_cnt = dp_board[x][y][1]
        for nx, ny in directions:
            nx += x
            ny += y
            if (
                0 <= nx < N
                and 0 <= ny < M
                and board[nx][ny] == 0
                and dp_board[nx][ny][1] > n_cnt + 1
            ):
                stack.append((nx, ny))
                dp_board[nx][ny][1] = n_cnt + 1


def dfs_after_update(board):
    start = (0, 0)
    # end = (N - 1, M - 1)
    stack = [start]
    # visited = [start]
    while stack:
        x, y = stack.pop()
        # n_cnt_list = dp_board[x][y]
        for nx, ny in directions:
            nx += x
            ny += y
            if 0 <= nx < N and 0 <= ny < M:
                if board[x][y] == 0:  # 원래 통로였다면, 현재 값을 반영해서 업데이트해줌
                    if dp_board[x][y][1] + 1 < dp_board[nx][ny][1]:
                        dp_board[nx][ny][1] = dp_board[x][y][1] + 1
                        stack.append((nx, ny))
                else:  # 원래 벽이였다면 현재 뚫린 값을 반영해준다.
                    if dp_board[nx][ny][1] > dp_board[x][y][0] + 1:
                        dp_board[nx][ny][1] = dp_board[x][y][0] + 1
                        stack.append((nx, ny))


N, M = map(int, input().split())

board = [list(map(int, list(input().rstrip()))) for _ in range(N)]
# pprint(board)

directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

dp_board = [[[-1, 1_000_001] for _ in range(M)] for _ in range(N)]
dp_board[0][0] = [-1, 1]  # 벽 뚫었다. 아니다.
# pprint(dp_board)
dfs(board)
# pprint(dp_board)

for i in range(N):
    for j in range(M):
        for nx, ny in directions:
            nx += i
            ny += j
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 1:
                    if (
                        dp_board[nx][ny][0] == -1
                        or dp_board[nx][ny][0] > dp_board[i][j][1] + 1
                    ):
                        dp_board[nx][ny][0] = dp_board[i][j][1] + 1  # 값 업데이트

# pprint(dp_board)
dfs_after_update(board)
pprint(dp_board)
tmp = [i for i in dp_board[N - 1][M - 1] if i != -1 and i < 1_000_001]
# print(tmp)
# if [i for i in dp_board[N-1][M-1] if i != -1]:
if tmp:
    print(min(tmp))
else:
    print(-1)
# 업데이트 해줬으니까 다시 DFS돌아야할 것 같은데


# 벽 처음 뚫고 이후 계속 진행하면 해당 값을 게속 업데이트 한다.
# 뚫지 않았을 때의 값은,,,? 어떻게 하니..
# 루트가 겹쳐서 나오는 경우는 없다.
"""
그럼 방문했는지를 확인하는건 결국 해당 칸에 적힌 최단 거리를 구한 값보다 작으면 방문하지 않은걸로
근데 지금의 값이 더 작다면 이는 업데이트 해야할 부분이다.
그럼 언제 한번씩 실행하면 좋을까

처음 벽 뚫기 전에 한번 쭉 돌고
벽을 한번만 뚫을 수 있으니까 위와같은 자료구조로 정할 수 있겠다.
"""
