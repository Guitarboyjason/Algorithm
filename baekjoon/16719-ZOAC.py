# 길이별로 하나씩, 사전순으로 정렬해서 가장 앞에 있는 걸 뽑으면 되나?
# 근데 순서별로 확인해주려면,,,? 어떡하지?
# 뭔가 "","",A,"" 이런식으로 진행하면 좋을것 같은데,,,

# from itertools import combinations
from copy import deepcopy
import sys
input = sys.stdin.readline

word = list(input().rstrip())
# 넣은건 빼버릴까
check = [False for _ in range(len(word))]
best_word = [""for _ in range(len(word))]
maybe_best = ["Z"for _ in range(len(word))]

for i in range(len(word)):
    tmp = deepcopy(best_word)
    maybe_best = ["Z"for _ in range(len(word))] # 초기화를 매번 시켜야 할 듯
    for idx,c in enumerate(word):
        ttmp = deepcopy(tmp)
        if check[idx] == False:
            ttmp[idx] = c
            compare = ["".join(ttmp),"".join(maybe_best)]
            # print(compare)
            if compare == sorted(compare):
                # print(tmp)
                maybe_best = deepcopy(ttmp)
    # 다 돌고 나면 maybe_best가 update되어있겠지?
    # print(maybe_best)
    changed = -1
    for idx,i in enumerate(maybe_best):
        if best_word[idx] != i:
            changed = idx
            break
    check[changed] = True
    best_word = maybe_best
    print("".join(best_word))