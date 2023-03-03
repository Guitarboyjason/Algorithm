N = int(input())

arr = [i for i in range(N+1)]

for i in range(2,N+1):
    arr[i] = arr[i-1]+1
    if i*i <= N+1:
        arr[i*i] = 1
