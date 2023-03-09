N = int(input())

computer = [[]for _ in range(N+1)]

pair = int(input())

pairs = [list(map(int,input().split()))for _ in range(pair)]

for i in pairs:
    computer[i[0]].append(i[1])
    computer[i[1]].append(i[0])

def DFS(arr,start):
    stack = list()
    visit = list()
    stack.append(start)
    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(arr[node])
    return visit

print(len(DFS(computer,1))-1)
