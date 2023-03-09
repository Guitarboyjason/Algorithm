# 검정 칸과 하얀 칸이 번갈아가며 색칠되어 있다.
# 가장 왼쪽 위 칸 (0,0)은 하얀색이다.
# 체스판의 상태가 주어졌을 때, 하얀 칸 위에 말이 몇 개 있는지 출력하라.

board= list(input()for _ in range(8))
cnt = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            if board[i][j] == "F":
                cnt += 1
print(cnt)
