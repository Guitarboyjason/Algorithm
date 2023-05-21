import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    trees = list(map(int, input().split()))
    trees.sort()
    odds = [i for idx, i in enumerate(trees) if idx % 2 == 1]
    evens = [i for idx, i in enumerate(trees) if idx % 2 == 0]
    odds.reverse()
    trees = evens + odds + [trees[0]]
    # print(trees)
    maximum = -1
    for i in range(len(trees) - 1):
        if abs(trees[i] - trees[i + 1]) > maximum:
            maximum = abs(trees[i] - trees[i + 1])
    print(maximum)
