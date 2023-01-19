def dfs(triangle,sum,n,now_x,now_y):
    if n == 0:
        return sum
    else:
        if now_y ==
        left = triangle[now_x][now_y]
        return triangle[now_x][now_y] + max(dfs())

def solution(triangle):
    answer = 0
    n = len(triangle)
    dfs(triangle,0,n)
    return answer

