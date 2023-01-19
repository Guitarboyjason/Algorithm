import math

#몇 라운드에서 붙을 수 있는지 확인해본다

def solution(n,a,b):
    tmp = int(math.log(n,2))
    print(tmp)

    cnt = 0
    while n:
        if a <= n // 2 and b > n // 2 or a > n // 2 and b <= n // 2:
            return tmp-cnt
        if a > n//2:
            a -= n//2
            b -= n//2
        n = n// 2
        cnt += 1

