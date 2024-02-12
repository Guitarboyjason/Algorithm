# N,S = map(int,input().split())
# permutation_list = list(map(int,input().split()))

# cnt = 0
# for i in range(N-1):
#     for j in range(i+1,N):
#         if sum(permutation_list[i:j+1]) == S:
#             cnt += 1
# print(cnt)

# N,S = map(int,input().split())
# per_list = list(map(int,input().split()))
# available_list =[[True],[False]]

# def make_index_list(N):
#     for _ in range(N-1):
#         tmp = available_list.copy()
#         for idx_list in tmp:
#             available_list.extend([idx_list + [True],idx_list+[False]])

#     return [i for i in available_list if len(i) == N]
# available_list = make_index_list(N)

# cnt = 0
# for idx_list in available_list:
#     if idx_list.count(True) != 0: ## 수열의 갯수가 양수
#         if sum([i[0] for i in zip(per_list,idx_list) if i[1] == True]) == S:
#             cnt += 1
# print(cnt)

N,S = map(int,input().split())
arr = list(map(int,input().split()))

summary_arr = [0]
for i in arr:
    tmp = summary_arr.copy()
    for j in tmp:
        summary_arr.append(j+i)
print(summary_arr[1:].count(S))