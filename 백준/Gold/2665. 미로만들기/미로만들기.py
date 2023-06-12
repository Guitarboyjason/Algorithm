from collections import deque
import sys

input = sys.stdin.readline


def pre_processing():
    n = int(input())
    graph = [list(input()) for _ in range(n)]
    return n, graph


def dijkstra():
    queue = deque()
    queue.append((0, 0, 0))  # x,y,cnt

    while queue:
        x, y, cnt = queue.popleft()
        for nx, ny in directions:
            nx += x
            ny += y
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == "1" and visited[nx][ny] > cnt:
                    visited[nx][ny] = cnt
                    queue.append((nx, ny, cnt))
                elif graph[nx][ny] == "0" and visited[nx][ny] > cnt + 1:
                    visited[nx][ny] = cnt + 1
                    queue.append((nx, ny, cnt + 1))
    print(visited[n - 1][n - 1])


if __name__ == "__main__":
    n, graph = pre_processing()
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    visited = [[3000 for _ in range(n)] for _ in range(n)]
    visited[0][0] = 0
    dijkstra()
