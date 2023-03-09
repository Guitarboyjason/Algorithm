N = input()
arr = []
for i in N :
    arr.append(int(i))
if sum(arr) % 3 == 0 and 0 in arr:
    arr.sort(reverse=True)
    for i in arr:
        print("%d"%i,end="")
else:
    print(-1)

