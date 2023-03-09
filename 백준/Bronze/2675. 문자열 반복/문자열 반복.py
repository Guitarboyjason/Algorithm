import sys
tstCase = int(input())
for _ in range(tstCase):
    num,word = sys.stdin.readline().split()
    num = int(num)
    for i in word:
        print(i*num,end="")
    print()
