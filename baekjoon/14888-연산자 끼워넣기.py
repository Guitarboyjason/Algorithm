# 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행한다.
# 나눗셈은 정수 나눗셈으로 몫만 취한다.
# 음수를 양수로 나눈때는 양수로 바꾼 뒤 몫을 취하고 그 뒤 음수로 바꾼다.

# N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램



def operators( arr,result,arr_operators): # 결과값을 또 다시 써야한다.
    if result == 1000000000: #처음 실행한다는 뜻
        result = arr_A[0]
        return operators(arr,result,arr_operators)
    else:
        arr_operators

result = 1000000000


N = int(input())
arr_A = list(map(int,input().split()))
arr_operators = list(map(int,input().split()))

# 결국 operators를 어떻게 배치하냐가 관건인데
# 모든 경우의 수를 랜덤하게 다 넣는다면?

for i in range(N-1):
