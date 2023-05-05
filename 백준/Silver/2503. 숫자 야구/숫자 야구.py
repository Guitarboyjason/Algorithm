from itertools import permutations
N = int(input())
poss_list = list(permutations([i for i in range(1,10)],3))
answer = set(permutations([i for i in range(1,10)],3))
# print(len(answer))
for _ in range(N):
    num,s,b = map(int,input().split())
    num = list(map(int,list(str(num))))
    
    can_list = set()
    
    for i in range(len(poss_list)):
        pos = poss_list[i]
        check_s = 0
        check_b = 0
        for j in range(3):
            if pos[j] == num[j]:
                check_s += 1
            elif num[j] in pos:
                check_b += 1
        if check_s == s and check_b == b:
            can_list.add(pos)
    answer = answer.intersection(can_list)
# answer.intersection((1,3,7))
# print(answer)
print(len(answer))