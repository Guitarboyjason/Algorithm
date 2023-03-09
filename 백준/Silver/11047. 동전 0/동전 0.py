N,K = map(int,input().split())

values_coin = [int(input())for _ in range(N)]

coin_count = 0
while K:
    coin_count += K // max([i for i in values_coin if i <= K])
    K %= max([i for i in values_coin if i <= K])
print(coin_count)