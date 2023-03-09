def chicken(n,k):
    cnt = n
    while n >= k:
        tmp = n // k
        cnt += tmp
        n = n % k
        n += tmp
    return cnt

while True:
    try:
        n,k = map(int,input().split())
        print(chicken(n,k))
    except EOFError:
        break
# 5 + 2 +
