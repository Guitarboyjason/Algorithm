N = int(input())
painting = [[list(input())for _ in range(5)] for _ in range(N)]

answer = []
max_simmilar = -1
for i in range(N-1):
    for j in range(i+1,N):
        simmilar = 0
        for row in range(5):
            for column in range(7):
                if painting[i][row][column] == painting[j][row][column]:
                    simmilar += 1
        if simmilar > max_simmilar:
            max_simmilar = simmilar
            answer = [i+1,j+1]

print(*answer)