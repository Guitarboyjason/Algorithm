def counter(num, n):
    cnt = 0
    while num:
        num //= n
        cnt += num
    return cnt


n, m = map(int, input().split())
cnt_2 = 0
cnt_5 = 0
cnt_2 += counter(n, 2)
cnt_5 += counter(n, 5)
cnt_2 -= counter(m, 2)
cnt_5 -= counter(m, 5)
cnt_2 -= counter(n-m, 2)
cnt_5 -= counter(n-m, 5)
print(min(cnt_2, cnt_5))
# print(min(cnt_comb_2_5(n, m)))
