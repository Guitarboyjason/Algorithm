def quad_tree(graph):
    n = len(graph)
    if n == 1:
        return graph[0][0]
    if sum([sum(list(map(int,list(i)))) for i in graph]) == n**2 or sum([sum(list(map(int,list(i)))) for i in graph]) == 0:
        # 전체를 더해서 n**2라면 전체가 1이라는 뜻이고, 0이라면 전체가 0이라는 뜻입니다.
        return graph[0][0]

    else:
        string_return = "("
        for i in range(2):
            for j in range(2):
                string_return += quad_tree([dots[n//2*j:n//2*(j+1)] for dots in graph[n//2*i:n//2*(i+1)]])
                #설명할 때 dots[n//2*j:n//2*(j+1)+1] 일 것이라고 설명했었는데 n은 len(graph)이므로 위와 같이 구현하는 것이 맞습니다.
        string_return += ")"
        return string_return

N = int(input())
graph = [input()for _ in range(N)]
print(quad_tree(graph))