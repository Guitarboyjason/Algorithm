# 2만 * 2만은 시간 초과가 나올 것 같음. sorting을 해서?
# index를 저장해두고 그 이후부터 확인하면 될 것 같음.
import sys
input = sys.stdin.readline
for T in range(int(input())):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()
    idx = 0
    summary = 0
    for a_num in A:
        while B[idx]<a_num:
            if idx != M-1:
                idx += 1
            else:
                summary += (idx+1)
                break
        else:
            summary += idx
    print(summary)