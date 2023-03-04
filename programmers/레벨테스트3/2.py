from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    dict_roads = {i+1 : [] for i in range(n)}
    for start,dest in roads:
        dict_roads[start].append(dest)
        dict_roads[dest].append(start)
    dp = [500001 for _ in range(n+1)]
    dp[destination] = 0
    queue = deque([destination])
    while queue:
        node = queue.popleft()
        for next in dict_roads[node]:
            if dp[next] > dp[node]+1:
                dp[next] = dp[node]+1
                queue.append(next)
                ## 다익 끝
    
    for unit in sources:
        if dp[unit] == 500001:
            answer.append(-1)
        else:
            answer.append(dp[unit])
        
    # for unit in sources:
        
    return answer

n = 3
roads = [[1,2],[2,3]]
sources = [2,3]
destination = 1
print(solution(n,roads,sources,destination))