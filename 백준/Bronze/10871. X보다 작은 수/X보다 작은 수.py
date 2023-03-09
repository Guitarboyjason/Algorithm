n, x = map(int,input().split())
list = []
list.extend(input().split())
for i in range(n):
    if int(list[i]) < x:
        print(list[i],end=" ")
