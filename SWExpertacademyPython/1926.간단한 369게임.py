import sys
sys.stdin = open("sources/input-4.txt")

N = int(input())
clap = ["3", "6", "9"]
for i in range(1, N+1):
    not_clap = True
    for j in str(i):
        if j in clap:
            print("-", end="")
            not_clap = False
    if not_clap:
        print(i, end="")
    print(" ", end="")
