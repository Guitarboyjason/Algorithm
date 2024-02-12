"""
비용 : 키가 가장 큰 원생, 키가 가장 작은 원생의 키 차이
비용의 합을 최소
"""

N, K = map(int, input().split())
students = list(map(int, input().split()))

# 왼쪽이 오른쪽보다 크지 않다.
# N = 5, K = 3
# 2 2 1 4

diffs = [students[i] - students[i - 1] for i in range(1, N)]
diffs.sort()
print(sum(diffs[: N - K]))
