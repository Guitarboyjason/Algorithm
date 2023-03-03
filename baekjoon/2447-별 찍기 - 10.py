#N은 3의 거듭제곱
#N이 3보다 클 경우 공백으로 채워진 가운데의 (N/3)x(N/3) 정사각형을
#크기 N/3의 패턴으로 둘러싼 형태이다.

#***
#* *
#***

def print_stars(N):
    DIV3 = N//3
    if N == 3:
        g[1] = ['*',' ','*']
        g[0][:3] = g[2][:3] = ['*']*3
        return

    print_stars(DIV3)

    for i in range(0,N,DIV3):
        for j in range(0,N,DIV3):
            if i != DIV3 or j != DIV3:
                for k in range(DIV3):
                    g[i+k][j:j+DIV3] = g[k][:DIV3]

    # else:
    #     return(print_stars(N/3)*3)
    #     print(print_stars(N/3)*3)
    #     print(print_stars(N/3)*3)
    #     print(print_stars(N/3)*3)


N = int(input())
g = [[' ' for _ in range(N)] for _ in range(N)]

print_stars(N)
for i in range(N):
    for j in range(N):
        print(g[i][j],end='')
    print()
