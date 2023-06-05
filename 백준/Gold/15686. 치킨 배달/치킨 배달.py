"""
빈칸, 치킨집, 집 중 하나

치킨거리 = 집과 가장 가까운 치킨집 사이의 거리

도시의 치킨거리는 모든 집의 치킨 거리의 합

가장 수익을 많이 낼 수 있는 치킨집의 갯수는 M개

도시의 치킨 거리가 가장 작게 될 수 있는지를 구하는 문제

0 : 빈칸
1 : 집
2 : 치킨집
"""
from itertools import combinations
import sys


input = sys.stdin.readline

N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]

houses = [(i, j) for i in range(N) for j in range(N) if city[i][j] == 1]
chickens = [(i, j) for i in range(N) for j in range(N) if city[i][j] == 2]
# print(houses)
# print(chickens)

min_summary = -1
for chicks in combinations(chickens, M):
    summary = 0
    for h_x, h_y in houses:
        summary += min([abs(h_x - x) + abs(h_y - y) for x, y in chicks])
    if min_summary == -1 or min_summary > summary:
        min_summary = summary

print(min_summary)
