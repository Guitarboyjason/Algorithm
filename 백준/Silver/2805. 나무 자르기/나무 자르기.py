import sys

input = sys.stdin.readline
N, M = map(int, input().split())

trees = list(map(int, input().split()))

max_tree = max(trees)

start = 0
end = max_tree
n_middle = 0
while start <= end:
    middle = (start + end) // 2
    if sum([i - middle for i in trees if i > middle]) < M:
        end = middle - 1
    else:
        start = middle + 1
        n_middle = middle

print(n_middle)
