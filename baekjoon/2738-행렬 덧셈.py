N,M = map(int,input().split())

A = [[]for _ in range(N)]
# B = [[]for _ in range(N)]

for i in range(N):
    num1,num2,num3 = map(int,input().split())
    A[i] = [num1,num2,num3]
for i in range(N):
    num1,num2,num3 = map(int,input().split())
    A[i][0]+=num1
    A[i][1]+=num2
    A[i][2]+=num3
for i in range(N):
    for j in range(M):
        print(A[i][j],end=" ")
    print()