# 1차원 배열을 생성함. 한 행에서 어떤 위치에 들어도 되는지를 검사
import sys
input = sys.stdin.readline

def put_queen(x):
    global cnt
    if x == N:  # 마지막에는 무조건 하나가 가능
        cnt += 1
        return
    else:
        for i in range(N):
            row[x] = i
            if can_put_queen(x):  # 놓을 수 있는 위치일때
                put_queen(x+1)


def can_put_queen(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
            return False
    return True


N = int(input())
cnt = 0
row = [0] * N

put_queen(0)
print(cnt)
