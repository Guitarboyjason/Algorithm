#아 괄호를 하나씩 벗겨보는거
#(의 갯수랑 )의 갯수를 비교
#배치되어있는 모양을 확인해야함.
#(이면 재귀로 들어감
#)이면 나옴


def find_VPS(string,cnt):
    if len(string) != 0:
        if string[0] == "(":
            find_VPS(string[1:],cnt+1)
        else:
            return cnt-1
        return ()

T = int(input())
for _ in range(T):
    string = input()
    if len(string) %2 == 1:
        print("NO")
    else:
