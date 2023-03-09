def gcd(a,b):
    for i in range(a,0,-1):
        if a%i == 0 and b % i == 0:
            return i

t = int(input())
for _ in range(t):
    ask = list(map(int,input().split()))
    ask = ask[1:]
    summary = 0
    for index_i,i in enumerate(ask):
        for index_j,j in enumerate(ask):
            if index_i < index_j:
                summary += gcd(i,j)
    print(summary)
