
N = int(input())
vote = []
for _ in range(N):
    vote.append(int(input()))
cnt = 0
while vote.index(max(vote)) != 0:
    cnt += 1
    vote[vote.index(max(vote))] -= 1
    vote[0] += 1
if vote.count(vote[0]) == 1:
    print(cnt)
else:
    print(cnt + 1)