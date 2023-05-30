'''
n장의 카드
1. x + y
2. x 와 y에 덮어씌운다
m번 진행
모든 카드의 합이 가장 작게
1 + 2 -> 3 3
0 + 3 -> 3 3
3 + 4 -> 7 7
작은 수들을 계속해서 합쳐야 하는 거겠지?
'''

# n <= 1000, m <= 15 * n
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
cards = list(map(int,input().split()))

for i in range(m):
    cards.sort()
    cards[0],cards[1] = cards[0]+cards[1],cards[0]+cards[1]

print(sum(cards))