def knapsack(capacity,n):
    arr = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for s in range(1,capacity+1):
            if things[i][0] > s:
                arr[i][s] = arr[i-1][s]
            else:
                arr[i][s] = max(things[i][1] + arr[i-1][s-things[i][0]],\
                                arr[i-1][s])
    return arr[n][capacity]

N,K = map(int,input().split())
things = [[0,0]]+[list(map(int,input().split()))for _ in range(N)]
print(knapsack(K,N))