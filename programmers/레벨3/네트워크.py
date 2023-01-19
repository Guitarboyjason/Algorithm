#Bfs로 구현할 건데

from collections import deque
def bfs(computers):
    stack = deque()
    while computers:
        connected = deque()
        stack.append(computers.pop())
        while stack:
            tmp = stack.popleft()
            for index,i in enumerate(tmp):
                if i == 1:
                    connected.append()


def solution(n,computers):
    answer = 0
    visited = [False for i in range(n)]
    for com in range(n):
        if visited[com] == False:
            DFS(n,computers,com,visited)
            answer += 1
    return answer

def DFS(n,computers,com,visited):
    visited[com] = True
    for connect in range(n):
        if connect != com and computers[com][connect] == 1:
            if visited[connect] == False:
                DFS(n,computers,connect,visited)


n = 3
computers = [[1,1,0],[1,1,1],[0,1,1]]

print(solution(n,computers))
