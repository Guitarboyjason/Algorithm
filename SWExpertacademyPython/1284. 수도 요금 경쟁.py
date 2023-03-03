import sys
sys.stdin = open("sources/input-8.txt", "r")
T = int(input())
for test_case in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    if R >= W:
        print("#{} {}".format(test_case, min(P*W, Q)))
    else:
        print("#{} {}".format(test_case, min(P*W, Q+(W-R)*S)))
