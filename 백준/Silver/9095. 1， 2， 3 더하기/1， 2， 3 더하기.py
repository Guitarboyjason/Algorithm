T = int(input())
for i in range(T):
    n = int(input())
    arr = [-1] * (n+1)
    for j in range(1,n+1):
        if j == 1:
            arr[j] = 1
        elif j == 2:
            arr[j] = 2
        elif j == 3:
            arr[j] = 4
        else:
            arr[j] = arr[j-1]+arr[j-2]+arr[j-3]
    print(arr[n])
