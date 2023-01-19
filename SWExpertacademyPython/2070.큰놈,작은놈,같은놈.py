T = int(input())
case = 1
for i in range(T):
    a,b = map(int,input().split())
    if a>b:
        answer = ">"
    elif a<b:
        answer = "<"
    else:
        answer = "="
    print(f"#{case} {answer}")
    case += 1
