N,M = map(int,input().split())
reverse_baskets = [list(map(int,input().split())) for _ in range(M)]

baskets = [i for i in range(N+1)]

for i,j in reverse_baskets:
    baskets[i:j+1] = baskets[j:i-1:-1]
print(*baskets[1:])