num = int(input())
count = 0
for i in range(1,num+1):
    if len(str(i)) == 3 :
        a = i // 100
        b = (i - a*100) // 10
        c = i % 10
        if (a-b) == (b-c):
            count += 1
    elif i == 1000 :
        pass
    else :
        count += 1
print(count)
