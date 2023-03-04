# N = int(input())

# arr = [[]for _ in range(N)]

# for i in range(N):
#     for j in range(5):
#         arr[i].append(input())
# # print(arr)
# similar_1 = -1
# similar_2 = -1    
# min_diff_cnt = 36
# for i in range(N-1):
#     diff_cnt = 0
#     for j in range(i+1,N):
#         for k in range(5):
#             for l in range(7):
#                 if arr[i][k][l] != arr[j][k][l]:
#                     diff_cnt+=1
#         if diff_cnt < min_diff_cnt:
#             min_diff_cnt = diff_cnt
#             similar_1 = i
#             similar_2 = j
               
# print(similar_1+1, similar_2+1) 

N = int(input())
painting = [[list(input())for _ in range(5)] for _ in range(N)]

answer = []
max_simmilar = 0
for i in range(N-1):
    for j in range(i+1,N):
        simmilar = 0
        for row in range(5):
            for column in range(7):
                if painting[i][row][column] == painting[j][row][column]:
                    simmilar += 1
        if simmilar > max_simmilar:
            max_simmilar = simmilar
            answer = [i+1,j+1]

print(*answer)