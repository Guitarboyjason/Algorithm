

quarter = 25
dime = 10
nickel = 5
penny = 1

T = int(input())
for _ in range(T):
    C = int(input())
    q, d, n, p = 0, 0, 0, 0
    q = C//quarter
    C %= quarter
    d = C // dime
    C %= dime
    n = C // nickel
    C %= nickel
    p = C // penny
    C %= penny

    print("{} {} {} {}".format(q, d, n, p))
