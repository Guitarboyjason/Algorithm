"""
정사각형은 서로 겹치면 안된다.
도형은 모두 연결되어 잇어야 한다.
정사각형의 변끼리 연결되어있어야 한다.
정사각형 4개를 이어붙인 테트로미노

테트로미노 하나를 적절히 놓아서 놓인 칸에 쓰여있는 수들의 합을 최대로 하는 프로그램

회전 혹은 대칭도 가능


가능한 경우의 수가 2 + 1 + 4 + 4 + 4 -> 15
15 * N * M = 15 * 500 * 500 < 4_000_000
가능은 할 것 같네
"""
import sys
from pprint import pprint

# 네 방향으로 네번 이동하는 모든 경우의 수를 다 구해놓을까

poss_list = set()
# poss_list = list()
direction = [[0, 1], [0, -1], [-1, 0], [1, 0]]

# 저장할 때 x 기준 제일 작은걸 0으로 두고, y도 마찬가지. 이걸로 중복을 제거하자
# 그냥 일자 바에다가 하나씩 붙이자
r_tmp = [(0, 0), (1, 0)]
c_tmp = [(0, 0), (0, 1)]
for i in range(4):
    nx, ny = direction[i]
    for j in range(4):
        nnx, nny = direction[j]

        for component in r_tmp:
            t_tmp = r_tmp.copy()
            t_tmp.append((component[0] + nx, component[1] + ny))
            t_tmp.append((component[0] + nnx, component[1] + nny))
            if len(set(t_tmp)) < 4:
                continue
            t_tmp.sort()
            x_start, y_start = t_tmp[0]
            t_tmp = [(i[0] - x_start, i[1] - y_start) for i in t_tmp]
            poss_list.add(tuple(t_tmp))
        for component in c_tmp:
            t_tmp = c_tmp.copy()
            t_tmp.append((component[0] + nx, component[1] + ny))
            t_tmp.append((component[0] + nnx, component[1] + nny))
            if len(set(t_tmp)) < 4:
                continue
            t_tmp.sort()
            x_start, y_start = t_tmp[0]
            t_tmp = [(i[0] - x_start, i[1] - y_start) for i in t_tmp]
            poss_list.add(tuple(t_tmp))
pprint(poss_list)

# for i in range(4):
#     tmp = [[0, 0]]
#     t = direction[i]
#     tmp.append(t)
#     for j in range(4):
#         t_j = t.copy()
#         j_tmp = tmp.copy()
#         t_j[0] += direction[j][0]
#         t_j[1] += direction[j][1]
#         if t_j not in j_tmp:
#             j_tmp.append(t_j)
#         else:
#             continue
#         for k in range(4):
#             k_tmp = j_tmp.copy()
#             t_k = t_j.copy()
#             t_k[0] += direction[k][0]
#             t_k[1] += direction[k][1]
#             if t_k not in k_tmp:
#                 k_tmp.append(t_k)
#             else:
#                 continue
#             # print(k_tmp)
#             k_tmp.sort()
#             x_start = k_tmp[0][0]
#             y_start = k_tmp[0][1]
#             for i in k_tmp:
#                 i[0] -= x_start
#                 i[1] -= y_start
#             # tmp.sort(key=lambda x: x[1])
#             # y_start = tmp[0][1]
#             # for i in tmp:
#             #     i[1] -= y_start
#             k_tmp = tuple(tuple(i) for i in k_tmp)
#             # print(k_tmp)
#             # print(set(k_tmp))
#             poss_list.add(tuple(k_tmp))
#             # poss_list.append(k_tmp)
# # print(poss_list)
# # poss_list = set(poss_list)
# pprint(poss_list)

input = sys.stdin.readline
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 완탐으로 풀어보자

summary_list = []
for i in range(N):
    for j in range(M):
        for pos in poss_list:
            for nx, ny in pos:
                nx += i
                ny += j
                if 0 <= nx < N and 0 <= ny < M:
                    pass
                else:
                    break
            else:
                # if sum([board[nx + i][ny + j] for nx, ny in pos]) == 20:
                #     print(i, j, pos)
                summary_list.append(sum([board[nx + i][ny + j] for nx, ny in pos]))

print(max(summary_list))
