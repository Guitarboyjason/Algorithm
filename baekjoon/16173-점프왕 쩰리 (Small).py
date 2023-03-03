#정사각형 구역 내부에서만 움직일 수 있다.
#출발점은 항상 정사각형의 가장 왼쪽, 가장 위의 칸이다.
#이동 가능한 방향은 오른쪽과 아래 뿐이다.
#가장 오른쪽 가장 아래칸에 도달하면 승리한다.
#한번에 이동할 수 있는 칸의 수는 현재 밟고 있는 칸에 쓰여 있는 수.
#수보다 많거나 적게 이동할 수 없다.

N = int(input())
arr = [[-1]*(N+1)]
for _ in range(N):
    # tmp = list(map(int,input().split()))
    # print(tmp)
    arr.append([-1]+list(map(int,input().split())))

def can_i_get_last(arr, x, y):
    if arr[y][x] == -1:
        return 'HaruHaru'
    elif y == N:

    else:
        int(arr[y][x])

print(arr)

