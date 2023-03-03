#분해합이란 N과 N을 이루는 각 자리수의 합
#M의 분해합이 N인 경우 M을 N의 생성자라 함
#자연수 N이 주어졌을 때 N의 가장 작은 생성자를 구하라

def find_sum(N):
    for i in range(1,N+1):
        M = i
        tmp = i
        for _ in range(len(str(N))):
            M += tmp % 10
            tmp = tmp // 10
        if M == N:
            return i
    return 0
N = int(input())
print(find_sum(N))
