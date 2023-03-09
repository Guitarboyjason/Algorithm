N = int(input())
scores_clear_level = [int(input())for _ in range(N)]

before_score = scores_clear_level[-1]
cnt = 0
for i in range(N-2, -1, -1):
    while scores_clear_level[i] >= before_score:
        cnt += 1
        scores_clear_level[i] -= 1
    else:
        before_score = scores_clear_level[i]
print(cnt)
