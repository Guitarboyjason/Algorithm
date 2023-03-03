N = int(input())

arr = [-1]*(N+1)

for i in range(2,N+1):
    if i == 3 or i == 5:
        arr[i] = 1
    if i>5 :
        if arr[i-3] != -1:
            arr[i] = arr[i-3]+1
        if arr[i-5] != -1:
            arr[i] = arr[i-5]+1

print(arr[N])
