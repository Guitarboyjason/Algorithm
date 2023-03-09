# 4보다 큰 모든 짝수는 두 홀수 소수의 합으로 나타낼 수 있다.
# 백만 이하의 모든 짝수에 대해서, 검증하라.
import sys
input = sys.stdin.readline
max_num = 1000000
prime_list = [-1,-1] + [i for i in range(2,max_num+1)]
def prime_num_list():
    for i in range(2,max_num//2 + 1):
        if prime_list[i] != -1:
            tmp = i
            for j in range(2,max_num//i+1):
                if prime_list[i*j] != -1:
                    prime_list[i*j] = -1
prime_num_list()
n = int(input())
while n != 0:
    for i in prime_list:
        if i != -1:
            if prime_list[n-i] != -1:
                print("{} = {} + {}".format(n,i,n-i))
                break
    n = int(input())
