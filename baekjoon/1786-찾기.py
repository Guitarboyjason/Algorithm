T = input()
P = input()
# print(T.count(P))
cnt = 0
T_start_index = 0
P_end_index = 0
p_k_list = [i for i in range(len(P))]
# for i in range(1,len(P)):
#     tmp = -1
#     for j in range(i):
#         if P[j] == P[i]:
#             tmp = j#이러면 안되는데,,

while T_start_index+len(P) <= len(T):
    