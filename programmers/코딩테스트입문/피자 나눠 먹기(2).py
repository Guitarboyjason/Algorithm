def gcd(r1,r2):
    while(r2):
        r1,r2 = r2,r1%r2
    return r1

def solution(n):
    return n  // gcd(n,6)

print(solution(4))
