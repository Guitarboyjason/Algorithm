# # i는 j보다 작다.
#
#
# n = int(input())
# arr = list(map(int,input().split()))
# x = int(input())
#
# cnt = 0
# for i in range(n-1):
#     for j in range(i+1,n):
#         if arr[j] + arr[i] == x:
#             cnt += 1
#
# print(cnt)
#
# # 10 9 8 7 6 5 4 3 2 1
# # 10만 ~ 1까지 더하는데
# # 100001 * 50000
# # 5000050000
# # 무조건 안될 것 같은데..
# # --- 안되네 ---

n = int(input())
arr = list(map(int,input().split()))
x = int(input())

# arr.sort(reverse=True)

# cnt = 0
# index_start = 0
# index_end = 0
#
# while index_end != n:
#     if index_start != index_end:
#         while arr[index_start] + arr[index_end] > x:
#             if index_start == index_end-1:
#                 break
#             index_start += 1
#         if arr[index_start] + arr[index_end] == x:
#             cnt += 1
#     index_end += 1
# print(cnt)

arr.sort()
cnt = 0
index_start = 0
index_end = 1



while index_end != n:
    if index_start != index_end:
        while arr[index_start] + arr[index_end] < x:
            if index_start == index_end-1:
                break
            index_start += 1
        while arr[index_start] + arr[index_end] > x:
            if index_start == 0:
                break
            index_start -= 1
        if arr[index_start] + arr[index_end] == x:
            cnt += 1
    index_end += 1
print(cnt)
# arr.sort(reverse=True)
# for i in range(n-1):
#     for j in range(i+1,n):
#         if arr[i] + arr[j] == x:
#             cnt += 1
#         elif arr[i] + arr[j] < x:
#             break
# print(cnt)
