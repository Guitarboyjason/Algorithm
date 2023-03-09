
# 정해진 총액 이하에서 가능한 한 최대의 총 예산을 배정한다.
# 1. 모든 요청이 배정될 수 있는 경우에는 요청한 금액을 그대로 배정한다.
# 2. 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산요청에는
# 모두 상한액을 배정한다

# 결국 상한선을 정하라는 말이구나

import math

N = int(input())
requests = list(map(int,input().split()))
M = int(input())

if M >= sum(requests):
    print(max(requests))
else:
    start = 1
    end = 100000
    while start <=end:
        middle = (start+end)//2
        if middle > M:
            end = middle-1
        else:
            summary = 0
            for i in requests :
                if i > middle:
                    summary += middle
                else:
                    summary += i
            if summary > M:
                end = middle -1
            else:
                start = middle +1
    print(end)

