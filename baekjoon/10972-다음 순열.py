# # N = int(input())
# # arr = list(map(int,input().split()))
# # def solution(arr):
# #     for i in range(N-1,0,-1):
# #         if arr[i] > arr[i-1]:
# #             arr[i],arr[i-1] = arr[i-1],arr[i]
# #             arr = arr[:i] + sorted(arr[i:])
# #             break
# #     else:
# #         return -1
# #     return arr

# # print(solution(arr))

# from itertools import permutations

# N = int(input())
# arr = [i+1 for i in range(N)]
# perm_list = list(permutations(arr,N))
# try:
#     print(perm_list[perm_list.index(list(map(int,input().split())))+1])
# except:
#     print(-1)
        
        
N = int(input())
arr= list(map(int,input().split()))

for i in range(N-1,0,-1):
    if 