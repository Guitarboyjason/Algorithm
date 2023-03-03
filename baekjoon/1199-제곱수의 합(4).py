N = int(input())

arr = [i for i in range(N+1)]

for i in range(2,N+1):
    if i*i <= N:
        arr[i*i] = 1
    if arr[i-1] + 1 < arr[i]:
        arr[i] = arr[i-1]+1
    for j in range(1,int(i/2)):     #이부분이 시간 많이 잡아먹는듯
        if arr[j] + arr[i-j] < arr[i]:
            arr[i] = arr[j]+arr[i-j]

print(arr[N])
