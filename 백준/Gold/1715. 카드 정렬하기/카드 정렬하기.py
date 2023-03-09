import sys, heapq
input = sys.stdin.readline

cards = list(int(input()) for _ in range(int(input())))

summary = 0
heapq.heapify(cards)
while cards:
    if len(cards) != 1:
        min_card = heapq.heappop(cards)
        second_min_card = heapq.heappop(cards)

        summary += min_card + second_min_card
        heapq.heappush(cards,min_card + second_min_card)
    else:
        break
print(summary)
