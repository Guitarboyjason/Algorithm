def make_arr(nodes, parent):
    if -1 in nodes_parent:
        for i in nodes:
            if i[0] == parent:
                nodes_parent[i[1]] = parent
                return make_arr(nodes,nodes_parent[i[1]])
            elif i[1] == parent:
                nodes_parent[i[0]] = parent
                return make_arr(nodes,nodes_parent[i[0]])

N = int(input())
nodes = []
for _ in range(N-1):
    x,y = map(int,input().split())
    nodes.append([x,y])

print(nodes)
nodes_parent = [-1]*(N+1)

nodes_parent[0] = 0
nodes_parent[1] = 0

make_arr(nodes,1)
print(nodes_parent)
