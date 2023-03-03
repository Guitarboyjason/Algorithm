n = int(input())
coin_cnt = [100000]*(n+1)
coin_cnt[0] = 0
if n >= 1:
    coin_cnt[1] = 1
if n >= 2:
    coin_cnt[2] = 1
if n >= 3:
    coin_cnt[3] = 2
if n >= 4:
    coin_cnt[4] = 2
if n >= 5:
    coin_cnt[5] = 1
if n >= 6:
    coin_cnt[6] = 2
if n >= 7:
    coin_cnt[7] = 1
if n >= 8:
    for i in range(8,n+1):
        coin_cnt[i] = min(coin_cnt[i-1],coin_cnt[i-2],coin_cnt[i-5],coin_cnt[i-7])+1
print(coin_cnt[n])
