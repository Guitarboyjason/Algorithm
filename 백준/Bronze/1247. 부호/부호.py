import sys
input = sys.stdin.readline
for _ in range(3):
    answer = sum([int(input()) for _ in range(int(input()))])
    if answer == 0:
        print(0)
    if answer > 0:
        print("+")
    if answer < 0:
        print("-")