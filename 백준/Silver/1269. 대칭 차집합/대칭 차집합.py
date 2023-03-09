#1269-대칭차집합.py

#대칭 차집합 : (A-B) + (B-A)
#대칭 차집합의 갯수는 A + B - (A^B)*2를 하면 될 것

import sys
A_num,B_num = map(int,sys.stdin.readline().split())
A = list(map(int,sys.stdin.readline().split()))
tmp_A = {}
for i in range(len(A)):
    tmp_A[A[i]] = i
B = list(map(int,sys.stdin.readline().split()))
count= 0 
for i in B:
    if i in tmp_A:
        count += 1
print(len(A) + len(B) - 2*count)