# 0 0 0 0 0
#

T = int(input())
for testcase in range(1,T+1):
    N,D =map(int,input().split())
    tmp = 1 + 2*D
    if N % tmp == 0:
        print(f"#{testcase} {N // tmp}")
    else:
        print(f"#{testcase} {N // tmp+1}")
