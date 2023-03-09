A,B,N = map(int,input().split())
# 10000
# 101
#
A %= B
for i in range(N-1):
    A = (A*10)%B
print((A*10)//B)
