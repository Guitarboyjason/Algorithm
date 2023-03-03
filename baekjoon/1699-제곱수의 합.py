N = int(input())
arr = [i * i for i in range(N+1)]

count = 0
while N != 0:
    minus = 0
    for i in range(len(arr)):
        if N - arr[i] == 0:
            minus = arr[i]
            break
        if N - arr[i] <0:
            minus = arr[i-1]
            break
    count += 1
    N -= minus
print(count)
