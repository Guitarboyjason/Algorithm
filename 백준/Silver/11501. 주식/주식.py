"""
이후 최고점보다 낮은 가격들에 대해 사모으고
최고점에서 판다.
"""
import sys

input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    price = list(map(int, input().split()))
    max_list = []
    maximum = -1
    for i in range(N - 1, -1, -1):
        if price[i] > maximum:
            maximum = price[i]
        max_list.append(maximum)
    max_list.reverse()
    stocks = 0
    money = 0
    for i in range(N - 1):
        # if price[i] > price[i + 1]:
        if price[i] < max_list[i]:
            money -= price[i]
            stocks += 1
            # tmp_money = 0
        else:
            money += stocks * price[i]
            stocks = 0
    money += stocks * price[-1]
    print(money)
