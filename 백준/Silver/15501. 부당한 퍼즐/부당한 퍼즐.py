n = int(input())

arr = list(map(int,input().split()))
# arr = input()
goal = list(map(int,input().split()))
# goal = input()

arr_compare = arr.index(1)
goal_compare = goal.index(1)
direction = 0

if arr_compare + 1 < n-1 and goal_compare + 1 < n-1 and arr[arr_compare+1] == goal[goal_compare+1]:
    direction = 1
else:
    direction = -1
flag = True
for i in range(1,n):
    arr_compare += 1
    goal_compare += direction
    arr_compare %= n
    goal_compare %= n
    if arr[arr_compare] == goal[goal_compare]:
        pass
    else:
        flag = False
        break

if not flag:
    print("bad puzzle")
else:
    print("good puzzle")


# 1 2 3 4 5 -> 5 1 2 3 4 -> 4 3 2 1 5 -> 3 2 1 5 4
# 하나 혹은 두개의 내림(오름)차순이 아니라 바뀐 결과가 그렇다 라는 말인가

# 원래 순서나 뒤집었을 때, 연속되어 겹치는 걸 없애고 한번 더 없앴을 때 완전히 없어지는가

# 수의 범위가 1_000_000 이므로 나누는 구간을 이분탐색으로 확인하는게 정신건강에 좋을듯

# start = 0
# end = len(arr)

# saved_index = -1
# while start < end:
#     middle = (start+end) // 2
#     print(arr[:middle], arr[-1:middle:-1])
#     if arr[:middle] in goal or arr[-1:middle:-1] in goal:
#         saved_index = middle
#         start = middle + 1
#     else:
#         end = middle
        
# print(saved_index)
#     # if arr[:middle:-1] in goal:
        