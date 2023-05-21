import sys

input = sys.stdin.readline

N = int(input())
houses = list(map(int, input().split()))
houses.sort()
if len(houses) % 2 == 1:
    print(houses[len(houses) // 2])
else:
    print(houses[len(houses) // 2 - 1])
