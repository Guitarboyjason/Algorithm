import math
D, H, W = map(int, input().split())
length = D / math.sqrt(H**2+W**2)
print(int(H * length), int(W*length))
