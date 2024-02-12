"""
N개의 구간
Ai는 i번째 구간에 있는 물체가 지면으로부터 떨어져 있는 높이

배너는 지도에 표현된 N개의 구간중 연속된 M개의 구간
배너가 있는 연속된 M개의 구간에서 [9M/10]개 이상의 Ai의 값이 하나의 값으로 같아야한다

이때, 도로에 배너를 걸 수 있는지 확인하는 프로그램
"""

# 완탐?

# M<=N<=2*10^5

import math
from collections import Counter

N, M = map(int, input().split())
cnt = math.ceil(9 * M / 10)
arr = list(map(int, input().split()))

for i in range(N - M + 1):
    # print(Counter(arr[i : i + M]))
    # print(list(Counter(arr[i : i + M]).values()))
    if len([i for i in Counter(arr[i : i + M]).values() if i >= cnt]):
        print("YES")
        break
else:
    print("NO")
