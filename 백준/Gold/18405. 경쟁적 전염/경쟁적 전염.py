# 모든 바이러스는 1초마다 상하좌우 방향으로 증식.
# 매 초 번호가 낮은 종류의 바이러스 먼저 증식
# 특정 칸에 이미 바이러스가 있다면 그 곳에는 다른 바이러스가 들어갈 수 없다.

# 시험관의 크기와 바이러스의 위치 정보가 주어졌을 때, S초 이후 (X,Y)에 존재하는 바이러스의
# 종류를 출력
# S초 이후 해당 위치에 바이러스가 존재하지 않는다면 0을 출력.X와 Y는 행과 열.
# 가장 왼쪽 위는 (1,1)
# 결국 (X,Y)에 가장 가까운 바이러스 근원지가 어디인가를 구하는 문제인 것 같다.
# 만약 거리가 같다면 작은 수를 print.
# 또 떨어진 숫자보다 S가 크거나 같지 않으면 0을 print.

N,K = map(int,input().split())

arr = [[0]* (N+1)]
for _ in range(N):
    arr.append([0]+list(map(int,input().split())))

S,X,Y = map(int,input().split())
# print(arr)

min = 400
tmp = 0
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] != 0:
            if abs(i-X) + abs(j-Y) < min:
                min = abs(i-X) + abs(j-Y)
                tmp = arr[i][j]
            elif abs(i-X) + abs(j-Y) == min:
                if tmp > arr[i][j]:
                    tmp = arr[i][j]

if S >= min:
    print(tmp)
else:
    print(0)
# 떨어진 정도를 어떻게 보나.
# 1,1 에 바이러스가 존재하고
# 5, 3 을 확인한다 하면
# 결국 4 + 2인것 같다.
