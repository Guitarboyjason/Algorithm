N = int(input())
cards = list(map(int,input().split()))

origin_sum = 0
for i in range(N):
    if i % 2 == 0:
        origin_sum += cards[i]
ans = origin_sum

junghoon_mitjang = origin_sum
for i in range(N-1,0,-2):
    junghoon_mitjang += cards[i]
    junghoon_mitjang -= cards[i-1]
    ans = max(ans,junghoon_mitjang)

junghoon_mitjang = origin_sum
for i in range(N-2,0,-2):
    junghoon_mitjang -= cards[i]
    junghoon_mitjang += cards[i-1]
    ans = max(ans,junghoon_mitjang)
print(ans)
    # 5 3 1
    # 4 2

