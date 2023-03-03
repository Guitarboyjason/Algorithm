def find_min(N):
    arr = []
    if N == 0 :
        return 0
    for i in range(1,N+1):
        if i*i <= N:
            arr.append(N-i*i)
        else:
            break
    for i in arr:
        return 1 + find_min(i)

N = int(input())
print(find_min(N))
