""" 
학생들에게 1이상이고 스위치 개수 이하인 자연수를 하나씩 준다.
남학생 : 스위치 번호가 자기가 받은 수의 배수면 그 !스위치
여학생 : 받은 스위치를 중심으로 좌우 대칭이면서 가장 많은 스위치를 포함하는 구간 (가장 길게 대칭인 구간) 그 구간의 스위치 모두를 바꾼다.
        이때 구간에 속한 스위치의 갯수는 항상 홀수
"""

import sys

input = sys.stdin.readline


def solution(student, switch):
    if student == 1:
        male_student(switch)
    else:
        female_student(switch)


def male_student(switch):
    for i in range(switch, num_switches + 1, switch):
        switches[i] = not switches[i]


def female_student(switch):
    limit = -1
    l_switches = num_switches
    if switch <= l_switches // 2:  # 5 <= 4 -> False
        limit = 1
    # if limit == 1: # 왼족이랑 비교 .. ?
    else:
        limit = l_switches
    switches[switch] = not switches[switch]
    for i in range(1, abs(limit - switch) + 1):
        if switches[switch + i] == switches[switch - i]:
            switches[switch + i] = not switches[switch + i]
            switches[switch - i] = not switches[switch - i]
        else:
            break


num_switches = int(input())  # 9
switches = [-1] + list(map(int, input().split()))

num_students = int(input())  # 2
for _ in range(num_students):
    student, switch = map(int, input().split())
    solution(student, switch)  # 2, 5
# print([i for i in switches if i == True i = 1 else 0])
for idx, i in enumerate(switches):
    if i == True:
        switches[idx] = 1
    elif i == False:
        switches[idx] = 0
# print(*switches[1:])
for i in range(1, num_switches + 1):
    if i != 1 and (i - 1) % 20 == 0:
        print()
    print(switches[i], end=" ")
