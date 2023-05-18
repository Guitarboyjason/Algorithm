# 예상 등수가 A인데 B인 경우, 불만도는 |A-B|로 수치화 할 수 있다.
# 불만도의 총 합을 최소로
# 불만도의 합을 최소로 하는 프로그램

# 한 등수를 예상하는 사람이 많으면 사실 불만이 많아지게 될 것
import sys

input = sys.stdin.readline

N = int(input())
expected = [int(input()) for _ in range(N)]
# grade = {i:0 for i in range(1,N+1)}

# print(expected)

# for i in expected:
#     grade[i] += 1
# changed = []
expected.sort()

compare = [i + 1 for i in range(N)]
answer = 0
for i in range(N):
    answer += abs(compare[i] - expected[i])
print(answer)
