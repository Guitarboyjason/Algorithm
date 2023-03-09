from collections import deque
import sys
sys.setrecursionlimit = 10**6
input = sys.stdin.readline

dir = [[-1, 2], [1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, 1], [-2, -1]]


def BFS():
    queue = deque()
    queue.append(now_knight)
    while queue:
        x, y = queue.popleft()
        if [x, y] == knight_want:
            return cnt_arr[knight_want[0]][knight_want[1]]
        if visited[x][y] == False:
            visited[x][y] = True
            for i in range(len(dir)):
                nx = x + dir[i][0]
                ny = y + dir[i][1]
                if 0 <= nx < I and 0 <= ny < I:
                    queue.append([nx, ny])
                    cnt_arr[nx][ny] = cnt_arr[x][y]+1
test_case = int(input())
for _ in range(test_case):
    I = int(input())
    now_knight = list(map(int, input().split()))
    knight_want = list(map(int, input().split()))
    cnt_arr = [[-1 for _ in range(I)]for _ in range(I)]
    cnt_arr[now_knight[0]][now_knight[1]] = 0
    visited = [[False for _ in range(I)]for _ in range(I)]
    print(BFS())

