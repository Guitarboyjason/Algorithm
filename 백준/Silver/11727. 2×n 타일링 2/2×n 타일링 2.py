n = int(input())
arr_cnt = [-1] * (n+1)
arr_cnt[1] = 1
if n >= 2:
    arr_cnt[2] = 3
if n>= 3:
    for i in range(3,n+1):
        arr_cnt[i] = arr_cnt[i-1]+arr_cnt[i-2]*2

print(arr_cnt[n] % 10007)