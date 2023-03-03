import sys
sys.stdin = open("sources/input.txt", "r")

for test_case in range(1, 11):
    cnt = int(input())
    land = list(map(int, input().split()))
    while max(land)-min(land) > 1 and cnt:
        cnt -= 1
        land[land.index(max(land))] -= 1
        land[land.index(min(land))] += 1
    print("#{} {}".format(test_case, max(land)-min(land)))
