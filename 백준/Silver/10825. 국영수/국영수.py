import sys
input = sys.stdin.readline
N = int(input())
students = [list(input().split())for _ in range(N)]
students.sort(key=lambda x : x[0])
students.sort(key=lambda x : int(x[3]),reverse=True)
students.sort(key=lambda x : int(x[2]))
students.sort(key=lambda x : int(x[1]),reverse=True)

for student in students:
    print(student[0])