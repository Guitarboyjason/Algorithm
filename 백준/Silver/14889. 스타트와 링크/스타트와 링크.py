# N명이 모임. N은 짝수.
# 스타트팀, 링크팀
# 능력치 : i 와 j가 같은팀에 속했을 때 팀에 더해지는 능력치
# Sij 와 Sji를 다 더해야 한다.
# 능력치의 차이를 최소로 하라.

# 일단 무조건적으로 능력을 합으로 생각을 한다면,
# 어차피 능력치의 차이의 최솟값만 출력하면 되므로,
# 반 접어서 더한 값을 먼저 확인한다.

from itertools import combinations
import math
N = int(input())

arr = [list(map(int,input().split())) for i in range(N)]

# i = j 일때는 고려하지 않는다.

# 편은 a, b팀 둘로 나뉜다.
# 그럼 x와 함께하는 사람들은 N/2 - 1 이다.
# 나머지는 다른팀이 될 것.

# 그럼 i = 0일 때 combination N/2-1 만큼을 하고,
# 나머지들을 확인하면 될 것.

# 00 01 02 03
# 10 11 12 13
# 20 21 22 23
# 30 31 32 33

for i in range(N): # 절반 이상일때만 확인을 할까
    for j in range(i+1,N):
        arr[i][j] += arr[j][i]
        arr[j][i] = arr[i][j]           #초기화를 하자 필수는 아님 --> 같은 값을 넣어줌

arr_N = [i for i in range(N)] # 0 1 2 3

arr_posibility = list(combinations(arr_N,N//2))     # 편을 나눌 수 있는 경우의 수
# print(arr_posibility)
# 나머지는 자동으로 설정됨.
min = 10000
for i in arr_posibility:
    if 0 in i:     # 모든 경우의 수 중에서 0을 특정지어 확인한다.
        # for j in i:
        #     if j != 0:
        #         team_zero = j
        team_zero = i
        team_others = []
        for k in arr_N:
            if k not in team_zero:
                team_others.append(k)
        score_zero = 0
        score_others = 0
        for k in combinations(team_zero,2):
            # print(k)
            # print(arr[k[0]][k[1]])
            score_zero+= arr[k[0]][k[1]]
                # score_zero += arr[0][k]     # 근데 0과 같은 팀인 사람들 시너지도 확인 해야함
        for k in combinations(team_others,2):
            score_others += arr[k[0]][k[1]]
        result  = abs(score_zero-score_others)
        if result < min :
            min = result    # 간단하게 쓰는 방법이 있을텐데
print(min)
