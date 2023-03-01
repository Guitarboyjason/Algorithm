N,M = map(int,input().split())
baskets = [i for i in range(N+1)]

for _ in range(M):
    i,j,k = map(int,input().split())
    baskets[i:j+1] = baskets[k:j+1]+baskets[i:k]
    
print(*baskets[1:])