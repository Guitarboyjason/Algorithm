import sys

sys.setrecursionlimit(10**6)
# 다이나믹 프로그래밍으로 짜도 될 것 같고..

fibo = [-1] * 100001
fibo[0] = 0
fibo[1] = 1
def fibonacchi(n):
    if fibo[n] != -1:
        return fibo[n]
    # -1 일 땐 아직 저장이 안된 부분이라는 뜻
    fibo[n] =  fibonacchi(n-1) + fibonacchi(n-2)
    return fibo[n]

def solution(n):
    answer = fibonacchi(n)%1234567

    return answer

print(solution(5))
