import math

N = int(input())
n = math.ceil(math.log2(N))
# N => 2^n - x
# 1 --> 1
# 2 --> 2
# 3 --> 2
# 4 --> 4
# ...
# 8 --> 8
# 9 --> 2

#2^n - x --> 2^n - 2*x
#N = 2^n - 2*x
#2^n = N+2x
#n = log2(N+2x)


#9일때는 2^4-2*7


x = 2**n - N

result = 2**n - 2*x

print(result)
