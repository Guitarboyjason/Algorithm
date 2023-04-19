# 게임 횟수 : X
# 이긴 게임 : Y, (Z%)
# Z 는 형택이의 승률, 소수점은 버림.
# X와 Y가 주어질 때, 형택이가 게임을 최소 몇 번 더 해야 Z가 변하는지 구하라

# Z가 절대 변하지 않는다면 -1을 출력

X,Y = map(int,input().split())
Z =(100 * Y)//X

min_cnt = 1
max_cnt = X

if Z >= 99:
    print(-1)

else:
    start = 0
    end = X
    while start <= end:
        mid = (start+end) // 2
        # if int((Y+mid)/(X+mid) * 100) == Z+1:
        #     k = end
        #     end = mid-1
        if (100 * (Y+mid))//(X+mid) == Z:   #같을 때는 확인하지 않고
            start = mid+1
        else:                               # 다를 때만 구분지어 확인하자.
            end = mid-1
            k = mid

    print(k)


# 야발,,, 왜 안되는데,,,,
