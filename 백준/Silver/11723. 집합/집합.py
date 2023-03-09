import sys
input = sys.stdin.readline
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
for _ in range(int(input())):
    command = input().split()
    if len(command) == 2:
        command,number = command[0],int(command[1])
        if command == "check":
            print(locals()[command](number))
        else:
            locals()[command](number)
    else:
        command = command[0]
        locals()[command]()