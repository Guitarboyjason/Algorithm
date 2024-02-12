# 2보다 큰 짝수는 두 소수의 합으로 나타낼 수 있다.

# 짝수 N이 주어졌을 때, 골드바흐 파티션의 갯수를 구해보자

# 두 소수의 순서만 다른 것은 같은 파티션이다.

import sys
input = sys.stdin.readline


MAX_NUM = 1_000_000
primes = [True for i in range(MAX_NUM+1)]
primes[0] = False
primes[1] = False

prime_list = []

for i in range(2,MAX_NUM+1):
    if primes[i]:
        prime_list.append(i)
        for j in range(i,MAX_NUM+1,i):
            primes[j] = False

# print(prime_list[:20])
# 투포인터로 확인해야하나?
# print(primes[:10])


# print(prime_list[:10])
T = int(input())

for t in range(T):
    N = int(input())
    
    cnt = 0
    
    p1 = 0
    p2 = N if N < len(prime_list) else len(prime_list) - 1
    # print(p2)
    while p1 <= p2:
        summary = prime_list[p1] + prime_list[p2]
        if summary == N:
            cnt +=1
            p1 += 1
        elif summary < N:
            p1 += 1
        else:
            p2 -= 1
    print(cnt)