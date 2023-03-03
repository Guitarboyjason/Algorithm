N = int(input())

arr = [i for i in range(N+1)]
dp = 0
for i in range(2,N+1):
    if i * i <= N:
        dp = i
        arr[i*i] = 1
    if arr[i] < arr[i-1]+1:
        arr[i] = arr[i-1]+1
    for j in range(dp,0,-1):
        if j*j <= i and arr[i-j*j] + 1 <arr[i]:
            arr[i] = arr[i-j*j] + 1
print(arr[N])
