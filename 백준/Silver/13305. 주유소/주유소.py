import sys 
input = sys.stdin.readline
sys.setrecursionlimit = 10**6
# 가장 기름 값이 싼 곳에서 끝까지 갈 수 있는 양만큼 주유한다

# 그 전까지는 그 전의 도시 중 주유 가격이 가장 싼 곳에서

# 이걸 반복하다 보면 될 것 같다.

N = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))


def greedy(length, price):
    if price[0] == min(price):
        return sum(length) * price[0]

    return min(price) * sum(length[price.index(min(price)):]) + greedy(length[:price.index(min(price))], price[:price.index(min(price))])


print(greedy(length, price))
