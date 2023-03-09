from collections import deque
import sys
sys.setrecursionlimit = 10**6
input = sys.stdin.readline
dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def DFS(start):
    stack = deque()
    stack.append(start)
    while stack:
        now_area_x, now_area_y = stack.pop()
        if visited[now_area_x][now_area_y] == False:
            visited[now_area_x][now_area_y] = True
            for i in range(4):
                next_area_x = now_area_x + dir[i][0]
                next_area_y = now_area_y + dir[i][1]
                if 0 <= next_area_x < N and 0 <= next_area_y < N \
                        and arr[next_area_x][next_area_y] > rain_height:
                    stack.append([next_area_x, next_area_y])


N = int(input())
arr = [list(map(int, input().split()))for _ in range(N)]
# print(max(max(arr)))
cnt_list = list()
for rain_height in range(max(max(arr))+1):
    cnt = 0
    visited = [[False for _ in range(N)]for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False and arr[i][j] > rain_height:
                DFS([i, j])
                cnt += 1
                # print(visited)
                # print(cnt)
    cnt_list.append(cnt)
print(max(cnt_list))
