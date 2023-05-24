'''
가장 느린 시간은 아마 한쪽 방향으로 모두 이동하는것...? 이 아닐지도 몰라
'''
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    len_stick,num_ants = map(int,input().split())
    n_min = 1_000_001
    n_max = -1
    middle_position = -1
    for _ in range(num_ants):
        position = int(input())
        # print([position, len_stick-position])
        t_n_max = max(position, len_stick-position)
        t_n_min = min(position, len_stick-position)
        if t_n_max > n_max:
            n_max = t_n_max
        if n_min > t_n_max - t_n_min:
            n_min = t_n_max - t_n_min
            middle_position = t_n_min
    # print(n_max)
    # print(middle_position)
    print(middle_position,n_max)