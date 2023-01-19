TC = int(input())

for test_case in range(1,TC+1):
    N = input()
    count = len(N)
    tmp = N[:3]
    print(tmp)
    tmp = int(tmp) / 10
    tmp = round(tmp)
    if len(str(tmp)) > 2:
        count += 1
        tmp /= 10
    tmp /= 10
    count -= 1
    print(f"#{test_case} {tmp}*10^{count}")
