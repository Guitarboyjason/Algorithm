import sys
from itertools import combinations

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
K = int(input())

nums_extend = [i for i in nums for _ in range(K)]
# print(nums_extend)
poss_nums = []
# for i in range(1, K + 1):
#     poss_nums.extend(list(combinations(nums_extend, i)))
# limit = set([sum(i) for i in poss_nums])
for i in range(1, K + 1):
    poss_nums.append(combinations(nums_extend, i))
limit = set()
for poss in poss_nums:
    for i in poss:
        limit.add(sum(i))
print(limit)
for i in range(1, K * nums[-1] + 2):
    if i not in limit:
        if i % 2 == 0:
            print(f"holsoon win at {i}")
        else:
            print(f"jjaksoon win at {i}")
        break
