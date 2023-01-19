# 재귀로 풀어야 할 듯?

from collections import deque

direction_x = [-1,0,0,1]
direction_y = [0,-1,1,0]
def BFS(graph,root):
    visited = []
    queue = deque([root])

    while queue:
        n = queue.popleft()
        if graph[n[0]][n[1]] == "#" and n not in visited:
            visited.append(n)
            for i in range(4):
                if n[0] + direction_x[i] < len(graph) and n[0] + direction_x[i] >= 0 \
                    and n[1] + direction_y[i] < len(graph) and n[1] + direction_y[i] >= 0:
                    queue.append((n[0]+direction_x[i],n[1]+direction_y[i]))
    return visited

T = int(input())
for test_case in range(1,T+1):
    counter = 0
    N = int(input())

    arr = []
    for i in range(N):
        line = input()
        arr.append(line)
        if "#" in line:
            counter += line.count("#")
    count_x = 0
    count_y = 0
    root = (-1,-1)
    compare = []
    if counter == 1:
        print(f"#{test_case} yes")
    else:
        try:
            for i_index,i in enumerate(arr):
                for j_index,j in enumerate(i):
                    if j == "#":
                        if arr[i_index][j_index] == "#":
                            root = (i_index,j_index)
                            if compare == []:
                                compare = sorted(BFS(arr,root))
                            else:
                                if compare != sorted(BFS(arr,root)):
                                    raise Exception
            print(f"#{test_case} yes")
        except:
            print(f"#{test_case} no")

        # if root != (-1,-1):
        #     break

