def find_min_paint(chess, N, M):
    cnt = 0
    for i in range(N,N+8):
        for j in range(M , M+8):
            if chess[i][j] == 'P':
                cnt += 1
    return min(cnt, 64-cnt)

N,M = map(int,input().split())
chess = ['0'*(M+1)]
for _ in range(N):
    chess.append('0'+input())
# print('\n'.join(chess))

for i in range(1,N+1):
    for j in range(1,M+1):
        if (i+j) %2 == 0 and chess[i][j] == 'W':
            chess[i] = chess[i][:j]+'P'+chess[i][j+1:]
        elif (i+j) % 2 == 1 and chess[i][j] == 'B':
            chess[i] = chess[i][:j]+'P'+chess[i][j+1:]
min = 64

for i in range(N-8):
    for j in range(M-8):
        tmp = find_min_paint(chess,i,j)
        if tmp < min:
            min = tmp
print(min)

