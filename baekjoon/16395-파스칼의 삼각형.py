n,k = map(int,input().split())
triangle = [[1]*i for i in range(1,n+1)]
# print(triangle)
for i in range(2,n):
    for j in range(1,i):
        triangle[i][j] = triangle[i-1][j] + triangle[i-1][j-1]
# print(triangle)
print(triangle[n-1][k-1])
# print(triangle)11 3
