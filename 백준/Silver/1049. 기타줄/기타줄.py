
# 낱개 가격이 가장 싼게 묶음으로 산 어떤것 보다도 싼 경우
# 낱개 가격 * N
# 아니면 묶음으로 몇개 사고 어떤게 더 싼지 비교하면 될 듯


N, M = map(int, input().split())

price = [list(map(int, input().split()))for _ in range(M)]

summary = 0

minimum_one = min(price, key=lambda x: x[1])[1]
minimum_multy = min(price, key=lambda x: x[0])[0]

if minimum_one * 6 <= minimum_multy:
    summary += minimum_one * N
else:
    summary += minimum_multy * (N//6)
    if minimum_multy <= N % 6 * minimum_one:
        summary += minimum_multy
    else:
        summary += N % 6 * minimum_one
print(summary)
