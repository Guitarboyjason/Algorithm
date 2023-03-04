#add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
# remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
# check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
# toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
# all: S를 {1, 2, ..., 20} 으로 바꾼다.
# empty: S를 공집합으로 바꾼다. 

# M = int(input())
import sys
sys.stdin = open("baekjoon/input.txt","r")
S = set()
def add(number):
    S.add(number)

def remove(number):
    
    if number in S:
        S.remove(number)
        
def check(number):
    
    if number in S:
        return 1
    else:
        return 0

def toggle(number):
    
    if check(number):
        S.remove(number)
    else:
        S.add(number)

def all():
    global S
    S = {i for i in range(1,21)}
    
def empty():
    global S
    S = set()
    
# command_dict = {"add":add(number),"remove":remove(number),"check":check(number),\
#     "toggle":toggle(number),"all":all(number),"empty":empty(number)}
for _ in range(int(input())):
    command = input().split()
    # number = None
    if len(command) == 2:
        # print(command)
        command,number = command[0],int(command[1])
        if command == "check":
            print(locals()[command](number))
        else:
            locals()[command](number)
        # tmp = locals()[command](number)
        # if tmp != None:
        #     print(tmp)
    else:
        command = command[0]
        locals()[command]()
    # print(command_dict[command])
    
    # if command == "add":
        
