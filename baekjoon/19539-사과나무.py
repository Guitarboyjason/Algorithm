
# ## 일단 모든 수를 다 더했을 때 3의 배수가 나와야함.
# ## 그럼에도 불구하고 나오지 못하는 경우가 발생할 수 있다.
# ## 3보다 큰 나무들은 3으로 나누고...? 이럼 안됨
# ## 1 3 1 3 1 은 나올수가 없는데 어떤 규칙일까

# ## 다 더하면 9. 총 세번을 물을 준다는건데
# ## 그럼 각 1에 1을 줘야하니까
# ## 나머지 3 3 에 2씩 안나눠진다.

# ## 4 6 4 6 4 는 어떨까, 당연히 3의 배수.
# ## 24 로 총 8번을 물주는건데
# ## 가능한 경우의 수 (1,2) or (3)으로 2**8?
# ## 사실 순서는 상관 없으니까

# # N <= 100_000, 각 h <= 10_000인데

# # 직접 뿌려댈 순 없음
# # 100 10 1
# # 100 8 0
# # 99 6 0

# # 모든 나무가 3의 배수일땐 무조건 가능함.


# # 9900 900 0

# # 적당히 1 이랑 2로 빼고 나면도 같은 결과?

# ## 1이 필요한 갯수로 볼까..

# ## 반대로 2가 필요한 갯수를 본다면?

# ## 똑같지 1이 필요하면 어디선간 2가 필요하니까

# N = int(input())
# tree_heights = list(map(int,input().split()))

# if sum(tree_heights)%3:
#     print("NO")
# else:
#     tmp = sum(tree_heights)
#     cnt_3 = 0
#     while tmp:
#         tmp //= 3
#         cnt_3 += 1
    
#     # tmp = sum(tree_heights)
#     cnt_1 = 0
#     cnt_2 = 0
#     for height in tree_heights:
#         while height > 2:
#             height //= 3
#         if height == 1:
#             cnt_1 += 1
#         elif height == 2:
#             cnt_2 += 1
            
#     if cnt_1 > cnt_2 and (cnt_1-cnt_2)%3 != 0:
#         print("NO")
#     else:
#         if (cnt_2 - cnt_1) % 3 == 0:
#             print("YES")
#         else:
#             print("NO")
# import heapq
N = int(input())
heights = list(map(int,input().split()))

if sum(heights)% 3 != 0:
    print("NO")
else:
    cnt_2 = 0
    for height in heights:
        if height >= 2:
            cnt_2 += height//2
            
    if cnt_2 < sum(heights)//3:
        print("NO")
    else:
        print("YES")


# heapq.heapify(hq)
# while 

# while len(hq) > 1 :
#     while hq and hq[0] % 3 == 0:
#         heapq.heappop(hq)


