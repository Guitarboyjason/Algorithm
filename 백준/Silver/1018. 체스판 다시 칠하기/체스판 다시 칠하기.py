# 체스판을 칠하는 최소값을 구하기 위해서는 브루트포스로 진행을 한번 해보자
# 그럼 50 * 50이 제일 큰데
# 43 * 43 개의 경우의 수가 생기게 된다.
# 그리고 모든 경우의 수에 모든 패턴을 파악해야한다.
# 그게 8*8을 다 확인하는건데
# 그럼 43*43*8*8이 됨.
# 그래봐야 118,336 개 정도라 다 갖다 넣어도 될 것 같음


N,M = map(int,input().split())
board = [input()for _ in range(N)]
cnt_list = list()

for i in range(M-8+1):
    # collumn = [i,i+7]
    collumn = [k for k in range(i,i+8)]
    white = True
    for j in range(N-8+1):
        row = [k for k in range(j,j+8)]
        cnt = 0
        for r in row:
            for c in collumn:
                if board[r][c] =="W" and not white or \
                        board[r][c] == "B" and white:
                    cnt += 1
                white = not white
            white = not white
        if cnt >64//2:
            cnt = 64-cnt
        cnt_list.append(cnt)
print(min(cnt_list))



