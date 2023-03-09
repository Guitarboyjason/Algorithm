
N = int(input())
tips = [int(input())for _ in range(N)]

tips.sort(reverse=True)
cnt = 0
for i in range(N):
    tip = tips[i] - i
    if tip < 0:
        tip = 0
        break
    cnt += tip
print(cnt)
