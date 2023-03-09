for test_case in range(int(input())):
    N = int(input())
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            cnt = 0
            while N % i == 0:
                N //= i
                cnt += 1
            print("{} {}".format(i, cnt))
    if N > 1:
        print("{} {}".format(N, 1))
