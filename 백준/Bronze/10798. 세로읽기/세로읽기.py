lines = [list(input())for _ in range(5)]

for i in range(len(max(lines,key=lambda x:len(x)))):
    for j in range(5):
        if len(lines[j]) <= i:
            continue
        else:
            print(lines[j][i],end="")
