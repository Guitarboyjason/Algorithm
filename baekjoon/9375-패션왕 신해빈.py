import sys
import itertools
input = sys.stdin.readline
test_case = int(input())
for _ in range(test_case):
    n = int(input())
    if n == 0:
        print(0)
        continue
    dic = {}
    for _ in range(n):
        clothes = list(input().split())
        if clothes[1] in dic:
            dic[clothes[1]] += 1
        else:
            dic[clothes[1]] = 1
    # for i in range(1,len(dic)+1):
    #     for j in list(itertools.combinations(dic,i)):
    #         mult = 1
    #         for k in j:
    #             mult *= dic[k]
    #         count += mult
    mult = 1
    for i in (dic):
        mult *= (dic[i]+1)
    print(mult-1)
