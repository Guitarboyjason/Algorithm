n = int(input())
# # @bottom-up
# arr_cnt = [-1] * (n+1)
# arr_cnt[1] = 1
# if n >= 2:
#     arr_cnt[2] = 3
# if n>= 3:
#     for i in range(3,n+1):
#         arr_cnt[i] = arr_cnt[i-1]+arr_cnt[i-2]*2

# @memoization          #함수 
arr_cnt = [-1] * (n+1)
def find_cnt(n):
    if arr_cnt[n] != -1:
        return arr_cnt[n]
    else:
        arr_cnt[n] = find_cnt(n-1) + 2*find_cnt(n-2)
        return arr_cnt[n]

print(arr_cnt[n] % 10007)
