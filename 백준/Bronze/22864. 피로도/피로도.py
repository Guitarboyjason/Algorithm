A, B, C, M = map(int, input().split())
time_count = 24
work = 0
hard = 0
while time_count:
    if hard + A > M:
        hard -= C
        if hard < 0:
            hard = 0
    else:
        hard += A
        work += B
    time_count -= 1
print(work)
