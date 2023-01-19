# 최소 공배수는 최대 공약수 * (num1)/최대공약수 *(num2)/최대공약수
# 로 볼 수 있다 그러므로 (num1) * (num2)/최대공약수
# 와 같게 된다.

def euclid(r1,r2):
    while r2:
        r1,r2 = r2,r1%r2
    return r1

def solution(arr):
    answer = 1
    for i in arr:
        answer = answer * i //euclid(answer,i)
    return answer

print(solution([1,2,3]))
