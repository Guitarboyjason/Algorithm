def solution(triangle):
    answer = 0
    tmp_triangle = [[0] + i +[0]for i in triangle]
    for i in range(1,len(tmp_triangle)):
        for j in range(1,len(tmp_triangle[i])-1):
            tmp_triangle[i][j] += max(tmp_triangle[i-1][j-1],tmp_triangle[i-1][j])
    return max(tmp_triangle[-1])