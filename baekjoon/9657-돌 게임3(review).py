# 1 --> sk
# 2 --> cy
# 3 -- sk
# 4 -- sk
# 5 -- sk ( 3 - 1 - 1)
# 6 -- sk ( 4 - 1 - 1)
# 7 -- cy (1 - 4 - 1 - 1)
# 8 -- sk (1 1 4 1 1)
# 9 --


N = int(input())
# # @bottom-up
# def find_winner(N):
#     win_arr = ['']*(N+1)
#     win_arr[1] = 'SK'
#     if N >= 3:
#         win_arr[3] = 'SK'
#     if N >= 2:
#         win_arr[2] = 'CY'
#     if N >= 4:
#         win_arr[4] = 'SK'
#     if N >= 5:
#         for i in range(5,N+1):
#             if win_arr[i-1] == 'CY' or win_arr[i-3] == 'CY' or \
#                     win_arr[i-4] == 'CY':
#                 win_arr[i] = 'SK'
#             else:
#                 win_arr[i] = 'CY'
#     print(win_arr[N])

# @memoization
arr_winner = [''] * (N+1)
arr_winner[1] = 'SK'
if N >= 2:
    arr_winner[2] = 'CY'
if N >= 3:
    arr_winner[3] = 'SK'
if N >= 4:
    arr_winner[4] = 'SK'
def find_winner(N):
    if arr_winner[N] != '':
        return arr_winner[N]
    else:
        if find_winner(N-1) == 'CY' or find_winner(N-3) == 'CY' or find_winner(N-4) == 'CY':
            arr_winner[N] = 'SK'
            return 'SK'
        else:
            arr_winner[N] = 'CY'
            return 'CY'

# find_winner(N)
print(find_winner(N))
