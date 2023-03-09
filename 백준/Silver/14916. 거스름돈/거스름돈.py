n = int(input())
cnt = 0
if n < 5 :
    if n % 2 == 1:
        print(-1)
    else:
        print(n//2)
else:
    cnt += n // 5
    n = n % 5
    if n % 2 == 1:
        cnt -= 1
        n += 5

    cnt += n // 2
    print(cnt)
