# 최소 공배수는 최대 공약수를 제외한 나머지를 곱해서 만듦
# 혹은 두 수를 곱하고 최대 공약수로 나누는 것도 방법

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)
A,B = map(int,input().split())
print(int(A*B/gcd(A,B)))