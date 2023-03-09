# 보드 N
# 출발점 1
# 도착점 N
# 지시사항
# 지시 사항으로 이동해서 도착하면 지시를 따르지 않음
# 몇 번 만에 도착하는가
# 그냥 계속 따라가면 안되나?

from collections import deque
N,M = map(int,input().split())
arr_board = [0]+[int(input()) for _ in range(N)]
arr_dice = deque([int(input()) for _ in range(M)])
now = 1
def follow(now,step,cnt):
    cnt += 1
    now += step
    if now > N:
        return cnt
    now += arr_board[now]
    if now >= N:
        return cnt
    else:
        return follow(now,arr_dice.popleft(),cnt)

print(follow(now,arr_dice.popleft(),0))

# print(arr_board)
