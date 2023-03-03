N = int(input())
arr = [0 for _ in range(N+1)]
arr[1] = 0
for i in range(2,N+1):
    arr[i] = arr[i-1] + 1
    if i%2 == 0 and arr[i//2] + 1 < arr[i]:
        arr[i] = arr[i//2]+1
    if i%3 == 0 and arr[i//3] + 1 < arr[i]:
        arr[i] = arr[i//3]+1
print(arr[N])
