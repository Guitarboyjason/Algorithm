"""
정오에 한번 자란다.
첫날 아침 모든 애벌레들의 크기는 1 

커지는 정도는 +0,+1,+2 중 하나
1. 제일 왼쪽 열과, 제일 위쪽 행의 애벌레들은 자신이 자라는 정도를 스스로 결정. 이것을 입력으로 받음.. 모든 입력에서 이러한 값들은 감소하지 않는다.
2. 나머지 애벌레들은 자신의 왼쪽, 왼쪽위, 위쪽의 애벌레들이 다 자란 이후 그날 가장 많이 자란 애벌레가 자란만큼 자신도 자란다.

읽는 순서가 힌트네

"""
from pprint import pprint


def bug_grow(n_growing):
    i, j = M - 1, 0
    for g in n_growing:
        bugs[i][j] += g
        if i == 0:
            j += 1
        else:
            i -= 1
    steps = 1
    after_update(steps)


directions = [(-1, 0), (-1, -1), (-1, 0)]


def after_update(steps):
    n = N - steps * 2
    if n <= 0:
        return
    i, j = M - 1, steps
    # grow_list = []
    while i != steps and j != M - 1:
        bugs[i][j] += max(bugs[i + k[0]][j + k[1]] for k in directions)
        if i != steps:
            i -= 1
        else:
            j += 1
    after_update(steps + 1)


M, N = map(int, input().split())

growth = [list(map(int, input().split())) for _ in range(N)]


bugs = [[1 for _ in range(M)] for _ in range(M)]
# print(bugs)
for n_growing in growth:
    # pass
    bug_grow(n_growing)
    pprint(bugs)
