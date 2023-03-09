# 가로등의 높이가 같아야 한다. 정수여야 한다.
# 높이가 H라면 좌 우로 H만큼 비춘다.

N = int(input())
M = int(input())
locations = list(map(int,input().split()))
# 떨어진 정도를 찾으면 될 듯,
# 가장 멀리 떨어져 있는 가로등의 길이를 알면 된다.
# 그 길이의 //2 만큼 높이가 필요함.
# 10만개가 가능하기 때문에 O(N^2)으로는 접근하면 안됨.

# 0과 -1 에 가로등이 없을 때를 확인 해줘야 할듯.
# 근데 한번 호출만에 거리를 알 수 있겠는데?


# 처음과 마지막의 거리는 나중에 한번 더 확인해주자
max = 0

for i in range(M-1):
    tmp = locations[i+1]-locations[i]
    if tmp % 2 == 1:
        tmp = tmp//2 + 1
    else:
        tmp = tmp // 2
    if max< tmp:
        max = tmp
if locations[0] > max:
    max = locations[0]
if N - locations[-1] > max:
    max = N-locations[-1]

print(max)
