
#에라토스테네스의 체 에서 2,3,5,7, 등등 해당 되는 소수들을 이미 걸러
#내고 나면 그 배수들은 다 이미 확인 했기 때문에 와 그러네

max_num = 10001
prime_num = [True] * (max_num)
prime_num[1] = [False]
for i in range(2,int(max_num**0.5)):
    if prime_num[i] is True:
        for j in range(i*2,len(prime_num),i):
            prime_num[j] = False

T = int(input())
for _ in range(T):
    n = int(input())
    for i in range(n//2,1,-1):
        if prime_num[i] is True and prime_num[n-i] is\
        True:
            print(i, n-i)
            break
