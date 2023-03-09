def find_DFS(arr,start_node):
    visit = list()
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            for j in range(len(arr[node])-1,-1,-1):
                stack.append(arr[node][j])
    return visit
def find_BFS(arr,start_node):
    visit = list()
    queue = list()

    queue.append(start_node)

    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(arr[node])
    return visit

N,M,V = map(int,input().split())

arr_lines = [list(map(int,input().split()))for _ in range(M)]

arr = [[]for _ in range(N+1)]

for i in arr_lines:
    arr[i[0]].append(i[1])
    arr[i[1]].append(i[0])

for i in arr:
    i.sort()

start_node = V




arr_DFS = find_DFS(arr,start_node)
arr_BFS = find_BFS(arr,start_node)

for i in arr_DFS:
    print(i,end=' ')
print()
for i in arr_BFS:
    print(i,end=' ')

