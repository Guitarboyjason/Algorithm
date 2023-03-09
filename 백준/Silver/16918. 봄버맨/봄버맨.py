# 일부 칸에 폭탄을 설치한다.
# 모든 폭탄이 설치된 시간은 같다
# 1초간 아무것도 하지 않는다

# 1초동안 설치되지 않은 모든칸에 폭탄을 설치한다.
# 1초가 지난 후에 3초 전에 설치된 폭탄이 모두 폭발한다.
# 3과 4를 반복한다.

R,C,N = map(int,input().split())
bomb = [input() for _ in range(R)]

dx = [-1,0,0,1,0]
dy = [0,-1,1,0,0]
# def bombomb(time,bomb):
#     if time == N -1 :
#         return bomb
#     if time == 0:
#         return bombomb(time+1,bomb)
#     else:
#         newbomb = ["0"*C for _ in range(R)]
#         if time + 1 != N - 1:
#             for x in range(R):
#                 for y in range(C):
#                     if bomb[x][y] == '0':
#                         for i in range(5):
#                             nx = dx + x
#                             ny = dy + y
#                             if nx >= 0 and nx < R and ny >= 0 and ny < C:
#                                 newbomb[nx] = newbomb[nx][:ny] + '.' + newbomb[nx][ny+1:]
#             return bombomb(time+2,newbomb)
#         else:
#             return newbomb
def bombomb(time,bomb):
    newbomb = ["O"*C for _ in range(R)]

    bombcase3 =newbomb.copy()
    dx = [0,-1,0,0,1]
    dy = [0,0,-1,1,0]
    for x in range(R):
        for y in range(C):
            if bomb[x][y] == 'O':
                for i in range(5):
                    nx = dx[i] + x
                    ny = dy[i] + y
                    if nx >= 0 and nx < R and ny >= 0 and ny < C:
                        bombcase3[nx] = bombcase3[nx][:ny] + '.' + bombcase3[nx][ny+1:]
    bombcase5 = newbomb.copy()
    for x in range(R):
        for y in range(C):
            if bombcase3[x][y] == 'O':
                for i in range(5):
                    nx = dx[i] + x
                    ny = dy[i] + y
                    if nx >= 0 and nx < R and ny >= 0 and ny < C:
                        bombcase5[nx] = bombcase5[nx][:ny] + '.' + bombcase5[nx][ny+1:]
    if time == 1:
        return bomb
    elif N % 2 == 0:
        return newbomb
    elif N>1 and N % 4 == 1:
        return bombcase5
    elif N %4 == 3:
        return bombcase3
result = bombomb(N,bomb)
for i in result:
    print(i)

