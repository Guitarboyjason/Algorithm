# N = int(input())
dp = [0 for _ in range(100_001)]

for N in range(1, 100_001):
    compare = []
    dp[0] = 1
    dp[1] = 3
    for i in range(2, N + 1):
        dp[i] = (dp[i - 2] + dp[i - 1] * 2) % 9901
    compare.append(dp[N])

    A, B = 1, 3
    for i in range(N - 1):
        A, B = B, (2 * B + A) % 9901
    compare.append(B)
    # print(B)
    if compare[0] != compare[1]:
        print("!!")
