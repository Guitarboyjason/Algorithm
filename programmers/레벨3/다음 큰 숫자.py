#조건 1 n의 다음 큰 숫자는 n보다 큰 자연수
# n의 다음 큰 숫자와 n은 2진수로 변환했을 때 1의 갯수가 같다
# n의 다음 큰 숫자는 1 2 를 만족하는 숫자들 중 가장 작은 수

def solution(n):
    for i in range(n+2,n*n):
        if format(n,'#b').count('1') == format(i,'#b').count('1'):
            return i


print(solution(15))
