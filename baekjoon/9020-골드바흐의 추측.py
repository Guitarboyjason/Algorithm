#1보다 큰 자연수중 1과 자기 자신을 제외한 약수가 없는 자연수 : 소수
#2보다 큰 모든 짝수는 두 소수의 합으로 나타낼 수 있다.
#가능한 n의 골드바흐 파티션이 여러 가지인 경우에는 두 소수의 차이가
#가장 작은 것을 출력

#일단 테라토스테네스의 체? 로 소수를 걸러내야 할 듯

#줄일 수 있는 오버헤드 :
# 1. 이중 for 문을 줄여야 할 듯

prime_arr = [i for i in range(10001)]
for i in range(2,len(prime_arr)//2):
    if prime_arr[i] != -1:
        for j in range(i*2,len(prime_arr),i):
            prime_arr[j] = -1
prime_arr[0] = -1
prime_arr[1] = -1

T = int(input())
for _ in range(T):
    n = int(input())


    #n을 절반을 나눠서 하나씩 줄여가며 소수인지 확인하고 소수일때
    #뺀 수도 소수면 출력하면 될 것.
    for i in range(n//2,1,-1):
        if i in prime_arr and n-i in prime_arr:
            print(i ,(n-i))
            break

