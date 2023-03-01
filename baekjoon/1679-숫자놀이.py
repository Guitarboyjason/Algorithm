from itertools import combinations

N = int(input())

num_list = list(map(int,input().split()))

K = int(input())

num_list *= K
# print(num_list)

possible_list = set()

for i in range(1,K+1):
    for j in combinations(num_list,i):
        possible_list.add(sum(j))
# print(set(possible_list))
possible_list = set(possible_list)

for i in range(1,num_list[-1]*K+1):
    if i not in possible_list:
        if i % 2 == 0:
            winner = "holsoon"
        else:
            winner = "jjaksoon"
        win_num = i
        break

print(winner+" win at "+str(win_num))