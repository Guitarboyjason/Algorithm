"""
N의 범위가 200,000
가능한 수의 범위는 100,000
그럼 이건 무조건 이분탐색으로 풀어야 할 것임
"""

import sys

input = sys.stdin.readline

N = int(input())
houses = list(map(int, input().split()))
houses.sort()
# 딱 하나를 설치, 집들간에 거리가 가장 작은 것
# 같은 결과가 여러개가 나오면 가장 작은 수
# 아.. 그냥 왼쪽 오른쪽 수의 갯수를 맞추면 되겠네
# 짝수인 경우에는 당연히 왼쪽으로 가나 오른쪽으로 가나 상쇄될 것이고
# 홀수면 다른 문젠데 이건 아마 큰 차이가 없을 거니까 5개라면 2번째 정도에 세우면 될 듯
# 아 그냥 3번째의 위치에 세우면 되겠네 ㅇㅋ

if len(houses) % 2 == 1:
    print(houses[len(houses) // 2])
else:
    print(houses[len(houses) // 2 - 1])
