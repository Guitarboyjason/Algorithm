# 딸 초 바


N = int(input())
milk = list(map(int, input().split()))
milk_want = 0
cnt = 0
for i in milk:
    if i == milk_want:
        cnt += 1
        milk_want += 1
        if milk_want == 3:
            milk_want = 0
print(cnt)
