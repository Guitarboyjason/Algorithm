import sys

def quad_tree(graph):
    n = len(graph)
    if n == 1:
        return graph[0][0]
    tmp = []
    if sum([sum(list(map(int,list(i)))) for i in graph]) == n**2 or sum([sum(list(map(int,list(i)))) for i in graph]) == 0:
        return graph[0][0]

    else:
        string_return = "("
        for i in range(2):
            for j in range(2):
                string_return += quad_tree([dots[n//2*j:n//2*(j+1)] for dots in graph[n//2*i:n//2*(i+1)]])
                
        string_return += ")"
        return string_return

N = int(input())
graph = [input()for _ in range(N)]
print(quad_tree(graph))