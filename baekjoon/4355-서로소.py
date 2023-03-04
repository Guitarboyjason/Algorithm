#p가 소수인 경우 -> p-1
#소수 p의 거듭제곱인 경우 p^(k-1)*(p-1)
#n과 m이 서로소인 경우 n * m

import sys
import math
input = sys.stdin.readline

prime_num = [i for i in range(int((10**9)**0.5)+1)]
prime_list = []
prime_num[0],prime_num[1] = False,False
for i in prime_num:
    if i != False:
        prime_list.append(i)
        for j in range(i*2,len(prime_num),i):
            prime_num[j] = False


n = int(input())
while n:
    if n == 1:
        print(0)
        n = int(input())
        continue
    tmp = 1
    while n>1:
        for p in prime_list:
            if p > n:
                break
            if n % p == 0:
                n //= p
                tmp *= (p-1)
                while n > 1 and n % p == 0:
                    tmp *= p
                    n //= p
    print(tmp)
    n = int(input())