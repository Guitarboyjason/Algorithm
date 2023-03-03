#두 정수 K,L이 주어진다.
#좋은 암호 - GOOD, 나쁜 암호 -BAD
#K를 인수분해 했을 때 항상 L 이상의 값으로만 이루어져 있는지
def password(K,L):
    for i in range(2,L):
        if K%i == 0:
            return("BAD %d"%i)
            break
    return("GOOD")

K,L = map(int,input().split())
print(password(K,L))
